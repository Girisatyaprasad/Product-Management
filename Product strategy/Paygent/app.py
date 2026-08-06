import threading
import time
import uuid
from collections import deque
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

class PaygentV0:
    __slots__ = (
        "lock", "active", "limit", "available",
        "reservations", "requests", "audit"
    )

    def __init__(self, limit=500000):  # paise = INR 5,000
        if type(limit) is not int or limit <= 0:
            raise ValueError("INVALID_LIMIT")

        self.lock = threading.Lock()
        self.active = True
        self.limit = limit
        self.available = limit

        # rid -> (agent, amount, expires_ns, request_id)
        self.reservations = {}

        # request_id -> previous response
        self.requests = {}

        self.audit = deque(maxlen=1000)

    def _log(self, action, agent, amount, result):
        self.audit.append(
            (time.time_ns(), action, agent, amount, result, self.available)
        )

    def _expire(self, now):
        expired = [
            rid for rid, (_, amount, expiry, _)
            in self.reservations.items()
            if expiry <= now
        ]

        for rid in expired:
            _, amount, _, request_id = self.reservations.pop(rid)
            self.available = min(self.limit, self.available + amount)
            self._clear_request(request_id, rid)
            self._log("EXPIRE", None, amount, "EXPIRED")

    def _clear_request(self, request_id, rid):
        previous = self.requests.get(request_id)
        if (
            previous and
            previous.get("status") == "APPROVED" and
            previous.get("reservation_id") == rid
        ):
            del self.requests[request_id]

    def authorize(self, request_id, agent, amount, ttl_s=600):
        if (
            not request_id or
            not agent or
            type(amount) is not int or
            amount <= 0
        ):
            return {"status": "DENIED", "reason": "INVALID_REQUEST"}

        with self.lock:
            now = time.monotonic_ns()
            self._expire(now)

            previous = self.requests.get(request_id)
            if previous:
                return previous

            if not self.active:
                result = {"status": "DENIED", "reason": "FROZEN"}

            elif amount > self.available:
                result = {"status": "DENIED", "reason": "LIMIT_EXCEEDED"}

            else:
                rid = uuid.uuid4().hex
                self.available -= amount

                self.reservations[rid] = (
                    agent,
                    amount,
                    now + ttl_s * 1_000_000_000,
                    request_id
                )

                result = {
                    "status": "APPROVED",
                    "reservation_id": rid,
                    "available": self.available
                }

            self.requests[request_id] = result
            self._log("AUTH", agent, amount, result["status"])

            return result

    def confirm(self, agent, rid):
        with self.lock:
            res = self.reservations.get(rid)

            if res is None:
                return {"status": "INVALID_RESERVATION"}

            owner, amount, _, request_id = res

            if owner != agent:
                return {"status": "DENIED", "reason": "AGENT_MISMATCH"}

            del self.reservations[rid]
            self._clear_request(request_id, rid)

            self._log("CONFIRM", agent, amount, "CONFIRMED")
            return {"status": "CONFIRMED"}

    def release(self, agent, rid):
        with self.lock:
            res = self.reservations.get(rid)

            if res is None:
                return {"status": "INVALID_RESERVATION"}

            owner, amount, _, request_id = res

            if owner != agent:
                return {"status": "DENIED", "reason": "AGENT_MISMATCH"}

            del self.reservations[rid]
            self._clear_request(request_id, rid)
            self.available = min(self.limit, self.available + amount)

            self._log("RELEASE", agent, amount, "RELEASED")

            return {
                "status": "RELEASED",
                "available": self.available
            }

    def freeze(self):
        with self.lock:
            self.active = False
            self._log("FREEZE", None, None, "FROZEN")
            return {"status": "FROZEN"}

    def unfreeze(self):
        with self.lock:
            self.active = True
            self._log("UNFREEZE", None, None, "ACTIVE")
            return {"status": "ACTIVE"}

    def state(self):
        with self.lock:
            self._expire(time.monotonic_ns())
            reserved = sum(amount for _, amount, _, _ in self.reservations.values())
            return {
                "active": self.active,
                "limit": self.limit,
                "available": self.available,
                "reserved": reserved,
                "reservation_count": len(self.reservations),
            }

    def audit_log(self):
        with self.lock:
            return [
                {
                    "time_ns": ts,
                    "action": action,
                    "agent": agent,
                    "amount": amount,
                    "result": result,
                    "available": available,
                }
                for ts, action, agent, amount, result, available in self.audit
            ]


class AuthRequest(BaseModel):
    request_id: str
    agent: str
    amount: int


class ReservationRequest(BaseModel):
    agent: str
    reservation_id: str


core = PaygentV0()
app = FastAPI(title="Paygent V0")


@app.post("/authorize")
def authorize(body: AuthRequest) -> dict[str, Any]:
    return core.authorize(body.request_id, body.agent, body.amount)


@app.post("/confirm")
def confirm(body: ReservationRequest) -> dict[str, Any]:
    return core.confirm(body.agent, body.reservation_id)


@app.post("/release")
def release(body: ReservationRequest) -> dict[str, Any]:
    return core.release(body.agent, body.reservation_id)


@app.post("/freeze")
def freeze() -> dict[str, Any]:
    return core.freeze()


@app.post("/unfreeze")
def unfreeze() -> dict[str, Any]:
    return core.unfreeze()


@app.get("/state")
def state() -> dict[str, Any]:
    return core.state()


@app.get("/audit")
def audit() -> list[dict[str, Any]]:
    return core.audit_log()

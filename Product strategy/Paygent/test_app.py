import time

from fastapi.testclient import TestClient

import app as app_module
from app import PaygentV0


def make_client():
    app_module.core = PaygentV0()
    return TestClient(app_module.app)


def test_confirm_keeps_reservation_consumed():
    client = make_client()

    approved = client.post(
        "/authorize",
        json={"request_id": "req-a", "agent": "agent-a", "amount": 300000},
    ).json()

    assert approved["status"] == "APPROVED"
    assert approved["available"] == 200000
    assert client.get("/state").json() == {
        "active": True,
        "limit": 500000,
        "available": 200000,
        "reserved": 300000,
        "reservation_count": 1,
    }

    confirmed = client.post(
        "/confirm",
        json={"agent": "agent-a", "reservation_id": approved["reservation_id"]},
    ).json()
    assert confirmed == {"status": "CONFIRMED"}

    assert client.get("/state").json() == {
        "active": True,
        "limit": 500000,
        "available": 200000,
        "reserved": 0,
        "reservation_count": 0,
    }


def test_release_restores_available_authority_after_fresh_authorization():
    client = make_client()

    approved = client.post(
        "/authorize",
        json={"request_id": "req-a", "agent": "agent-a", "amount": 300000},
    ).json()

    released = client.post(
        "/release",
        json={"agent": "agent-a", "reservation_id": approved["reservation_id"]},
    ).json()
    assert released == {"status": "RELEASED", "available": 500000}

    assert client.get("/state").json() == {
        "active": True,
        "limit": 500000,
        "available": 500000,
        "reserved": 0,
        "reservation_count": 0,
    }


def test_freeze_denies_new_authorizations_and_unfreeze_allows_again():
    client = make_client()

    assert client.post("/freeze").json() == {"status": "FROZEN"}
    denied = client.post(
        "/authorize",
        json={"request_id": "req-frozen", "agent": "agent-a", "amount": 100000},
    ).json()
    assert denied == {"status": "DENIED", "reason": "FROZEN"}

    assert client.post("/unfreeze").json() == {"status": "ACTIVE"}
    approved = client.post(
        "/authorize",
        json={"request_id": "req-active", "agent": "agent-a", "amount": 100000},
    ).json()
    assert approved["status"] == "APPROVED"
    assert approved["available"] == 400000


def test_state_and_audit_endpoints():
    client = make_client()

    client.post(
        "/authorize",
        json={"request_id": "req-a", "agent": "agent-a", "amount": 125000},
    )
    state = client.get("/state").json()
    audit = client.get("/audit").json()

    assert state == {
        "active": True,
        "limit": 500000,
        "available": 375000,
        "reserved": 125000,
        "reservation_count": 1,
    }
    assert audit[-1]["action"] == "AUTH"
    assert audit[-1]["agent"] == "agent-a"
    assert audit[-1]["amount"] == 125000
    assert audit[-1]["result"] == "APPROVED"
    assert audit[-1]["available"] == 375000


def test_released_request_id_can_authorize_again_without_stale_approval():
    core = PaygentV0()

    first = core.authorize("req-a", "agent-a", 300000)
    assert first["status"] == "APPROVED"
    assert core.release("agent-a", first["reservation_id"]) == {
        "status": "RELEASED",
        "available": 500000,
    }

    second = core.authorize("req-a", "agent-a", 250000)
    assert second["status"] == "APPROVED"
    assert second["reservation_id"] != first["reservation_id"]
    assert second["available"] == 250000


def test_confirmed_request_id_can_authorize_again_without_stale_approval():
    core = PaygentV0()

    first = core.authorize("req-a", "agent-a", 300000)
    assert first["status"] == "APPROVED"
    assert core.confirm("agent-a", first["reservation_id"]) == {"status": "CONFIRMED"}

    second = core.authorize("req-a", "agent-a", 100000)
    assert second["status"] == "APPROVED"
    assert second["reservation_id"] != first["reservation_id"]
    assert second["available"] == 100000


def test_expired_request_id_can_authorize_again_without_stale_approval():
    core = PaygentV0()

    first = core.authorize("req-a", "agent-a", 300000, ttl_s=0)
    assert first["status"] == "APPROVED"

    second = core.authorize("req-a", "agent-a", 250000)
    assert second["status"] == "APPROVED"
    assert second["reservation_id"] != first["reservation_id"]
    assert second["available"] == 250000


def test_authorization_default_ttl_is_ten_minutes():
    core = PaygentV0()

    approved = core.authorize("req-a", "agent-a", 100000)
    _, _, expires_ns, _ = core.reservations[approved["reservation_id"]]
    remaining_s = (expires_ns - time.monotonic_ns()) / 1_000_000_000

    assert 590 <= remaining_s <= 600

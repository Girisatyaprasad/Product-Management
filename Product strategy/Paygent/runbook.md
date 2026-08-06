# Paygent V0 — Operational Runbook

Experimental prototype. No real funds are moved or held by Paygent V0.

---

## 1. Development & Testing Commands

| Phase | Operation | PowerShell / Terminal Command |
| :--- | :--- | :--- |
| **Setup** | Install dependencies | `python -m pip install -r requirements.txt` |
| **Test** | Run unit test suite | `python -m pytest -q` |
| **Serve** | Start local server | `python -m uvicorn app:app --reload` |
| **Verify** | Execute full smoke test | `.\smoke_test.ps1` |

---

## 2. API Endpoint Reference

| Method | Endpoint | Example Request Payload | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/state` | *None* | Returns limits, available balance, and active reservations |
| `POST` | `/authorize` | `{"request_id":"req-1", "agent":"Agent-A", "amount":300000}` | Reserves spending authority for an agent |
| `POST` | `/confirm` | `{"agent":"Agent-A", "reservation_id":"<id>"}` | Marks reservation as settled/consumed |
| `POST` | `/release` | `{"agent":"Agent-A", "reservation_id":"<id>"}` | Cancels reservation and restores authority limit |
| `POST` | `/freeze` | *None* | Pauses all new authorization requests |
| `POST` | `/unfreeze` | *None* | Resumes system authorization |
| `GET` | `/audit` | *None* | Retrieves complete state transition audit log |

---

## 3. Manual Verification Steps (PowerShell)

| Step | Action | PowerShell Command |
| :---: | :--- | :--- |
| **1** | Check Initial State | `Invoke-RestMethod "http://127.0.0.1:8000/state"` |
| **2** | Authorize Agent A | `$a = Invoke-RestMethod "http://127.0.0.1:8000/authorize" -Method Post -ContentType "application/json" -Body '{"request_id":"manual-a","agent":"Agent A","amount":300000}'` |
| **3** | View Updated State | `Invoke-RestMethod "http://127.0.0.1:8000/state"` |
| **4** | Confirm Reservation | `Invoke-RestMethod "http://127.0.0.1:8000/confirm" -Method Post -ContentType "application/json" -Body (@{agent="Agent A"; reservation_id=$a.reservation_id} \| ConvertTo-Json)` |
| **5** | Freeze System | `Invoke-RestMethod "http://127.0.0.1:8000/freeze" -Method Post` |
| **6** | Attempt Blocked Auth | `Invoke-RestMethod "http://127.0.0.1:8000/authorize" -Method Post -ContentType "application/json" -Body '{"request_id":"manual-frozen","agent":"Agent B","amount":250000}'` |
| **7** | Unfreeze System | `Invoke-RestMethod "http://127.0.0.1:8000/unfreeze" -Method Post` |
| **8** | Authorize Agent B | `$b = Invoke-RestMethod "http://127.0.0.1:8000/authorize" -Method Post -ContentType "application/json" -Body '{"request_id":"manual-b","agent":"Agent B","amount":250000}'` |
| **9** | Release Reservation | `Invoke-RestMethod "http://127.0.0.1:8000/release" -Method Post -ContentType "application/json" -Body (@{agent="Agent B"; reservation_id=$b.reservation_id} \| ConvertTo-Json)` |
| **10** | Retrieve Audit Log | `Invoke-RestMethod "http://127.0.0.1:8000/audit"` |

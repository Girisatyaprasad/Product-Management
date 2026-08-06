# Paygent V0 - Interactive API Smoke Test
$ErrorActionPreference = "Stop"
$base = "http://127.0.0.1:8000"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " 1. INITIAL SYSTEM STATE" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Invoke-RestMethod "$base/state" | Format-List

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " 2. AUTHORIZE AGENT A (INR 3,000)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
$a = Invoke-RestMethod "$base/authorize" -Method Post -ContentType "application/json" -Body '{"request_id":"manual-a","agent":"Agent A","amount":300000}'
$a | Format-List
Invoke-RestMethod "$base/state" | Format-List

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " 3. CONFIRM RESERVATION (AGENT A)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Invoke-RestMethod "$base/confirm" -Method Post -ContentType "application/json" -Body (@{agent="Agent A"; reservation_id=$a.reservation_id} | ConvertTo-Json) | Format-List
Invoke-RestMethod "$base/state" | Format-List

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " 4. FREEZE SYSTEM & ATTEMPT AUTH (EXPECT DENIED)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Invoke-RestMethod "$base/freeze" -Method Post | Format-List
Invoke-RestMethod "$base/authorize" -Method Post -ContentType "application/json" -Body '{"request_id":"manual-frozen","agent":"Agent B","amount":250000}' | Format-List

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " 5. UNFREEZE & AUTHORIZE AGENT B (INR 2,500)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Invoke-RestMethod "$base/unfreeze" -Method Post | Format-List
$b = Invoke-RestMethod "$base/authorize" -Method Post -ContentType "application/json" -Body '{"request_id":"manual-b","agent":"Agent B","amount":250000}'
$b | Format-List

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " 6. RELEASE RESERVATION (AGENT B)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Invoke-RestMethod "$base/release" -Method Post -ContentType "application/json" -Body (@{agent="Agent B"; reservation_id=$b.reservation_id} | ConvertTo-Json) | Format-List
Invoke-RestMethod "$base/state" | Format-List

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " 7. AUDIT TRAIL LOGS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Invoke-RestMethod "$base/audit" | Format-Table

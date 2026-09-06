from app.services.totp_service import generate_ticket_secret, get_current_token, verify_token, build_qr_payload
import time

secret = generate_ticket_secret()
print("Secret:", secret)

code1 = get_current_token(secret)
print("Current code:", code1)

is_valid = verify_token(secret, code1)
print("Is this code valid?", is_valid)

payload = build_qr_payload(ticket_id=1, totp_secret=secret)
print("QR Payload:", payload)
from app.services.totp_service import generate_ticket_secret, get_current_token
import time

secret = generate_ticket_secret()
print("Secret:", secret)

print("Code abhi:", get_current_token(secret))
print("31 second wait kar rahe hain...")

time.sleep(31)

print("Code 31 second baad:", get_current_token(secret))git
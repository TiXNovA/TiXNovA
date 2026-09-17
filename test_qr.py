from app.services.totp_service import generate_ticket_secret, build_qr_payload
from app.services.qr_service import generate_qr_base64
import base64

secret = generate_ticket_secret()
payload = build_qr_payload(1, secret)
print("Payload:", payload)

qr_image = generate_qr_base64(payload)
print("QR base64 length:", len(qr_image))

# Save the actual QR image for visual verification
with open("test_qr.png", "wb") as f:
    f.write(base64.b64decode(qr_image))

print("QR code image saved as test_qr.png in the project root folder.")
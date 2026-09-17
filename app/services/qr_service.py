"""
QR Service — TOTP se mile text ko QR code image mein convert karta hai.
Image ko base64 format mein return karta hai taaki seedha HTML mein
<img> tag ke andar dikhaya ja sake, bina file save kiye disk pe.
"""

import qrcode
import io
import base64


def generate_qr_base64(data: str) -> str:
    """
    'data' string leke ek QR code image banata hai, aur usse
    base64 text mein convert karke return karta hai.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()

    return base64.b64encode(img_bytes).decode("utf-8")
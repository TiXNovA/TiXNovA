"""
TOTP Service — TeXNovA ka core anti-scalping feature.

Har ticket ka apna secret key hota hai. Us secret key aur current time
se ek code generate hota hai jo sirf 30 second ke liye valid hota hai —
bilkul Google Authenticator jaisa. Isse screenshot lekar resell karna
bekaar ho jata hai, kyunki 30 second baad wo code expire ho jayega.
"""

import pyotp


def generate_ticket_secret():
    """Naye ticket ke liye ek random secret key banata hai."""
    return pyotp.random_base32()


def get_current_token(totp_secret, interval=30):
    """Is secret key ke liye ABHI ka valid code kya hai, wo return karta hai."""
    totp = pyotp.TOTP(totp_secret, interval=interval)
    return totp.now()


def verify_token(totp_secret, submitted_token, interval=30):
    """
    Scanner jab QR scan kare, to check karta hai submitted code
    abhi valid hai ya nahi. valid_window=1 se thoda time-drift allow hota hai.
    """
    totp = pyotp.TOTP(totp_secret, interval=interval)
    return totp.verify(submitted_token, valid_window=1)


def build_qr_payload(ticket_id, totp_secret):
    """QR code ke andar ye text jayega: TICKET:<id>:<current_code>"""
    token = get_current_token(totp_secret)
    return f"TICKET:{ticket_id}:{token}"
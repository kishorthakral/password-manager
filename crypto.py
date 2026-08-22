import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_salt():
    # Generate a random salt of 16 bytes
    return os.urandom(16)


def derive_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000
    )
    key = kdf.derive(master_password.encode())
    return base64.urlsafe_b64encode(key)


salt = generate_salt()
print("Salt:", salt.hex())

password = "test123"
key = derive_key(password, salt)
print("Key:", key)
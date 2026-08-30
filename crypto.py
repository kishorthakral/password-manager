import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


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

def encrypt_password(plaintext, key):
    f = Fernet(key)
    # your code here — encrypt plaintext and return it
    return f.encrypt(plaintext.encode())

def decrypt_password(encrypted_text, key):
    f = Fernet(key)
    # your code here — decrypt encrypted_text and return it
    decrypted_bytes = f.decrypt(encrypted_text)
    return decrypted_bytes.decode()

       

salt = generate_salt()
print("Salt:", salt.hex())

password = "test123"
key = derive_key(password, salt)
print("Key:", key)

encrypted = encrypt_password("MyNetflixPassword123", key)
print("Encrypted:", encrypted)

decrypted = decrypt_password(encrypted, key)
print("Decrypted:", decrypted)
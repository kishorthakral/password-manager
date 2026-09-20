import os
from crypto import generate_salt
from storage import save_vault, load_vault

if os.path.exists("vault.json"):
    print("Vault found. Loading...")
    vault_data = load_vault()
    salt = bytes.fromhex(vault_data["salt"])
    #print(load_vault())

else:
    print("No Vault found. Creating a new one...")
    salt = generate_salt()
    salt_hex = salt.hex()
    entries = []
    save_vault(salt_hex, entries)

print("Using Salt:", salt)

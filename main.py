import os
from crypto import derive_key, generate_salt, encrypt_password, decrypt_password
from storage import save_vault, load_vault

if os.path.exists("vault.json"):
    print("Vault found. Loading...")
    vault_data = load_vault()
    salt = bytes.fromhex(vault_data["salt"])
    entries = vault_data["entries"]
    

else:
    print("No Vault found. Creating a new one...")
    salt = generate_salt()
    salt_hex = salt.hex()
    entries = []
    save_vault(salt_hex, entries)

print("Using Salt:", salt)

master_password = input("Enter your master password: ")
key = derive_key(master_password, salt)

label = input("Enter a label (e.g Gmail) for your entry: ")
password_to_store = input("Enter the password you want to store: ")

encrypted_password = encrypt_password(password_to_store, key)
encrypted_password_str = encrypted_password.decode()

new_entry = {"label": label, "password": encrypted_password_str}

entries.append(new_entry)
save_vault(salt.hex(), entries)

print("Password saved!")

print("\nYour saved passwords:")
for entry in entries:
    label = entry["label"]
    encrypted = entry["password"]
    decrypted = decrypt_password(encrypted.encode(), key)
    print(f"Label: {label}, Password: {decrypted}")
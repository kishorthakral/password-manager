import os
from crypto import derive_key, generate_salt, encrypt_password, decrypt_password
from storage import save_vault, load_vault
from getpass import getpass
from cryptography.fernet import InvalidToken

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

master_password = getpass("Enter your master password: ")
key = derive_key(master_password, salt)

while True:
    print("\n--- Password Manager Menu ---")
    print("1. Add a new password")
    print("2. View saved passwords")   
    print("3. Delete a password") 
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        label = input("Enter a label (e.g Gmail) for your entry: ") 
        password_to_store = getpass("Enter the password you want to store: ")
        if not label or not password_to_store:
            print("Label and password cannot be empty.")
            continue
        encrypted_password = encrypt_password(password_to_store, key)
        encrypted_password_str = encrypted_password.decode()
        new_entry = {"label": label, "password": encrypted_password_str}
        entries.append(new_entry)
        save_vault(salt.hex(), entries)
        print("Password saved!")


    elif choice == "2":
        print("\nYour saved passwords:")
        for entry in entries:
            label = entry["label"]
            encrypted = entry["password"]
            try:
                decrypted = decrypt_password(encrypted.encode(), key)
                print(f"Label: {label}, Password: {decrypted}")
            except InvalidToken:
                print(f"Label: {label}, Password: [Decryption Failed - Wrong Master Password]")

    elif choice == "3":
        label_to_delete = input("Enter the label of the password you want to delete: ")
        found = False
        for entry in entries:
            if entry["label"] == label_to_delete:
                entries.remove(entry)
                found = True
                break
        if found:
            save_vault(salt.hex(), entries)
            print(f"Password for label '{label_to_delete}' deleted.")
        else:
            print(f"No entry found for label '{label_to_delete}'.")
                            
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")



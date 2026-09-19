import json

def save_vault(salt, entries, filename="vault.json"):
    vault_data = {
        "salt": salt,
        "entries": entries
    }
    with open(filename, "w") as f:
        json.dump(vault_data, f, indent=4)

save_vault("dca5609047d60a3ced6c4c19eda0d554", [{"label": "Gmail", "password": "test123encrypted"}])
print("Vault saved!")

def load_vault(filename="vault.json"):
    with open(filename, "r") as f:
        vault_data = json.load(f)
    return vault_data

data = load_vault()
print(data)
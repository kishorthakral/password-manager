import json
from crypto import generate_salt

def save_vault(salt, entries, filename="vault.json"):
    vault_data = {
        "salt": salt,
        "entries": entries
    }
    with open(filename, "w") as f:
        json.dump(vault_data, f, indent=4)


def load_vault(filename="vault.json"):
    try:
        with open(filename, "r") as f:
            vault_data = json.load(f)
        return vault_data
    except json.JSONDecodeError:
        print("Error: Vault file is corrupted.")
        return {"salt": generate_salt().hex(), "entries": []}

if __name__ == "__main__":
    # Example usage
    save_vault("dca5609047d60a3ced6c4c19eda0d554", [{"label": "Gmail", "password": "test123encrypted"}])
    print("Vault saved!")

    data = load_vault()
    print(data)


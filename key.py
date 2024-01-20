import secrets

secret_key = secrets.token_hex(16)  # Mendapatkan string hex sepanjang 16 byte
print(secret_key)

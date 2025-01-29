from cryptography.fernet import Fernet

# Generate a new encryption key (store securely in a file/env variable)
ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)

def encrypt(data: str) -> bytes:
    """Encrypt a string using Fernet encryption."""
    return cipher.encrypt(data.encode())

def decrypt(encrypted_data: bytes) -> str:
    """Decrypt an encrypted string."""
    return cipher.decrypt(encrypted_data).decode()

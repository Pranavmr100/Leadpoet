# utils/crypto.py
from cryptography.fernet import Fernet
from config import ENCRYPTION_KEY  # Import from root directory

cipher = Fernet(ENCRYPTION_KEY)

def encrypt_data(data):
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data):
    return cipher.decrypt(encrypted_data).decode()
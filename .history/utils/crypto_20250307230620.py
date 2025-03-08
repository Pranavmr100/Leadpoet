
from cryptography.fernet import Fernet
import config

cipher = Fernet(config.ENCRYPTION_KEY)

def encrypt_data(data):
    return cipher.encrypt(data.encode())  

def decrypt_data(encrypted_data):
    return cipher.decrypt(encrypted_data).decode()  
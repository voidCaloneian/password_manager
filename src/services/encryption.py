"""
Модуль для шифрования и дешифрования паролей
"""

from cryptography.fernet import Fernet
from src.config import ENCRYPTION_KEY

fernet = Fernet(ENCRYPTION_KEY)


def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()


def decrypt_password(encrypted: str) -> str:
    return fernet.decrypt(encrypted.encode()).decode()

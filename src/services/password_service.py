"""
Модуль извлечения и сохранения паролей в базе данных
"""

from sqlalchemy.orm import Session
from src.models import Password
from src.services.encryption import encrypt_password, decrypt_password


def get_password_entry(db: Session, service_name: str) -> Password:
    return db.query(Password).filter(Password.service_name == service_name).first()


def create_or_update_password(
    db: Session, service_name: str, password: str
) -> Password:
    encrypted = encrypt_password(password)
    entry = get_password_entry(db, service_name)
    if entry:
        entry.encrypted_password = encrypted
    else:
        entry = Password(service_name=service_name, encrypted_password=encrypted)
        db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def retrieve_password(db: Session, service_name: str) -> str:
    entry = get_password_entry(db, service_name)
    if not entry:
        return None
    return decrypt_password(entry.encrypted_password)

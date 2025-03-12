"""
Модель для хранения паролей
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Password(Base):
    """
    Модель Пароля
    """

    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, unique=True, index=True)
    encrypted_password = Column(String)

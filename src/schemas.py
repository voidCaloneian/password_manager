"""
Модуль для описания схем
"""

from pydantic import BaseModel


class PasswordCreate(BaseModel):
    """
    Схема создания пароля
    """

    password: str


class PasswordResponse(BaseModel):
    """
    Схема ответа с паролем
    """

    service_name: str
    password: str

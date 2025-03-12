"""
Модуль для работы с паролями
"""

from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from src.schemas import PasswordCreate, PasswordResponse
from src.db import SessionLocal
from src.models import Password
from src.services import password_service

router = APIRouter()


def get_db():
    """
    Получить сессию базы данных
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/password/{service_name}",
    response_model=PasswordResponse,
    summary="Создать или обновить пароль",
)
def create_or_update_password(
    service_name: str, payload: PasswordCreate, db: Session = Depends(get_db)
):
    entry = password_service.create_or_update_password(
        db, service_name, payload.password
    )
    return {"service_name": entry.service_name, "password": payload.password}


@router.get(
    "/password/{service_name}",
    response_model=PasswordResponse,
    summary="Получить пароль по имени сервиса",
)
def get_password(service_name: str, db: Session = Depends(get_db)):
    decrypted = password_service.retrieve_password(db, service_name)
    if decrypted is None:
        raise HTTPException(status_code=404, detail="Пароль не найден")
    return {"service_name": service_name, "password": decrypted}


@router.get("/password/", summary="Поиск паролей по части имени сервиса")
def search_password(
    service_name: str = Query(..., min_length=1), db: Session = Depends(get_db)
):
    entries = (
        db.query(Password)
        .filter(Password.service_name.ilike(f"%{service_name}%"))
        .all()
    )
    result = []
    for entry in entries:
        result.append(
            {
                "service_name": entry.service_name,
                "password": password_service.retrieve_password(db, entry.service_name),
            }
        )
    return result

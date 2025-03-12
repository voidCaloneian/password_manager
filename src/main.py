"""
Основной файл приложения
"""

from fastapi import FastAPI
from src.models import Base
from src.db import engine
from src.routes import password as password_routes

# Создаем таблицы, если они ещё не существуют
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Password Manager Service")

# Подключаем роуты
app.include_router(password_routes.router)

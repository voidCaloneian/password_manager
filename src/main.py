"""
Основной файл приложения
"""

from fastapi import FastAPI
from src.routes import password as password_routes


app = FastAPI(title="Password Manager Service")

# Подключаем роуты
app.include_router(password_routes.router)

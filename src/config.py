"""
Конфиг приложения
"""

import os

DATABASE_URL = os.getenv("DATABASE_URL")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

missing_vars = []
if not DATABASE_URL:
    missing_vars.append("DATABASE_URL")
if not ENCRYPTION_KEY:
    missing_vars.append("ENCRYPTION_KEY")

if missing_vars:
    raise ValueError("Переменные окружения не заданы: " + ", ".join(missing_vars))

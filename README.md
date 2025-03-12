# Описание проекта
**Менеджер паролей на FastAPI***

## Установка и запуск проекта
1. Клонирование репозитория:  
   ```bash
   git clone git@github.com:voidCaloneian/password_manager.git 
   cd password_manager
   ```
2. Запуск проекта, создание миграций и их применение
   ```bash
   docker compose build
   docker compose up -d
   docker compose exec web alembic revision --autogenerate -m "init"
   docker compose exec web alembic upgrade head
   ```
3. Опциональный запуск тестов
   ```docker compose exec web pytest```

> - Сервис будет доступен по адресу: ```http://localhost:8000```
> - API документация будет доступна по адресу: ```http://localhost:8000/docs```

## API

- **POST** ```/password/{service_name}``` – Создать или обновить пароль  
- **GET** ```/password/{service_name}``` – Получить пароль по имени сервиса  
- **GET** ```/password/?service_name=part``` – Поиск паролей по части имени сервиса

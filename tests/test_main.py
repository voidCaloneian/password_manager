"""
Тесты приложения
"""

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Base
from src.db import engine

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Очищаем и создаём таблицы для тестирования
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_password():
    service_name = "test_service"
    password = "secret123"
    response = client.post(f"/password/{service_name}", json={"password": password})
    assert response.status_code == 200
    data = response.json()
    assert data["service_name"] == service_name
    assert data["password"] == password


def test_get_password():
    service_name = "test_service"
    password = "secret123"
    response = client.get(f"/password/{service_name}")
    assert response.status_code == 200
    data = response.json()
    assert data["service_name"] == service_name
    assert data["password"] == password


def test_update_password():
    service_name = "test_service"
    new_password = "new_secret"
    response = client.post(f"/password/{service_name}", json={"password": new_password})
    assert response.status_code == 200
    data = response.json()
    assert data["password"] == new_password

    response = client.get(f"/password/{service_name}")
    data = response.json()
    assert data["password"] == new_password


def test_search_password():
    service_name = "another_service"
    password = "another_secret"
    client.post(f"/password/{service_name}", json={"password": password})

    response = client.get("/password/", params={"service_name": "test"})
    assert response.status_code == 200
    data = response.json()
    # Ожидается, что найдётся сервис "test_service"
    assert any(entry["service_name"] == "test_service" for entry in data)

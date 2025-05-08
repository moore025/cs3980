import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
log_dir = os.path.join(ROOT, "api", "logs")
os.makedirs(log_dir, exist_ok=True)

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import pytest
from httpx import AsyncClient, ASGITransport

from main import app
from db.db_context import init_database
from models.my_config import get_settings
from routers.user import HashPassword
from models.user import User

hash_password = HashPassword()


async def init_db():
    settings = get_settings()
    settings.connection_string = "mongodb://localhost:27017/test_db"
    settings.secret_key = "test_secret"
    await init_database()


@pytest.mark.anyio
async def test_sign_new_user() -> None:
    await init_db()
    await User.find_all().delete()

    payload = {
        "username": "python-web-dev@cs.uiowa.edu",
        "email": "python-web-dev@cs.uiowa.edu",
        "password": "test-password",
    }

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://app"
    ) as client:
        r = await client.post("/users/signup", json=payload)

    assert r.status_code == 200
    assert r.json() == {"message": "User created successfully"}


@pytest.mark.anyio
async def test_sign_user_in() -> None:
    await init_db()
    await User.find_all().delete()

    user = User(
        username="test-user@cs.uiowa.edu",
        email="test-user@cs.uiowa.edu",
        role="BasicUser",
        password=hash_password.create_hash("test-password"),
    )
    await user.create()

    form_data = {
        "username": "test-user@cs.uiowa.edu",
        "password": "test-password",
    }

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://app"
    ) as client:
        r = await client.post(
            "/users/sign-in",
            data=form_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

    assert r.status_code == 200
    body = r.json()
    assert body["token_type"] == "bearer"
    assert body["username"] == "test-user@cs.uiowa.edu"
    assert body["role"] == "BasicUser"
    assert "access_token" in body

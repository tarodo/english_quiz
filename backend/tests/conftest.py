from typing import Dict, Generator

import pytest
from app.core.config import settings
from app.db import session
from fastapi.testclient import TestClient
from main import app
from sqlmodel import Session
from tests.utils.users import (get_authentication_token_from_email,
                               get_bot_father_token_headers,
                               get_superuser_token_headers)


@pytest.fixture(scope="session")
def db() -> Generator:
    yield session


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return get_authentication_token_from_email(
        client=client, email=settings.EMAIL_TEST_USER, db=db
    )


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> Dict[str, str]:
    return get_superuser_token_headers(client)


@pytest.fixture(scope="module")
def bot_father_token_headers(client: TestClient) -> Dict[str, str]:
    return get_bot_father_token_headers(client)

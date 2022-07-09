from app.crud import tags
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models import TagIn
from tests.utils.utils import random_lower_string


def test_create_tag_by_admin(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    tag_in = TagIn(name=random_lower_string(10))
    data = tag_in.dict()
    r = client.post(f"/tags/", headers=superuser_token_headers, json=data)
    assert 200 <= r.status_code < 300
    created_tag = r.json()
    tag = tags.read_by_name(db, tag_name=tag_in.name)
    assert tag
    assert tag.name == created_tag["name"]


def test_create_tag_by_user(
    client: TestClient, user_token_headers: dict[str, str], db: Session
) -> None:
    tag_in = TagIn(name=random_lower_string(10))
    data = tag_in.dict()
    r = client.post(f"/tags/", headers=user_token_headers, json=data)
    assert 200 <= r.status_code < 300
    created_tag = r.json()
    tag = tags.read_by_name(db, tag_name=tag_in.name)
    assert tag
    assert tag.name == created_tag["name"]

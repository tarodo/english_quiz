import pytest

from app.api.tags import TagErrors
from app.crud import tags
from app.models import Student, TagIn
from fastapi.testclient import TestClient
from sqlmodel import Session
from tests.utils.students import create_random_student
from tests.utils.utils import random_lower_string


@pytest.fixture(scope="module")
def tags_student(db: Session) -> Student:
    student = create_random_student(db)
    return student


def test_create_tag_by_admin(
    client: TestClient,
    superuser_token_headers: dict[str, str],
    db: Session,
    tags_student: Student,
) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tags_student.id)
    data = tag_in.dict()
    r = client.post(f"/tags/", headers=superuser_token_headers, json=data)
    assert 200 <= r.status_code < 300
    created_tag = r.json()
    tag = tags.read_by_name_and_id(db, tag_name=tag_in.name, student_id=tag_in.student_id)
    assert tag
    assert tag.name == created_tag["name"]


def test_create_tag_by_user(
    client: TestClient,
    user_token_headers: dict[str, str],
    db: Session,
    tags_student: Student,
) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tags_student.id)
    data = tag_in.dict()
    r = client.post(f"/tags/", headers=user_token_headers, json=data)
    assert 200 <= r.status_code < 300
    created_tag = r.json()
    tag = tags.read_by_name_and_id(db, tag_name=tag_in.name, student_id=tag_in.student_id)
    assert tag
    assert tag.name == created_tag["name"]


def test_create_tag_same(
    client: TestClient,
    user_token_headers: dict[str, str],
    db: Session,
    tags_student: Student,
) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tags_student.id)
    tag = tags.create(db, payload=tag_in)
    data = tag_in.dict()
    r = client.post(f"/tags/", headers=user_token_headers, json=data)
    assert r.status_code == 400
    created_tag = r.json()
    assert created_tag["detail"]["err"] == str(TagErrors.TagExists)


def test_read_tag_by_admin(
    client: TestClient,
    superuser_token_headers: dict[str, str],
    db: Session,
    tags_student: Student,
) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tags_student.id)
    tag = tags.create(db, payload=tag_in)
    r = client.get(f"/tags/{tag.id}", headers=superuser_token_headers)
    assert r.status_code == 200
    retrieved_tag = r.json()
    assert tag.id == retrieved_tag["id"]
    assert tag.name == retrieved_tag["name"]
    assert tag.student_id == retrieved_tag["student_id"]


def test_read_tag_user(
    client: TestClient,
    user_token_headers: dict[str, str],
    db: Session,
    tags_student: Student,
) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tags_student.id)
    tag = tags.create(db, payload=tag_in)
    r = client.get(f"/tags/{tag.id}", headers=user_token_headers)
    assert r.status_code == 400
    created_tag = r.json()
    assert created_tag["detail"]["err"] == str(TagErrors.UserIsNotAdmin)

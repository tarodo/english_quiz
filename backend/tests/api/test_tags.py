import pytest

from app.crud import tags, students
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models import TagIn, Student
from tests.utils.students import get_student_in
from tests.utils.utils import random_lower_string


@pytest.fixture(scope="module")
def tags_student(db: Session) -> Student:
    student_in = get_student_in()
    student = students.create(db, payload=student_in)
    return student


def test_create_tag_by_admin(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session,
    tags_student: Student
) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tags_student.id)
    data = tag_in.dict()
    r = client.post(f"/tags/", headers=superuser_token_headers, json=data)
    assert 200 <= r.status_code < 300
    created_tag = r.json()
    tag = tags.read_by_name(db, tag_name=tag_in.name)
    assert tag
    assert tag.name == created_tag["name"]


def test_create_tag_by_user(
    client: TestClient, user_token_headers: dict[str, str], db: Session,
    tags_student: Student
) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tags_student.id)
    data = tag_in.dict()
    r = client.post(f"/tags/", headers=user_token_headers, json=data)
    assert 200 <= r.status_code < 300
    created_tag = r.json()
    tag = tags.read_by_name(db, tag_name=tag_in.name)
    assert tag
    assert tag.name == created_tag["name"]

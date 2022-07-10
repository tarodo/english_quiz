import pytest
from app.crud import tags, students
from app.models import TagIn, Student
from pydantic.error_wrappers import ValidationError
from sqlmodel import Session

from tests.utils.students import get_student_in
from tests.utils.utils import random_lower_string


@pytest.fixture(scope="module")
def tag_student(db: Session) -> Student:
    student_in = get_student_in()
    student = students.create(db, payload=student_in)
    return student


def test_tag_create(db: Session, tag_student: Student) -> None:
    tag_in = TagIn(name=random_lower_string(10), student_id=tag_student.id)
    tag = tags.create(db, payload=tag_in)
    assert tag_in.name == tag.name


def test_tag_create_empty(db: Session, tag_student: Student) -> None:
    name = ""
    min_length = TagIn.schema()["properties"]["name"]["minLength"]
    with pytest.raises(
        ValidationError, match=f"value has at least {min_length} characters"
    ):
        tag_in = TagIn(name=name, student_id=tag_student.id)


def test_tag_create_long(db: Session, tag_student: Student) -> None:
    name = random_lower_string(300)
    max_length = TagIn.schema()["properties"]["name"]["maxLength"]
    with pytest.raises(
        ValidationError, match=f"value has at most {max_length} characters"
    ):
        tag_in = TagIn(name=name, student_id=tag_student.id)

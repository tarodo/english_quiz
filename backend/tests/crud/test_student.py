import pytest
from fastapi.encoders import jsonable_encoder
from pydantic.error_wrappers import ValidationError
from sqlmodel import Session

from app.crud import students
from app.models import StudentIn
from tests.utils.utils import random_lower_string, random_tg


def get_student_in() -> StudentIn:
    tg_id = random_tg()
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_lower_string()
    return StudentIn(
        tg_id=tg_id, first_name=first_name, last_name=last_name, username=username
    )


def test_student_create(db: Session) -> None:
    student_in = get_student_in()
    student = students.create(db, payload=student_in)
    assert student.tg_id == student_in.tg_id
    assert student.is_active


def test_student_create_with_empty_tg(db: Session) -> None:
    tg_id = ""
    min_length = StudentIn.schema()["properties"]["tg_id"]["minLength"]
    with pytest.raises(
        ValidationError, match=f"value has at least {min_length} characters"
    ):
        student_in = StudentIn(tg_id=tg_id)


def test_student_read_by_id(db: Session) -> None:
    student_in = get_student_in()
    student = students.create(db, student_in)
    student_test = students.read_by_id(db, student.id)
    assert student_test
    assert jsonable_encoder(student) == jsonable_encoder(student_test)


def test_student_read_by_tg_id(db: Session) -> None:
    student_in = get_student_in()
    student = students.create(db, student_in)
    student_test = students.read_by_tg_id(db, student.tg_id)
    assert student_test
    assert jsonable_encoder(student) == jsonable_encoder(student_test)

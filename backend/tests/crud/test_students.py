import pytest
from app.crud import students
from app.models import StudentIn, StudentUpdate
from fastapi.encoders import jsonable_encoder
from pydantic.error_wrappers import ValidationError
from sqlmodel import Session
from tests.utils.students import get_student_in, create_random_student
from tests.utils.users import create_random_user


def test_student_create(db: Session) -> None:
    user = create_random_user(db)
    student_in = get_student_in(user.id)
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
    student = create_random_student(db)
    student_test = students.read_by_id(db, student.id)
    assert student_test
    assert jsonable_encoder(student) == jsonable_encoder(student_test)


def test_student_read_by_tg_id(db: Session) -> None:
    student = create_random_student(db)
    student_test = students.read_by_tg_id(db, student.tg_id)
    assert student_test
    assert jsonable_encoder(student) == jsonable_encoder(student_test)


def test_student_update(db: Session) -> None:
    student = create_random_student(db)
    new_user = create_random_user(db)
    student_in_update = get_student_in(new_user.id)
    student_in_update = StudentUpdate(**student_in_update.dict())
    student_in_update.is_active = False
    student_update = students.update(db, student, student_in_update)
    assert student_update
    assert student_update.id == student.id
    assert student_update.tg_id == student.tg_id
    assert student_update.first_name == student.first_name
    assert student_update.last_name == student.last_name
    assert student_update.username == student.username


def test_student_remove(db: Session) -> None:
    student = create_random_student(db)
    student_remove = students.remove(db, student)
    student_test = students.read_by_id(db, student.id)
    assert not student_test
    assert student_remove == student

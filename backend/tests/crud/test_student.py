from sqlmodel import Session

from app.crud import students
from app.models import StudentIn
from tests.utils.utils import random_lower_string, random_tg


def test_student_create(db: Session) -> None:
    tg_id = random_tg()
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_lower_string()
    student_in = StudentIn(tg_id=tg_id, first_name=first_name, last_name=last_name, username=username)
    student = students.create(db, payload=student_in)
    assert student.tg_id == tg_id
    assert student.is_active


def test_student_create_with_empty_tg(db: Session) -> None:
    tg_id = ""
    student_in = StudentIn(tg_id=tg_id)
    student = students.create(db, payload=student_in)
    assert not student

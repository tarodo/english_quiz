from app.crud import students
from app.models import Student, StudentIn
from sqlmodel import Session
from tests.utils.users import create_random_user
from tests.utils.utils import random_lower_string, random_tg


def create_random_student(db: Session) -> Student:
    user = create_random_user(db)
    student_in = get_student_in(user.id)
    student = students.create(db, student_in)
    return student


def get_student_in(user_id: int) -> StudentIn:
    tg_id = random_tg()
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_lower_string()
    return StudentIn(
        tg_id=tg_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
        user_id=user_id,
    )

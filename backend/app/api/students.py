from enum import Enum

from app.api import deps
from app.api.tools import raise_400
from app.crud import students
from app.models import Student, StudentIn, StudentOut, User, responses
from fastapi import APIRouter, Depends
from sqlmodel import Session

router = APIRouter()


class StudentErrors(Enum):
    NoRightsForUser = "User doesn't have rights"
    StudentExists = "Student with tg_id exists"


@router.post("/", response_model=StudentOut, status_code=200, responses=responses)
def create_student(
    payload: StudentIn,
    current_user: User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Student:
    """Create one student"""
    if not current_user.is_admin:
        if current_user.id != payload.user_id:
            raise_400(StudentErrors.NoRightsForUser)

    old_student = students.read_by_tg_id(db, payload.tg_id)
    if old_student:
        raise_400(StudentErrors.StudentExists)

    old_student = students.read_by_user_id(db, payload.user_id)
    if old_student:
        raise_400(StudentErrors.StudentExists)

    student = students.create(db, payload)
    return student


@router.get(
    "/{student_id}", response_model=StudentOut, status_code=200, responses=responses
)
def read_student(
    student_id: int,
    current_user: User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Student | None:
    """Retrieve a student"""
    return None

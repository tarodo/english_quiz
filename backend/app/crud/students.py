from sqlmodel import Session

from app.models import Student, StudentIn


def create(db: Session, payload: StudentIn) -> Student:
    """Create a student"""
    student = Student(**payload.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def read_by_id(db: Session, student_id: int) -> Student | None:
    pass


def read_by_tg_id(db: Session, tg_id: int) -> Student | None:
    pass
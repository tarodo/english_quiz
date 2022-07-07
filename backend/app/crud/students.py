from sqlmodel import Session

from app.models import Student, StudentIn


def create(db: Session, payload: StudentIn) -> Student:
    """Create a student"""
    student = Student(**payload.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

from sqlmodel import Session, select

from app.models import StudentIn, Student


def create(db: Session, payload: StudentIn) -> Student:
    """Create a student"""
    student = Student(**payload.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

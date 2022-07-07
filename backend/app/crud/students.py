from sqlmodel import Session, select

from app.models import StudentIn, Student


def create(db: Session, payload: StudentIn) -> Student:
    pass

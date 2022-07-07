from sqlmodel import Session, select

from app.models import Student, StudentIn


def create(db: Session, payload: StudentIn) -> Student:
    """Create a student"""
    student = Student(**payload.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def read_by_id(db: Session, student_id: int) -> Student | None:
    """Read one student by id"""
    student = select(Student).where(Student.id == student_id)
    student = db.exec(student).one_or_none()
    return student


def read_by_tg_id(db: Session, tg_id: int) -> Student | None:
    """Read one student by tg_id"""
    student = select(Student).where(Student.tg_id == tg_id)
    student = db.exec(student).one_or_none()
    return student

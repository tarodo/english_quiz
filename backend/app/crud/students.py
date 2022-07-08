from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select

from app.models import Student, StudentIn, StudentUpdate


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


def update(db: Session, db_obj: Student, payload: StudentUpdate) -> Student:
    """Update student's data"""
    obj_data = jsonable_encoder(db_obj)
    update_data = payload.dict(exclude_unset=True, exclude_none=True)
    for field in obj_data:
        if field in update_data:
            new_data = update_data[field]
            setattr(db_obj, field, new_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def remove(db: Session, db_obj: Student) -> Student:
    """Remove student from DB"""
    db.delete(db_obj)
    db.commit()
    return db_obj

from app.models import Tag, TagIn
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select


def create(db: Session, payload: TagIn) -> Tag:
    """Create a tag"""
    tag = Tag(**payload.dict())
    try:
        db.add(tag)
        db.commit()
        db.refresh(tag)
        return tag
    except IntegrityError:
        db.rollback()


def read_by_id(db: Session, tag_id: int) -> Tag | None:
    """Read one tag by id"""
    tag = select(Tag).where(Tag.id == tag_id)
    tag = db.exec(tag).one_or_none()
    return tag


def read_by_name_and_id(db: Session, tag_name: str, student_id: int) -> Tag | None:
    """Read one tag by name and student_id"""
    tag = select(Tag).where(Tag.name == tag_name, Tag.student_id == student_id)
    tag = db.exec(tag).one_or_none()
    return tag

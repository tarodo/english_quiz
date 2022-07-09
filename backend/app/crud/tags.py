from app.models import Tag, TagIn
from sqlmodel import Session, select


def create(db: Session, payload: TagIn) -> Tag:
    """Create a tag"""
    tag = Tag(**payload.dict())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


def read_by_id(db: Session, tag_id: int) -> Tag | None:
    """Read one tag by id"""
    tag = select(Tag).where(Tag.id == tag_id)
    tag = db.exec(tag).one_or_none()
    return tag


def read_by_name(db: Session, tag_name: str) -> Tag | None:
    """Read one student by tg_id"""
    tag = select(Tag).where(Tag.name == tag_name)
    tag = db.exec(tag).one_or_none()
    return tag

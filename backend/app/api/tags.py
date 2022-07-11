from enum import Enum

from app.api import deps
from app.api.tools import raise_400
from app.crud import tags
from app.models import Tag, TagIn, TagOut, User, responses
from fastapi import APIRouter, Depends
from sqlmodel import Session

router = APIRouter()


class TagErrors(Enum):
    TagExists = "Tag exists"
    UserIsNotAdmin = "User is not an admin"


@router.post("/", response_model=TagOut, status_code=200, responses=responses)
def create_tag(
    payload: TagIn,
    current_user: User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Tag:
    """Create one tag"""
    old_tag = tags.read_by_name_and_id(db, payload.name, student_id=payload.student_id)
    if old_tag:
        raise_400(TagErrors.TagExists)

    tag = tags.create(db, payload)
    return tag


@router.get("/{tag_id}", response_model=TagOut, status_code=200, responses=responses)
def read_tags(
    tag_id: int,
    current_user: User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Tag | None:
    """Retrieve a tag"""
    if not current_user.is_admin:
        raise_400(TagErrors.UserIsNotAdmin)

    tag = tags.read_by_id(db, tag_id)
    return tag

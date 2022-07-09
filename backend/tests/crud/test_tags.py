import pytest
from app.crud import tags
from app.models import TagIn
from pydantic.error_wrappers import ValidationError
from sqlmodel import Session
from tests.utils.utils import random_lower_string


def test_tag_create(db: Session) -> None:
    tag_in = TagIn(name=random_lower_string(10))
    tag = tags.create(db, payload=tag_in)
    assert tag_in.name == tag.name


def test_tag_create_empty(db: Session) -> None:
    name = ""
    min_length = TagIn.schema()["properties"]["name"]["minLength"]
    with pytest.raises(
        ValidationError, match=f"value has at least {min_length} characters"
    ):
        tag_in = TagIn(name=name)


def test_tag_create_long(db: Session) -> None:
    name = random_lower_string(300)
    max_length = TagIn.schema()["properties"]["name"]["maxLength"]
    with pytest.raises(
        ValidationError, match=f"value has at most {max_length} characters"
    ):
        tag_in = TagIn(name=name)

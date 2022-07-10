from pydantic import constr
from sqlmodel import Field, SQLModel, Relationship

from app.models import Student


class TagBase(SQLModel):
    name: constr(min_length=1, max_length=200) = Field(
        index=True, nullable=False
    )
    student_id: int = Field(foreign_key="student.id")


class Tag(TagBase, table=True):
    id: int = Field(primary_key=True)

    student: Student = Relationship(back_populates="tags")


class TagIn(TagBase):
    pass


class TagOut(TagBase):
    id: int = Field(...)


class TagUpdate(TagBase):
    pass
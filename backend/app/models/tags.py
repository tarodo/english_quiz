from pydantic import constr
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel


class TagBase(SQLModel):
    __table_args__ = (UniqueConstraint("name", "student_id"),)
    name: constr(min_length=1, max_length=200) = Field(index=True, nullable=False)
    student_id: int = Field(foreign_key="student.id")


class Tag(TagBase, table=True):
    id: int = Field(primary_key=True)

    student: "Student" = Relationship(back_populates="tags")


class TagIn(TagBase):
    pass


class TagOut(TagBase):
    id: int = Field(...)


class TagUpdate(TagBase):
    pass

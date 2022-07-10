from pydantic import constr
from sqlmodel import Field, SQLModel, Relationship

from app import models


class StudentBase(SQLModel):
    tg_id: constr(min_length=1) = Field(
        index=True, nullable=False, sa_column_kwargs={"unique": True}
    )
    is_active: bool = True
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None


class Student(StudentBase, table=True):
    id: int = Field(primary_key=True)

    tags: list["models.tags.Tag"] | None = Relationship(back_populates="student")


class StudentIn(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int = Field(...)


class StudentUpdate(SQLModel):
    is_active: bool | None = None
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None

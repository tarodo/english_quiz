from pydantic import constr
from sqlmodel import Field, Relationship, SQLModel

from app.models.users import User


class StudentBase(SQLModel):
    tg_id: constr(min_length=1) = Field(
        index=True,
    )
    is_active: bool = True
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    user_id: int = Field(foreign_key="user.id")


class Student(StudentBase, table=True):
    id: int = Field(primary_key=True)
    user: User = Relationship(back_populates="student")

    tags: list["Tag"] | None = Relationship(back_populates="student")


class StudentIn(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int = Field(...)


class StudentUpdate(SQLModel):
    is_active: bool | None = None
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    user_id: int | None = None

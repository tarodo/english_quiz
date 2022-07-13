from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


class UserBase(SQLModel):
    email: EmailStr = Field(index=True, sa_column_kwargs={"unique": True})
    is_admin: bool = Field(default=False, nullable=False)
    is_bot: bool = Field(default=False, nullable=False)


class User(UserBase, table=True):
    id: int = Field(primary_key=True)
    password: str = Field(...)

    student: "Student" = Relationship(
        back_populates="user", sa_relationship_kwargs={"uselist": False}
    )


class UserIn(UserBase):
    password: str = Field(...)


class UserOut(UserBase):
    id: int = Field(...)


class UserUpdate(SQLModel):
    email: EmailStr | None = None
    is_admin: bool | None = None
    password: str | None = None

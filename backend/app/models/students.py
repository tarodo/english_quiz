from sqlmodel import Field, SQLModel


class StudentBase(SQLModel):
    tg_id: str = Field(index=True, nullable=False, sa_column_kwargs={"unique": True})
    is_active: bool = Field(default=True, nullable=False)
    first_name: str = Field(nullable=True, default=None)
    last_name: str = Field(nullable=True, default=None)
    username: str = Field(nullable=True, default=None)


class Student(StudentBase, table=True):
    id: int = Field(primary_key=True)


class StudentIn(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int = Field(...)


class StudentUpdate(SQLModel):
    is_active: bool | None = None
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
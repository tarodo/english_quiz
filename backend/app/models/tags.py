from pydantic import constr
from sqlmodel import Field, SQLModel


class TagBase(SQLModel):
    name: constr(min_length=1, max_length=200) = Field(
        index=True, nullable=False
    )


class Tag(TagBase, table=True):
    id: int = Field(primary_key=True)


class TagIn(TagBase):
    pass


class TagOut(TagBase):
    id: int = Field(...)


class TagUpdate(TagBase):
    pass
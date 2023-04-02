from pydantic import BaseModel


class Book(BaseModel):
    title: str
    rating:int
    author_: int

    class Config:
        orm_mode = True


class Author(BaseModel):
    name:str
    age:int

    class Config:
        orm_mode = True

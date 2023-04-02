from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    password: str 
    

class ReturnUser(BaseModel):
    name: str
    email: str
    is_admin: bool
    is_superuser: bool


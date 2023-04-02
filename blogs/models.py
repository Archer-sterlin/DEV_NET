from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # author  = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'Users'
    id: int= Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    email: str = Column(String)
    is_active:bool = Column(Boolean)
    is_admin:bool= Column(Boolean)
    password:str = Column(String)
    # blogs = relationship("Blog", back_populates="author")




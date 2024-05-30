from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

    tasks = relationship('Task', back_populates='user')

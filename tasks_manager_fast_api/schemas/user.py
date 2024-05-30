from pydantic import BaseModel, EmailStr
from typing import List, Any


#from schemas import Task

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    tasks: List[Any] = []

    class Config:
        orm_mode = True


User.update_forward_refs()
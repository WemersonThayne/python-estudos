from datetime import datetime, date

from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    date_start: date
    date_end: date
    status: str

class Task(TaskBase):
    id: int
    user_id: int
    date_start: date
    date_end: date
    status: str
    created_at: datetime
    updated_at: datetime


    class Config:
        orm_mode = True

from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate

def get_task(db: Session, post_id: int):
    return db.query(Task).filter(Task.id == post_id).first()

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

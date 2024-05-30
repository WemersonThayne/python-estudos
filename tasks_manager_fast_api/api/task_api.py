from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.crud_task as crud_task
import schemas
from api.deps import get_db

router = APIRouter()

@router.post("/users/{user_id}/tasks/", response_model=schemas.Task, status_code=201)
def create_task_for_user(user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = crud_task.create_task(db=db, task=task, user_id=user_id)
    if not task:
        raise HTTPException(status_code=400, detail=task)
    return task

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud_task.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

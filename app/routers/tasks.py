from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas import TaskCreate, TaskUpdate
from ..crud import create_task, get_task, update_task, delete_task
from ..auth import get_current_active_user
from ..models import Task, User

router = APIRouter()

@router.post("/", response_model=Task)
def create_new_task(task: TaskCreate, current_user: User = Depends(get_current_active_user)):
    return create_task(task)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: str, current_user: User = Depends(get_current_active_user)):
    db_task = get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=Task)
def update_existing_task(task_id: str, task: TaskUpdate, current_user: User = Depends(get_current_active_user)):
    db_task = get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(task_id, task)

@router.delete("/{task_id}", response_model=dict)
def delete_existing_task(task_id: str, current_user: User = Depends(get_current_active_user)):
    db_task = get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(task_id)
    return {"message": "Task deleted successfully"}

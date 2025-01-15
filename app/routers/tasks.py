"""Tasks

Raises:
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""

from fastapi import APIRouter, Depends, HTTPException
from ..schemas import TaskCreate, TaskUpdate
from ..crud import create_task, get_task, update_task, delete_task,get_project,get_project_tasks,get_task_tasks
from ..auth import get_current_active_user
from ..models import Task, User

router = APIRouter()


@router.post("/", response_model=Task)
def create_new_task(
    task: TaskCreate, current_user: User = Depends(get_current_active_user)
):
    """create_new_task

    Args:
        task (TaskCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    # Prefix the project ID with the user ID
    task.task_id = f"{current_user['user_id']}_{task.task_id}"
    db_task = get_task(task.task_id)
    if db_task:
        raise HTTPException(status_code=400, detail="Task already exists")
    return create_task(task)

@router.get("/all/{project_id}", response_model=list)
def get_all_task(project_id: str, 
                 current_user: User = Depends(get_current_active_user)
                 ):
    db_project = get_project_tasks(project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_project
@router.get("/in/{task_id}", response_model=list)
def get_all_task(task_id: str, 
                 current_user: User = Depends(get_current_active_user)
                 ):
    db_tasks = get_task_tasks(task_id)
    if db_tasks is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_tasks

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: str, current_user: User = Depends(get_current_active_user)):
    """read_task

    Args:
        task_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_task = get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put("/{task_id}", response_model=Task)
def update_existing_task(
    task_id: str,
    task: TaskUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """Update specific task fields

    Args:
        task_id (str): Task identifier
        task (TaskUpdate): Fields to update
        current_user (User): Current authenticated user

    Raises:
        HTTPException: 404 if task not found

    Returns:
        Task: Updated task
    """
    db_task = get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(task_id, task)


@router.delete("/{task_id}", response_model=dict)
def delete_existing_task(
    task_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_task

    Args:
        task_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_task = get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(task_id)
    return {"message": "Task deleted successfully"}

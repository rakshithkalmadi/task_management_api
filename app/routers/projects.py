"""Projects

Raises:
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""

from fastapi import APIRouter, Depends, HTTPException
from ..schemas import ProjectCreate, ProjectTasks, ProjectUpdate
from ..crud import create_project, get_project,get_projects_by_user, update_project, delete_project, project_tasks
from ..auth import get_current_active_user
from ..models import Project, User
from ..crud import update_user_projects

router = APIRouter()


@router.post("/", response_model=Project)
def create_new_project(
    project: ProjectCreate, current_user: User = Depends(get_current_active_user)
):
    db_project = get_project(project.project_id)
    if db_project:
        raise HTTPException(status_code=400, detail="Project already exists")
    
    # Add current user to access as admin
    current_user_data = User(**current_user)
    if project.access is None:
        project.access = {}
    project.access["admin"] = current_user_data.user_id
    
    if current_user_data.projects is None:
        current_user_data.projects = []
    current_user_data.projects.append(project.project_id)
    update_user_projects(current_user_data.user_id, current_user_data.projects)
    return create_project(project)

@router.get("/", response_model=list)
def get_user_projects(current_user: User = Depends(get_current_active_user)):
    print(current_user["user_id"])
    db_projects = get_projects_by_user(current_user["user_id"])
    if db_projects is None:
        raise HTTPException(status_code=404, detail="Project not found")    
    return db_projects


@router.get("/{project_id}", response_model=Project)
def read_project(
    project_id: str, current_user: User = Depends(get_current_active_user)
):
    """read_project

    Args:
        project_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_project = get_project(project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.put("/{project_id}", response_model=Project)
def update_existing_project(
    project_id: str,
    project: ProjectUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """update_existing_project

    Args:
        project_id (str): _description_
        project (ProjectUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_project = get_project(project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return update_project(project_id, project)

@router.put("/{project_id}/tasks", response_model=Project)
def add_project_tasks(
    project_id: str,
    tasks: ProjectTasks,
    current_user: User = Depends(get_current_active_user),
):
    """Add tasks to an existing project

    Args:
        project_id (str): The ID of the project
        tasks (ProjectTasks): The tasks to add
        current_user (User, optional): The current active user. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: If the project is not found

    Returns:
        Project: The updated project
    """
    db_project = get_project(project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project_tasks(project_id,tasks)

@router.delete("/{project_id}", response_model=dict)
def delete_existing_project(
    project_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_project

    Args:
        project_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_project = get_project(project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    delete_project(project_id)
    return {"message": "Project deleted successfully"}

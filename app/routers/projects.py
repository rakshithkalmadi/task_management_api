"""Projects

Raises:
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""

from fastapi import APIRouter, Depends, HTTPException
from ..schemas import ProjectCreate, ProjectUpdate
from ..crud import create_project, get_project, update_project, delete_project
from ..auth import get_current_active_user
from ..models import Project, User

router = APIRouter()


@router.post("/", response_model=Project)
def create_new_project(
    project: ProjectCreate, current_user: User = Depends(get_current_active_user)
):
    return create_project(project)


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

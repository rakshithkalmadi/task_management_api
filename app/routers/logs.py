"""Logs

Raises:
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
    """

from fastapi import APIRouter, Depends, HTTPException

from ..auth import get_current_active_user
from ..crud import create_log, delete_log, get_log, update_log
from ..models import Log, User
from ..schemas import LogCreate, LogUpdate

router = APIRouter()


@router.post("/", response_model=Log)
def create_new_log(
    log: LogCreate, current_user: User = Depends(get_current_active_user)
):
    """create_new_log

    Args:
        log (LogCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    return create_log(log)


@router.get("/{log_id}", response_model=Log)
def read_log(log_id: str, current_user: User = Depends(get_current_active_user)):
    """read_log

    Args:
        log_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_log = get_log(log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log


@router.put("/{log_id}", response_model=Log)
def update_existing_log(
    log_id: str, log: LogUpdate, current_user: User = Depends(get_current_active_user)
):
    """update_existing_log

    Args:
        log_id (str): _description_
        log (LogUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_log = get_log(log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return update_log(log_id, log)


@router.delete("/{log_id}", response_model=dict)
def delete_existing_log(
    log_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_log

    Args:
        log_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_log = get_log(log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    delete_log(log_id)
    return {"message": "Log deleted successfully"}

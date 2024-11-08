from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas import LogCreate, LogUpdate
from ..crud import create_log, get_log, update_log, delete_log
from ..auth import get_current_active_user
from ..models import Log, User

router = APIRouter()


@router.post("/", response_model=Log)
def create_new_log(
    log: LogCreate, current_user: User = Depends(get_current_active_user)
):
    return create_log(log)


@router.get("/{log_id}", response_model=Log)
def read_log(log_id: str, current_user: User = Depends(get_current_active_user)):
    db_log = get_log(log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log


@router.put("/{log_id}", response_model=Log)
def update_existing_log(
    log_id: str, log: LogUpdate, current_user: User = Depends(get_current_active_user)
):
    db_log = get_log(log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return update_log(log_id, log)


@router.delete("/{log_id}", response_model=dict)
def delete_existing_log(
    log_id: str, current_user: User = Depends(get_current_active_user)
):
    db_log = get_log(log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    delete_log(log_id)
    return {"message": "Log deleted successfully"}

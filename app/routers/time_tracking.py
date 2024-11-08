"""Time Tracking

Raises:
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""

from fastapi import APIRouter, Depends, HTTPException
from ..schemas import TimeEntryCreate, TimeEntryUpdate
from ..crud import (
    create_time_entry,
    get_time_entry,
    update_time_entry,
    delete_time_entry,
)
from ..auth import get_current_active_user
from ..models import TimeEntry, User

router = APIRouter()


@router.post("/", response_model=TimeEntry)
def create_new_time_entry(
    time_entry: TimeEntryCreate, current_user: User = Depends(get_current_active_user)
):
    """create_new_time_entry

    Args:
        time_entry (TimeEntryCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    return create_time_entry(time_entry)


@router.get("/{time_entry_id}", response_model=TimeEntry)
def read_time_entry(
    time_entry_id: str, current_user: User = Depends(get_current_active_user)
):
    """read_time_entry

    Args:
        time_entry_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_time_entry = get_time_entry(time_entry_id)
    if db_time_entry is None:
        raise HTTPException(status_code=404, detail="Time entry not found")
    return db_time_entry


@router.put("/{time_entry_id}", response_model=TimeEntry)
def update_existing_time_entry(
    time_entry_id: str,
    time_entry: TimeEntryUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """update_existing_time_entry

    Args:
        time_entry_id (str): _description_
        time_entry (TimeEntryUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_time_entry = get_time_entry(time_entry_id)
    if db_time_entry is None:
        raise HTTPException(status_code=404, detail="Time entry not found")
    return update_time_entry(time_entry_id, time_entry)


@router.delete("/{time_entry_id}", response_model=dict)
def delete_existing_time_entry(
    time_entry_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_time_entry

    Args:
        time_entry_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_time_entry = get_time_entry(time_entry_id)
    if db_time_entry is None:
        raise HTTPException(status_code=404, detail="Time entry not found")
    delete_time_entry(time_entry_id)
    return {"message": "Time entry deleted successfully"}

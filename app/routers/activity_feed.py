from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas import ActivityCreate, ActivityUpdate
from ..crud import create_activity, get_activity, update_activity, delete_activity
from ..auth import get_current_active_user
from ..models import Activity, User

router = APIRouter()


@router.post("/", response_model=Activity)
def create_new_activity(
    activity: ActivityCreate, current_user: User = Depends(get_current_active_user)
):
    return create_activity(activity)


@router.get("/{activity_id}", response_model=Activity)
def read_activity(
    activity_id: str, current_user: User = Depends(get_current_active_user)
):
    db_activity = get_activity(activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity


@router.put("/{activity_id}", response_model=Activity)
def update_existing_activity(
    activity_id: str,
    activity: ActivityUpdate,
    current_user: User = Depends(get_current_active_user),
):
    db_activity = get_activity(activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return update_activity(activity_id, activity)


@router.delete("/{activity_id}", response_model=dict)
def delete_existing_activity(
    activity_id: str, current_user: User = Depends(get_current_active_user)
):
    db_activity = get_activity(activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    delete_activity(activity_id)
    return {"message": "Activity deleted successfully"}

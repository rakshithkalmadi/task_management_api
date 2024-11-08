from fastapi import APIRouter, Depends, HTTPException
from ..schemas import ActivityCreate, ActivityUpdate
from ..crud import create_activity, get_activity, update_activity, delete_activity
from ..auth import get_current_active_user
from ..models import Activity, User

router = APIRouter()


@router.post("/", response_model=Activity)
def create_new_activity(
    activity: ActivityCreate, current_user: User = Depends(get_current_active_user)
):
    """create_new_activity

    Args:
        activity (ActivityCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    return create_activity(activity)


@router.get("/{activity_id}", response_model=Activity)
def read_activity(
    activity_id: str, current_user: User = Depends(get_current_active_user)
):
    """read_activity

    Args:
        activity_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
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
    """update_existing_activity

    Args:
        activity_id (str): _description_
        activity (ActivityUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_activity = get_activity(activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return update_activity(activity_id, activity)


@router.delete("/{activity_id}", response_model=dict)
def delete_existing_activity(
    activity_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_activity

    Args:
        activity_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_activity = get_activity(activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    delete_activity(activity_id)
    return {"message": "Activity deleted successfully"}

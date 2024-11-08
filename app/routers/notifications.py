from fastapi import APIRouter, Depends, HTTPException
from ..schemas import NotificationCreate, NotificationUpdate
from ..crud import (
    create_notification,
    get_notification,
    update_notification,
    delete_notification,
)
from ..auth import get_current_active_user
from ..models import Notification, User

router = APIRouter()


@router.post("/", response_model=Notification)
def create_new_notification(
    notification: NotificationCreate,
    current_user: User = Depends(get_current_active_user),
):
    """create_new_notification

    Args:
        notification (NotificationCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    return create_notification(notification)


@router.get("/{notification_id}", response_model=Notification)
def read_notification(
    notification_id: str, current_user: User = Depends(get_current_active_user)
):
    """read_notification

    Args:
        notification_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_notification = get_notification(notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification


@router.put("/{notification_id}", response_model=Notification)
def update_existing_notification(
    notification_id: str,
    notification: NotificationUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """update_existing_notification

    Args:
        notification_id (str): _description_
        notification (NotificationUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_notification = get_notification(notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return update_notification(notification_id, notification)


@router.delete("/{notification_id}", response_model=dict)
def delete_existing_notification(
    notification_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_notification

    Args:
        notification_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_notification = get_notification(notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    delete_notification(notification_id)
    return {"message": "Notification deleted successfully"}

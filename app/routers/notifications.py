from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas import NotificationCreate, NotificationUpdate
from ..crud import create_notification, get_notification, update_notification, delete_notification
from ..auth import get_current_active_user
from ..models import Notification, User

router = APIRouter()

@router.post("/", response_model=Notification)
def create_new_notification(notification: NotificationCreate, current_user: User = Depends(get_current_active_user)):
    return create_notification(notification)

@router.get("/{notification_id}", response_model=Notification)
def read_notification(notification_id: str, current_user: User = Depends(get_current_active_user)):
    db_notification = get_notification(notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification

@router.put("/{notification_id}", response_model=Notification)
def update_existing_notification(notification_id: str, notification: NotificationUpdate, current_user: User = Depends(get_current_active_user)):
    db_notification = get_notification(notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return update_notification(notification_id, notification)

@router.delete("/{notification_id}", response_model=dict)
def delete_existing_notification(notification_id: str, current_user: User = Depends(get_current_active_user)):
    db_notification = get_notification(notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    delete_notification(notification_id)
    return {"message": "Notification deleted successfully"}

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas import AttachmentCreate, AttachmentUpdate
from ..crud import create_attachment, get_attachment, update_attachment, delete_attachment
from ..auth import get_current_active_user
from ..models import Attachment, User

router = APIRouter()

@router.post("/", response_model=Attachment)
def create_new_attachment(attachment: AttachmentCreate, current_user: User = Depends(get_current_active_user)):
    return create_attachment(attachment)

@router.get("/{attachment_id}", response_model=Attachment)
def read_attachment(attachment_id: str, current_user: User = Depends(get_current_active_user)):
    db_attachment = get_attachment(attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return db_attachment

@router.put("/{attachment_id}", response_model=Attachment)
def update_existing_attachment(attachment_id: str, attachment: AttachmentUpdate, current_user: User = Depends(get_current_active_user)):
    db_attachment = get_attachment(attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return update_attachment(attachment_id, attachment)

@router.delete("/{attachment_id}", response_model=dict)
def delete_existing_attachment(attachment_id: str, current_user: User = Depends(get_current_active_user)):
    db_attachment = get_attachment(attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    delete_attachment(attachment_id)
    return {"message": "Attachment deleted successfully"}

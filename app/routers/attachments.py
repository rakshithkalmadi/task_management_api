from fastapi import APIRouter, Depends, HTTPException
from ..schemas import AttachmentCreate, AttachmentUpdate
from ..crud import (
    create_attachment,
    get_attachment,
    update_attachment,
    delete_attachment,
)
from ..auth import get_current_active_user
from ..models import Attachment, User

router = APIRouter()


@router.post("/", response_model=Attachment)
def create_new_attachment(
    attachment: AttachmentCreate, current_user: User = Depends(get_current_active_user)
):
    """create_new_attachment

    Args:
        attachment (AttachmentCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    return create_attachment(attachment)


@router.get("/{attachment_id}", response_model=Attachment)
def read_attachment(
    attachment_id: str, current_user: User = Depends(get_current_active_user)
):
    """read_attachment

    Args:
        attachment_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_attachment = get_attachment(attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return db_attachment


@router.put("/{attachment_id}", response_model=Attachment)
def update_existing_attachment(
    attachment_id: str,
    attachment: AttachmentUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """update_existing_attachment

    Args:
        attachment_id (str): _description_
        attachment (AttachmentUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_attachment = get_attachment(attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return update_attachment(attachment_id, attachment)


@router.delete("/{attachment_id}", response_model=dict)
def delete_existing_attachment(
    attachment_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_attachment

    Args:
        attachment_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_attachment = get_attachment(attachment_id)
    if db_attachment is None:
        raise HTTPException(status_code=404, detail="Attachment not found")
    delete_attachment(attachment_id)
    return {"message": "Attachment deleted successfully"}

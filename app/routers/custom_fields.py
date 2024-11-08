from fastapi import APIRouter, Depends, HTTPException
from ..schemas import CustomFieldCreate, CustomFieldUpdate
from ..crud import (
    create_custom_field,
    get_custom_field,
    update_custom_field,
    delete_custom_field,
)
from ..auth import get_current_active_user
from ..models import CustomField, User

router = APIRouter()


@router.post("/", response_model=CustomField)
def create_new_custom_field(
    custom_field: CustomFieldCreate,
    current_user: User = Depends(get_current_active_user),
):
    """create_new_custom_field

    Args:
        custom_field (CustomFieldCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    return create_custom_field(custom_field)


@router.get("/{field_id}", response_model=CustomField)
def read_custom_field(
    field_id: str, current_user: User = Depends(get_current_active_user)
):
    """read_custom_field

    Args:
        field_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_custom_field = get_custom_field(field_id)
    if db_custom_field is None:
        raise HTTPException(status_code=404, detail="Custom field not found")
    return db_custom_field


@router.put("/{field_id}", response_model=CustomField)
def update_existing_custom_field(
    field_id: str,
    custom_field: CustomFieldUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """update_existing_custom_field

    Args:
        field_id (str): _description_
        custom_field (CustomFieldUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_custom_field = get_custom_field(field_id)
    if db_custom_field is None:
        raise HTTPException(status_code=404, detail="Custom field not found")
    return update_custom_field(field_id, custom_field)


@router.delete("/{field_id}", response_model=dict)
def delete_existing_custom_field(
    field_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_custom_field

    Args:
        field_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_custom_field = get_custom_field(field_id)
    if db_custom_field is None:
        raise HTTPException(status_code=404, detail="Custom field not found")
    delete_custom_field(field_id)
    return {"message": "Custom field deleted successfully"}

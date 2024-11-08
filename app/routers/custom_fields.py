from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
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
    return create_custom_field(custom_field)


@router.get("/{field_id}", response_model=CustomField)
def read_custom_field(
    field_id: str, current_user: User = Depends(get_current_active_user)
):
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
    db_custom_field = get_custom_field(field_id)
    if db_custom_field is None:
        raise HTTPException(status_code=404, detail="Custom field not found")
    return update_custom_field(field_id, custom_field)


@router.delete("/{field_id}", response_model=dict)
def delete_existing_custom_field(
    field_id: str, current_user: User = Depends(get_current_active_user)
):
    db_custom_field = get_custom_field(field_id)
    if db_custom_field is None:
        raise HTTPException(status_code=404, detail="Custom field not found")
    delete_custom_field(field_id)
    return {"message": "Custom field deleted successfully"}

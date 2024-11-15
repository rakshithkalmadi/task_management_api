"""Users

Raises:
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""

from fastapi import APIRouter, Depends, HTTPException
from ..schemas import UserCreate, UserUpdate
from ..crud import create_user, get_user, update_user, delete_user
from ..auth import get_current_active_user
from ..models import User
from ..utils import get_user_by_email

router = APIRouter()


@router.post("/", response_model=UserCreate)
def create_new_user(user: UserCreate):
    """create_new_user

    Args:
        user (UserCreate): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_user = get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = get_user(user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User id already exists")
    return create_user(user)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: str, current_user: User = Depends(get_current_active_user)):
    """read_user

    Args:
        user_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_user = get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=User)
def update_existing_user(
    user_id: str,
    user: UserUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """update_existing_user

    Args:
        user_id (str): _description_
        user (UserUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_user = get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(user_id, user)


@router.delete("/{user_id}", response_model=dict)
def delete_existing_user(
    user_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_user

    Args:
        user_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_user = get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(user_id)
    return {"message": "User deleted successfully"}

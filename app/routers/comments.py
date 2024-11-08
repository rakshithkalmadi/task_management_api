from fastapi import APIRouter, Depends, HTTPException
from ..schemas import CommentCreate, CommentUpdate
from ..crud import create_comment, get_comment, update_comment, delete_comment
from ..auth import get_current_active_user
from ..models import Comment, User

router = APIRouter()


@router.post("/", response_model=Comment)
def create_new_comment(
    comment: CommentCreate, current_user: User = Depends(get_current_active_user)
):
    """create_new_comment

    Args:
        comment (CommentCreate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    return create_comment(comment)


@router.get("/{comment_id}", response_model=Comment)
def read_comment(
    comment_id: str, current_user: User = Depends(get_current_active_user)
):
    """read_comment

    Args:
        comment_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_comment = get_comment(comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment


@router.put("/{comment_id}", response_model=Comment)
def update_existing_comment(
    comment_id: str,
    comment: CommentUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """update_existing_comment

    Args:
        comment_id (str): _description_
        comment (CommentUpdate): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_comment = get_comment(comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return update_comment(comment_id, comment)


@router.delete("/{comment_id}", response_model=dict)
def delete_existing_comment(
    comment_id: str, current_user: User = Depends(get_current_active_user)
):
    """delete_existing_comment

    Args:
        comment_id (str): _description_
        current_user (User, optional): _description_. Defaults to Depends(get_current_active_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    db_comment = get_comment(comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    delete_comment(comment_id)
    return {"message": "Comment deleted successfully"}

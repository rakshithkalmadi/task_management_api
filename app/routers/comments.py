from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas import CommentCreate, CommentUpdate
from ..crud import create_comment, get_comment, update_comment, delete_comment
from ..auth import get_current_active_user
from ..models import Comment, User

router = APIRouter()


@router.post("/", response_model=Comment)
def create_new_comment(
    comment: CommentCreate, current_user: User = Depends(get_current_active_user)
):
    return create_comment(comment)


@router.get("/{comment_id}", response_model=Comment)
def read_comment(
    comment_id: str, current_user: User = Depends(get_current_active_user)
):
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
    db_comment = get_comment(comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return update_comment(comment_id, comment)


@router.delete("/{comment_id}", response_model=dict)
def delete_existing_comment(
    comment_id: str, current_user: User = Depends(get_current_active_user)
):
    db_comment = get_comment(comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    delete_comment(comment_id)
    return {"message": "Comment deleted successfully"}

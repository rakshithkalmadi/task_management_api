"""
Schemas for Application
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Token(BaseModel):
    """Token

    Args:
        BaseModel (_type_): _description_
    """

    access_token: str
    token_type: str


class UserCreate(BaseModel):
    """UserCreate

    Args:
        BaseModel (_type_): _description_
    """

    user_id: str
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    """UserUpdate

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    profile_picture: Optional[str] = None


class ProjectCreate(BaseModel):
    """ProjectCreate

    Args:
        BaseModel (_type_): _description_
    """

    project_id: str
    name: str
    description: str
    start_date: datetime
    due_date: datetime
    access: dict
    priority: str
    status: str
    tags: List[str]
    tasks: List[str]
    created_at: datetime
    updated_at: datetime


class ProjectUpdate(BaseModel):
    """ProjectUpdate

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    access: Optional[dict] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[List[str]] = None
    budget: Optional[float] = None
    actual_cost: Optional[float] = None
    milestones: Optional[List[str]] = None


class TaskCreate(BaseModel):
    """TaskCreate

    Args:
        BaseModel (_type_): _description_
    """

    task_id: str
    title: str
    description: str
    status: str
    priority: str
    due_date: datetime
    parent_id: Optional[str] = None
    sub_tasks: List[str]
    created_at: datetime
    updated_at: datetime


class TaskUpdate(BaseModel):
    """TaskUpdate

    Args:
        BaseModel (_type_): _description_
    """

    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    parent_id: Optional[str] = None
    sub_tasks: Optional[List[str]] = None
    estimated_time: Optional[int] = None
    actual_time: Optional[int] = None
    dependencies: Optional[List[str]] = None


class LogCreate(BaseModel):
    """LogCreate

    Args:
        BaseModel (_type_): _description_
    """

    operation: str
    description: str
    user_id: str


class LogUpdate(BaseModel):
    """LogUpdate

    Args:
        BaseModel (_type_): _description_
    """

    operation: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[str] = None


class NotificationCreate(BaseModel):
    """NotificationCreate

    Args:
        BaseModel (_type_): _description_
    """

    user_id: str
    message: str


class NotificationUpdate(BaseModel):
    """NotificationUpdate

    Args:
        BaseModel (_type_): _description_
    """

    user_id: Optional[str] = None
    message: Optional[str] = None


class CommentCreate(BaseModel):
    """CommentCreate

    Args:
        BaseModel (_type_): _description_
    """

    task_id: str
    user_id: str
    content: str


class CommentUpdate(BaseModel):
    """CommentUpdate

    Args:
        BaseModel (_type_): _description_
    """

    task_id: Optional[str] = None
    user_id: Optional[str] = None
    content: Optional[str] = None


class AttachmentCreate(BaseModel):
    """AttachmentCreate

    Args:
        BaseModel (_type_): _description_
    """

    task_id: str
    file_url: str
    uploaded_by: str


class AttachmentUpdate(BaseModel):
    """AttachmentUpdate

    Args:
        BaseModel (_type_): _description_
    """

    task_id: Optional[str] = None
    file_url: Optional[str] = None
    uploaded_by: Optional[str] = None


class ActivityCreate(BaseModel):
    """ActivityCreate

    Args:
        BaseModel (_type_): _description_
    """

    user_id: str
    action: str
    entity_id: str
    entity_type: str


class ActivityUpdate(BaseModel):
    """ActivityUpdate

    Args:
        BaseModel (_type_): _description_
    """

    user_id: Optional[str] = None
    action: Optional[str] = None
    entity_id: Optional[str] = None
    entity_type: Optional[str] = None


class TimeEntryCreate(BaseModel):
    """TimeEntryCreate

    Args:
        BaseModel (_type_): _description_
    """

    task_id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    duration: int


class TimeEntryUpdate(BaseModel):
    """TimeEntryUpdate

    Args:
        BaseModel (_type_): _description_
    """

    task_id: Optional[str] = None
    user_id: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration: Optional[int] = None


class CustomFieldCreate(BaseModel):
    """CustomFieldCreate

    Args:
        BaseModel (_type_): _description_
    """

    entity_type: str
    entity_id: str
    field_name: str
    field_value: str


class CustomFieldUpdate(BaseModel):
    """CustomFieldUpdate

    Args:
        BaseModel (_type_): _description_
    """

    entity_type: Optional[str] = None
    entity_id: Optional[str] = None
    field_name: Optional[str] = None
    field_value: Optional[str] = None

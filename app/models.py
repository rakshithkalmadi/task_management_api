"""
Models for the Application

"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    """User Model

    Args:
        BaseModel : _description_
    """

    user_id: str
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
    profile_picture: Optional[str] = None
    last_login: Optional[datetime] = None
    projects: Optional[List[str]] = None


class Project(BaseModel):
    """Project Model

    Args:
        BaseModel
    """

    project_id: str
    name: str
    description: str
    start_date: datetime
    due_date: datetime
    access: dict
    priority: str
    status: str
    created_at: datetime
    updated_at: datetime
    tags: List[str]
    tasks: List[str]
    milestones: Optional[List[str]] = None


class Task(BaseModel):
    """Task Model

    Args:
        BaseModel (_type_): _description_
    """

    task_id: str
    title: str
    description: str
    status: str
    priority: str
    due_date: datetime
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str] = None
    sub_tasks: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    estimated_time: Optional[int] = None
    actual_time: Optional[int] = None
    dependencies: Optional[List[str]] = None


class Log(BaseModel):
    """Log Model

    Args:
        BaseModel (_type_): _description_
    """

    log_id: str
    operation: str
    description: str
    user_id: str
    timestamp: datetime


class Notification(BaseModel):
    """Notification Mode
    l

    Args:
        BaseModel (_type_): _description_
    """

    notification_id: str
    user_id: str
    message: str
    read_status: bool
    created_at: datetime


class Comment(BaseModel):
    """Comment Model

    Args:
        BaseModel (_type_): _description_
    """

    comment_id: str
    task_id: str
    user_id: str
    content: str
    created_at: datetime


class Attachment(BaseModel):
    """Attachment Model

    Args:
        BaseModel (_type_): _description_
    """

    attachment_id: str
    task_id: str
    file_url: str
    uploaded_by: str
    uploaded_at: datetime


class Activity(BaseModel):
    """Activity Model

    Args:
        BaseModel (_type_): _description_
    """

    activity_id: str
    user_id: str
    action: str
    entity_id: str
    entity_type: str
    timestamp: datetime


class TimeEntry(BaseModel):
    """TimeEntry Model

    Args:
        BaseModel (_type_): _description_
    """

    time_entry_id: str
    task_id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    duration: int


class CustomField(BaseModel):
    """CustomField Model

    Args:
        BaseModel (_type_): _description_
    """

    field_id: str
    entity_type: str
    entity_id: str
    field_name: str
    field_value: str

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    user_id: str
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
    profile_picture: Optional[str] = None
    last_login: Optional[datetime] = None

class Project(BaseModel):
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
    budget: Optional[float] = None
    actual_cost: Optional[float] = None
    milestones: Optional[List[str]] = None

class Task(BaseModel):
    task_id: str
    title: str
    description: str
    status: str
    priority: str
    due_date: datetime
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str] = None
    sub_tasks: List[str]
    estimated_time: Optional[int] = None
    actual_time: Optional[int] = None
    dependencies: Optional[List[str]] = None

class Log(BaseModel):
    log_id: str
    operation: str
    description: str
    user_id: str
    timestamp: datetime

class Notification(BaseModel):
    notification_id: str
    user_id: str
    message: str
    read_status: bool
    created_at: datetime

class Comment(BaseModel):
    comment_id: str
    task_id: str
    user_id: str
    content: str
    created_at: datetime

class Attachment(BaseModel):
    attachment_id: str
    task_id: str
    file_url: str
    uploaded_by: str
    uploaded_at: datetime

class Activity(BaseModel):
    activity_id: str
    user_id: str
    action: str
    entity_id: str
    entity_type: str
    timestamp: datetime

class TimeEntry(BaseModel):
    time_entry_id: str
    task_id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    duration: int

class CustomField(BaseModel):
    field_id: str
    entity_type: str
    entity_id: str
    field_name: str
    field_value: str

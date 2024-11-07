from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    user_id: str
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    profile_picture: Optional[str] = None

class ProjectCreate(BaseModel):
    name: str
    description: str
    start_date: datetime
    due_date: datetime
    access: dict
    priority: str
    status: str
    tags: List[str]

class ProjectUpdate(BaseModel):
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
    title: str
    description: str
    status: str
    priority: str
    due_date: datetime
    parent_id: Optional[str] = None
    sub_tasks: List[str]

class TaskUpdate(BaseModel):
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
    operation: str
    description: str
    user_id: str
    
class LogUpdate(BaseModel):
    operation: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[str] = None

class NotificationCreate(BaseModel):
    user_id: str
    message: str

class NotificationUpdate(BaseModel):
    user_id: Optional[str] = None
    message: Optional[str] = None

class CommentCreate(BaseModel):
    task_id: str
    user_id: str
    content: str

class CommentUpdate(BaseModel):
    task_id: Optional[str] = None
    user_id: Optional[str] = None
    content: Optional[str] = None


class AttachmentCreate(BaseModel):
    task_id: str
    file_url: str
    uploaded_by: str

class AttachmentUpdate(BaseModel):
    task_id: Optional[str] = None
    file_url: Optional[str] = None
    uploaded_by: Optional[str] = None

class ActivityCreate(BaseModel):
    user_id: str
    action: str
    entity_id: str
    entity_type: str

class ActivityUpdate(BaseModel):
    user_id: Optional[str] = None
    action: Optional[str] = None
    entity_id: Optional[str] = None
    entity_type: Optional[str] = None

class TimeEntryCreate(BaseModel):
    task_id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    duration: int

class TimeEntryUpdate(BaseModel):
    task_id: Optional[str] = None
    user_id: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration: Optional[int] = None


class CustomFieldCreate(BaseModel):
    entity_type: str
    entity_id: str
    field_name: str
    field_value: str

class CustomFieldUpdate(BaseModel):
    entity_type: Optional[str] = None
    entity_id: Optional[str] = None
    field_name: Optional[str] = None
    field_value: Optional[str] = None


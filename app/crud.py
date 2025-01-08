"""CRUD Operations

"""

import datetime

from fastapi import HTTPException
from pymongo import MongoClient
from typing import List, Optional
from constants import MONGO_URI

from .schemas import (
    ActivityCreate,
    AttachmentCreate,
    CommentCreate,
    CustomFieldCreate,
    LogCreate,
    NotificationCreate,
    ProjectCreate,
    ProjectTasks,
    TaskCreate,
    TimeEntryCreate,
    UserCreate,
    UserUpdate,
)
from .utils import get_password_hash  # Updated import

client = MongoClient(MONGO_URI)
db = client.task_management


def create_user(user: UserCreate):
    """create_user

    Args:
        user (UserCreate): _description_

    Returns:
        _type_: _description_
    """
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user_dict["password"])
    user_dict["created_at"] = datetime.datetime.now()
    user_dict["updated_at"] = datetime.datetime.now()
    db.users.insert_one(user_dict)
    return user_dict


def get_user(user_id: str):
    """get_user

    Args:
        user_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.users.find_one({"user_id": user_id})


def update_user(user_id: str, user: UserUpdate):
    """update_user

    Args:
        user_id (str): _description_
        user (UserCreate): _description_

    Returns:
        _type_: _description_
    """
    db.users.update_one({"user_id": user_id}, {"$set": user.dict()})
    return db.users.find_one({"user_id": user_id})

def update_user_projects(user_id: str, projects: List[str]):
    db.users.update_one(
        {"user_id": user_id}, {"$set": {"projects": projects}}
    )


def delete_user(user_id: str):
    """delete_user

    Args:
        user_id (str): _description_
    """
    db.users.delete_one({"user_id": user_id})


def create_project(project: ProjectCreate):
    """create_project

    Args:
        project (ProjectCreate): _description_

    Returns:
        _type_: _description_
    """
    project_dict = project.dict()
    db.projects.insert_one(project_dict)
    return project_dict


def get_project(project_id: str):
    """get_project

    Args:
        project_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.projects.find_one({"project_id": project_id},{"_id": 0})

def get_projects_by_user(user_id: str):
    """get_projects_by_user

    Args:
        user_id (str): The ID of the user

    Returns:
        List[Project]: A list of projects associated with the user
    """
    return list(db.projects.find({"access.admin": user_id},{"_id": 0}))


def update_project(project_id: str, project: ProjectCreate):
    """update_project

    Args:
        project_id (str): _description_
        project (ProjectCreate): _description_

    Returns:
        _type_: _description_
    """
    db.projects.update_one({"project_id": project_id}, {"$set": project.dict()})
    return db.projects.find_one({"project_id": project_id})

def project_tasks(project_id: str, tasks: ProjectTasks):
    """Add tasks to project

    Args:
        project_id (str): The ID of the project
        tasks (ProjectTasks): The tasks to add

    Returns:
        dict: The updated project
    """
    # Retrieve the existing project
    db_project = db.projects.find_one({"project_id": project_id})
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Get the existing tasks
    existing_tasks = db_project.get("tasks", [])
    
    # Find new tasks that are not already in the existing tasks
    new_tasks = [task for task in tasks.tasks if task not in existing_tasks]
    
    # Update the project with the new tasks
    if new_tasks:
        db.projects.update_one(
            {"project_id": project_id}, 
            {"$push": {"tasks": {"$each": new_tasks}}}
        )
    
    # Return the updated project
    return db.projects.find_one({"project_id": project_id})

def get_project_tasks(project_id: str):
    """Fetch all tasks under a project

    Args:
        project_id (str): The ID of the project

    Returns:
        list: The list of tasks under the project with details
    """
    # Retrieve the existing project
    db_project = db.projects.find_one({"project_id": project_id})
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Get the existing tasks
    task_ids = db_project.get("tasks", [])
    
    if not task_ids:
        return []

    # Fetch details for all tasks in bulk
    tasks_with_details = list(db.tasks.find({"task_id": {"$in": task_ids}},{"_id": 0}))
    
    # Return the list of tasks with details
    return tasks_with_details



def delete_project(project_id: str):
    """delete_project

    Args:
        project_id (str): _description_
    """
    db.projects.delete_one({"project_id": project_id})


def create_task(task: TaskCreate):
    """create_task

    Args:
        task (TaskCreate): _description_

    Returns:
        _type_: _description_
    """
    task_dict = task.dict()
    db.tasks.insert_one(task_dict)
    return task_dict


def get_task(task_id: str):
    """get_task

    Args:
        task_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.tasks.find_one({"task_id": task_id})


def update_task(task_id: str, task: TaskCreate):
    """update_task

    Args:
        task_id (str): _description_
        task (TaskCreate): _description_

    Returns:
        _type_: _description_
    """
    db.tasks.update_one({"task_id": task_id}, {"$set": task.dict()})
    return db.tasks.find_one({"task_id": task_id})


def delete_task(task_id: str):
    """delete_task

    Args:
        task_id (str): _description_
    """
    db.tasks.delete_one({"task_id": task_id})


def create_log(log: LogCreate):
    """create_log

    Args:
        log (LogCreate): _description_

    Returns:
        _type_: _description_
    """
    log_dict = log.dict()
    db.logs.insert_one(log_dict)
    return log_dict


def get_log(log_id: str):
    """get_log

    Args:
        log_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.logs.find_one({"log_id": log_id})


def update_log(log_id: str, log: LogCreate):
    """update_log

    Args:
        log_id (str): _description_
        log (LogCreate): _description_

    Returns:
        _type_: _description_
    """
    db.logs.update_one({"log_id": log_id}, {"$set": log.dict()})
    return db.logs.find_one({"log_id": log_id})


def delete_log(log_id: str):
    """delete_log

    Args:
        log_id (str): _description_
    """
    db.logs.delete_one({"log_id": log_id})


def create_notification(notification: NotificationCreate):
    """create_notification

    Args:
        notification (NotificationCreate): _description_

    Returns:
        _type_: _description_
    """
    notification_dict = notification.dict()
    db.notifications.insert_one(notification_dict)
    return notification_dict


def get_notification(notification_id: str):
    """get_notification

    Args:
        notification_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.notifications.find_one({"notification_id": notification_id})


def update_notification(notification_id: str, notification: NotificationCreate):
    """update_notification

    Args:
        notification_id (str): _description_
        notification (NotificationCreate): _description_

    Returns:
        _type_: _description_
    """
    db.notifications.update_one(
        {"notification_id": notification_id}, {"$set": notification.dict()}
    )
    return db.notifications.find_one({"notification_id": notification_id})


def delete_notification(notification_id: str):
    """delete_notification

    Args:
        notification_id (str): _description_
    """
    db.notifications.delete_one({"notification_id": notification_id})


def create_comment(comment: CommentCreate):
    """create_comment

    Args:
        comment (CommentCreate): _description_

    Returns:
        _type_: _description_
    """
    comment_dict = comment.dict()
    db.comments.insert_one(comment_dict)
    return comment_dict


def get_comment(comment_id: str):
    """get_comment

    Args:
        comment_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.comments.find_one({"comment_id": comment_id})


def update_comment(comment_id: str, comment: CommentCreate):
    """update_comment

    Args:
        comment_id (str): _description_
        comment (CommentCreate): _description_

    Returns:
        _type_: _description_
    """
    db.comments.update_one({"comment_id": comment_id}, {"$set": comment.dict()})
    return db.comments.find_one({"comment_id": comment_id})


def delete_comment(comment_id: str):
    """delete_comment

    Args:
        comment_id (str): _description_
    """
    db.comments.delete_one({"comment_id": comment_id})


def create_attachment(attachment: AttachmentCreate):
    """create_attachment

    Args:
        attachment (AttachmentCreate): _description_

    Returns:
        _type_: _description_
    """
    attachment_dict = attachment.dict()
    db.attachments.insert_one(attachment_dict)
    return attachment_dict


def get_attachment(attachment_id: str):
    """get_attachment

    Args:
        attachment_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.attachments.find_one({"attachment_id": attachment_id})


def update_attachment(attachment_id: str, attachment: AttachmentCreate):
    """update_attachment

    Args:
        attachment_id (str): _description_
        attachment (AttachmentCreate): _description_

    Returns:
        _type_: _description_
    """
    db.attachments.update_one(
        {"attachment_id": attachment_id}, {"$set": attachment.dict()}
    )
    return db.attachments.find_one({"attachment_id": attachment_id})


def delete_attachment(attachment_id: str):
    """delete_attachment

    Args:
        attachment_id (str): _description_
    """
    db.attachments.delete_one({"attachment_id": attachment_id})


def create_activity(activity: ActivityCreate):
    """create_activity

    Args:
        activity (ActivityCreate): _description_

    Returns:
        _type_: _description_
    """
    activity_dict = activity.dict()
    db.activities.insert_one(activity_dict)
    return activity_dict


def get_activity(activity_id: str):
    """get_activity

    Args:
        activity_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.activities.find_one({"activity_id": activity_id})


def update_activity(activity_id: str, activity: ActivityCreate):
    """update_activity

    Args:
        activity_id (str): _description_
        activity (ActivityCreate): _description_

    Returns:
        _type_: _description_
    """
    db.activities.update_one({"activity_id": activity_id}, {"$set": activity.dict()})
    return db.activities.find_one({"activity_id": activity_id})


def delete_activity(activity_id: str):
    """delete_activity

    Args:
        activity_id (str): _description_
    """
    db.activities.delete_one({"activity_id": activity_id})


def create_time_entry(time_entry: TimeEntryCreate):
    """create_time_entry

    Args:
        time_entry (TimeEntryCreate): _description_

    Returns:
        _type_: _description_
    """
    time_entry_dict = time_entry.dict()
    db.time_entries.insert_one(time_entry_dict)
    return time_entry_dict


def get_time_entry(time_entry_id: str):
    """get_time_entry

    Args:
        time_entry_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.time_entries.find_one({"time_entry_id": time_entry_id})


def update_time_entry(time_entry_id: str, time_entry: TimeEntryCreate):
    """update_time_entry

    Args:
        time_entry_id (str): _description_
        time_entry (TimeEntryCreate): _description_

    Returns:
        _type_: _description_
    """
    db.time_entries.update_one(
        {"time_entry_id": time_entry_id}, {"$set": time_entry.dict()}
    )
    return db.time_entries.find_one({"time_entry_id": time_entry_id})


def delete_time_entry(time_entry_id: str):
    """delete_time_entry

    Args:
        time_entry_id (str): _description_
    """
    db.time_entries.delete_one({"time_entry_id": time_entry_id})


def create_custom_field(custom_field: CustomFieldCreate):
    """create_custom_field

    Args:
        custom_field (CustomFieldCreate): _description_

    Returns:
        _type_: _description_
    """
    custom_field_dict = custom_field.dict()
    db.custom_fields.insert_one(custom_field_dict)
    return custom_field_dict


def get_custom_field(field_id: str):
    """get_custom_field

    Args:
        field_id (str): _description_

    Returns:
        _type_: _description_
    """
    return db.custom_fields.find_one({"field_id": field_id})


def update_custom_field(field_id: str, custom_field: CustomFieldCreate):
    """update_custom_field

    Args:
        field_id (str): _description_
        custom_field (CustomFieldCreate): _description_

    Returns:
        _type_: _description_
    """
    db.custom_fields.update_one({"field_id": field_id}, {"$set": custom_field.dict()})
    return db.custom_fields.find_one({"field_id": field_id})


def delete_custom_field(field_id: str):
    """delete_custom_field

    Args:
        field_id (str): _description_
    """
    db.custom_fields.delete_one({"field_id": field_id})

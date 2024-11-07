from bson import ObjectId
from pymongo import MongoClient
from .models import User, Project, Task, Log, Notification, Comment, Attachment, Activity, TimeEntry, CustomField
from .schemas import UserCreate, ProjectCreate, TaskCreate, LogCreate, NotificationCreate, CommentCreate, AttachmentCreate, ActivityCreate, TimeEntryCreate, CustomFieldCreate
from .utils import get_password_hash  # Updated import
from constants import MONGO_URI
import datetime
client = MongoClient(MONGO_URI)
db = client.task_management

def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user_dict["password"])
    user_dict["created_at"] = datetime.datetime.now()
    user_dict["updated_at"] = datetime.datetime.now()
    db.users.insert_one(user_dict)
    return user_dict

# Other CRUD functions remain unchanged


def get_user(user_id: str):
    return db.users.find_one({"user_id": user_id})

def update_user(user_id: str, user: UserCreate):
    db.users.update_one({"user_id": user_id}, {"$set": user.dict()})
    return db.users.find_one({"user_id": user_id})

def delete_user(user_id: str):
    db.users.delete_one({"user_id": user_id})

def create_project(project: ProjectCreate):
    project_dict = project.dict()
    db.projects.insert_one(project_dict)
    return project_dict

def get_project(project_id: str):
    return db.projects.find_one({"project_id": project_id})

def update_project(project_id: str, project: ProjectCreate):
    db.projects.update_one({"project_id": project_id}, {"$set": project.dict()})
    return db.projects.find_one({"project_id": project_id})

def delete_project(project_id: str):
    db.projects.delete_one({"project_id": project_id})

def create_task(task: TaskCreate):
    task_dict = task.dict()
    db.tasks.insert_one(task_dict)
    return task_dict

def get_task(task_id: str):
    return db.tasks.find_one({"task_id": task_id})

def update_task(task_id: str, task: TaskCreate):
    db.tasks.update_one({"task_id": task_id}, {"$set": task.dict()})
    return db.tasks.find_one({"task_id": task_id})

def delete_task(task_id: str):
    db.tasks.delete_one({"task_id": task_id})

def create_log(log: LogCreate):
    log_dict = log.dict()
    db.logs.insert_one(log_dict)
    return log_dict

def get_log(log_id: str):
    return db.logs.find_one({"log_id": log_id})

def update_log(log_id: str, log: LogCreate):
    db.logs.update_one({"log_id": log_id}, {"$set": log.dict()})
    return db.logs.find_one({"log_id": log_id})

def delete_log(log_id: str):
    db.logs.delete_one({"log_id": log_id})

def create_notification(notification: NotificationCreate):
    notification_dict = notification.dict()
    db.notifications.insert_one(notification_dict)
    return notification_dict

def get_notification(notification_id: str):
    return db.notifications.find_one({"notification_id": notification_id})

def update_notification(notification_id: str, notification: NotificationCreate):
    db.notifications.update_one({"notification_id": notification_id}, {"$set": notification.dict()})
    return db.notifications.find_one({"notification_id": notification_id})

def delete_notification(notification_id: str):
    db.notifications.delete_one({"notification_id": notification_id})

def create_comment(comment: CommentCreate):
    comment_dict = comment.dict()
    db.comments.insert_one(comment_dict)
    return comment_dict

def get_comment(comment_id: str):
    return db.comments.find_one({"comment_id": comment_id})

def update_comment(comment_id: str, comment: CommentCreate):
    db.comments.update_one({"comment_id": comment_id}, {"$set": comment.dict()})
    return db.comments.find_one({"comment_id": comment_id})

def delete_comment(comment_id: str):
    db.comments.delete_one({"comment_id": comment_id})

def create_attachment(attachment: AttachmentCreate):
    attachment_dict = attachment.dict()
    db.attachments.insert_one(attachment_dict)
    return attachment_dict

def get_attachment(attachment_id: str):
    return db.attachments.find_one({"attachment_id": attachment_id})

def update_attachment(attachment_id: str, attachment: AttachmentCreate):
    db.attachments.update_one({"attachment_id": attachment_id}, {"$set": attachment.dict()})
    return db.attachments.find_one({"attachment_id": attachment_id})

def delete_attachment(attachment_id: str):
    db.attachments.delete_one({"attachment_id": attachment_id})

def create_activity(activity: ActivityCreate):
    activity_dict = activity.dict()
    db.activities.insert_one(activity_dict)
    return activity_dict

def get_activity(activity_id: str):
    return db.activities.find_one({"activity_id": activity_id})

def update_activity(activity_id: str, activity: ActivityCreate):
    db.activities.update_one({"activity_id": activity_id}, {"$set": activity.dict()})
    return db.activities.find_one({"activity_id": activity_id})

def delete_activity(activity_id: str):
    db.activities.delete_one({"activity_id": activity_id})

def create_time_entry(time_entry: TimeEntryCreate):
    time_entry_dict = time_entry.dict()
    db.time_entries.insert_one(time_entry_dict)
    return time_entry_dict

def get_time_entry(time_entry_id: str):
    return db.time_entries.find_one({"time_entry_id": time_entry_id})

def update_time_entry(time_entry_id: str, time_entry: TimeEntryCreate):
    db.time_entries.update_one({"time_entry_id": time_entry_id}, {"$set": time_entry.dict()})
    return db.time_entries.find_one({"time_entry_id": time_entry_id})

def delete_time_entry(time_entry_id: str):
    db.time_entries.delete_one({"time_entry_id": time_entry_id})

def create_custom_field(custom_field: CustomFieldCreate):
    custom_field_dict = custom_field.dict()
    db.custom_fields.insert_one(custom_field_dict)
    return custom_field_dict

def get_custom_field(field_id: str):
    return db.custom_fields.find_one({"field_id": field_id})

def update_custom_field(field_id: str, custom_field: CustomFieldCreate):
    db.custom_fields.update_one({"field_id": field_id}, {"$set": custom_field.dict()})
    return db.custom_fields.find_one({"field_id": field_id})

def delete_custom_field(field_id: str):
    db.custom_fields.delete_one({"field_id": field_id})

"""

Main Router

"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth import router as auth_router

from .routers import (
    activity_feed,
    attachments,
    comments,
    custom_fields,
    logs,
    notifications,
    projects,
    tasks,
    time_tracking,
    users,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
# app.include_router(logs.router, prefix="/logs", tags=["logs"])
# app.include_router(
#     notifications.router, prefix="/notifications", tags=["notifications"]
# )
# app.include_router(comments.router, prefix="/comments", tags=["comments"])
# app.include_router(attachments.router, prefix="/attachments", tags=["attachments"])
# app.include_router(
#     activity_feed.router, prefix="/activity_feed", tags=["activity_feed"]
# )
# app.include_router(
#     time_tracking.router, prefix="/time_tracking", tags=["time_tracking"]
# )
# app.include_router(
#     custom_fields.router, prefix="/custom_fields", tags=["custom_fields"]
# )


@app.get("/")
def read_root():
    """Test Router"""
    return {"message": "Welcome to the Task Management API"}

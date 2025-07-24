import uuid
from datetime import datetime

from pydantic import BaseModel

from src.core.task.entity import TaskStatus


class TaskResponseSchema(BaseModel):
    task_id: uuid.UUID
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime


class CreateTaskSchema(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus

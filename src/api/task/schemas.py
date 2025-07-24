import uuid
from datetime import datetime

from pydantic import BaseModel, Field, field_validator

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


class GetTaskListSchemaFilter(BaseModel):
    status: TaskStatus | None = Field(default=None, alias="status")

    @field_validator("status", mode='after')
    @classmethod
    def validate_status(cls, v):
        if isinstance(v, TaskStatus):
            return v.value
        return v

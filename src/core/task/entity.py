import uuid
from dataclasses import dataclass, field
from datetime import datetime, UTC
from enum import Enum


@dataclass
class Task:
    task_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    title: str
    description: str | None = field(default=None, kw_only=True)
    status: "TaskStatus"
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC), kw_only=True)


class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In progress"
    COMPLETED = "Completed"

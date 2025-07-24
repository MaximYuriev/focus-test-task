import uuid
from datetime import datetime
from typing import Self

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.core.commons.model import Base
from src.core.task.entity import Task, TaskStatus


class TaskModel(Base):
    __tablename__ = "task"
    task_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    @classmethod
    def from_entity(cls, task: Task) -> Self:
        return cls(
            task_id=task.task_id,
            title=task.title,
            description=task.description,
            status=task.status.value,
            created_at=task.created_at,
        )

    def to_entity(self) -> Task:
        return Task(
            task_id=self.task_id,
            title=self.title,
            description=self.description,
            status=TaskStatus(self.status),
            created_at=self.created_at,
        )

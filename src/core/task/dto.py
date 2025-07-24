from dataclasses import dataclass

from src.core.task.entity import TaskStatus


@dataclass(frozen=True, eq=False)
class CreateTaskDTO:
    title: str
    description: str | None
    status: TaskStatus


@dataclass(frozen=True, eq=False)
class UpdateTaskDTO:
    title: str | None
    description: str | None
    status: TaskStatus | None

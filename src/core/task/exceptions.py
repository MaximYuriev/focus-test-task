import uuid
from dataclasses import dataclass

from src.core.commons.exception import ApplicationException


@dataclass(frozen=True, eq=False)
class TaskException(ApplicationException):
    @property
    def message(self) -> str:
        return "Ошибка при работе с задачами!"


@dataclass(frozen=True, eq=False)
class TaskNotFoundException(TaskException):
    task_id: uuid.UUID

    @property
    def message(self) -> str:
        return f"Задача с id='{self.task_id}' не найдена!"

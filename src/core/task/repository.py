from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.task.entity import Task
from src.core.task.model import TaskModel


class TaskRepository(ABC):
    @abstractmethod
    async def add_task(self, task: Task) -> None:
        pass


class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add_task(self, task: Task) -> None:
        model = TaskModel.from_entity(task)
        self._session.add(model)
        await self._session.commit()

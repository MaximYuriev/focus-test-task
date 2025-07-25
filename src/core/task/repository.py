import uuid
from abc import ABC, abstractmethod

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.task.entity import Task
from src.core.task.exceptions import TaskNotFoundException
from src.core.task.filters import GetTaskListFilter
from src.core.task.model import TaskModel


class TaskRepository(ABC):
    @abstractmethod
    async def add_task(self, task: Task) -> None:
        pass

    @abstractmethod
    async def get_task_list(self, filters: GetTaskListFilter) -> list[Task]:
        pass

    @abstractmethod
    async def get_task_by_id(self, task_id: uuid.UUID) -> Task:
        pass

    @abstractmethod
    async def delete_task(self, task: Task) -> None:
        pass

    @abstractmethod
    async def update_task(self, task: Task) -> None:
        pass


class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add_task(self, task: Task) -> None:
        model = TaskModel.from_entity(task)
        self._session.add(model)
        await self._session.commit()

    async def get_task_list(self, filters: GetTaskListFilter) -> list[Task]:
        filter_dict = filters.to_dict()

        query = select(TaskModel).filter_by(**filter_dict)
        model_list = await self._session.scalars(query)

        return [model.to_entity() for model in model_list.all()]

    async def get_task_by_id(self, task_id: uuid.UUID) -> Task:
        query = select(TaskModel).where(TaskModel.task_id == task_id)
        model = await self._session.scalar(query)

        if model is None:
            raise TaskNotFoundException(task_id)

        return model.to_entity()

    async def delete_task(self, task: Task) -> None:
        stmt = delete(TaskModel).where(TaskModel.task_id == task.task_id)
        await self._session.execute(stmt)
        await self._session.commit()

    async def update_task(self, task: Task) -> None:
        model = TaskModel.from_entity(task)
        await self._session.merge(model)
        await self._session.commit()

import uuid
from dataclasses import asdict

from src.core.task.dto import CreateTaskDTO, UpdateTaskDTO
from src.core.task.entity import Task, TaskStatus
from src.core.task.filters import GetTaskListFilter
from src.core.task.repository import TaskRepository


class CreateTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self._task_repository = task_repository

    async def __call__(self, create_task_dto: CreateTaskDTO) -> Task:
        task = Task(
            title=create_task_dto.title,
            description=create_task_dto.description,
            status=TaskStatus(create_task_dto.status),
        )

        await self._task_repository.add_task(task)

        return task


class GetTaskListUseCase:
    def __init__(self, task_repository: TaskRepository):
        self._task_repository = task_repository

    async def __call__(self, filters: GetTaskListFilter) -> list[Task]:
        return await self._task_repository.get_task_list(filters)


class GetTaskByIdUseCase:
    def __init__(self, task_repository: TaskRepository):
        self._task_repository = task_repository

    async def __call__(self, task_id: uuid.UUID) -> Task:
        return await self._task_repository.get_task_by_id(task_id)


class DeleteTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self._task_repository = task_repository

    async def __call__(self, task_id: uuid.UUID) -> Task:
        task = await self._task_repository.get_task_by_id(task_id)

        await self._task_repository.delete_task(task)

        return task


class UpdateTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self._task_repository = task_repository

    async def __call__(self, task_id: uuid.UUID, update_task_dto: UpdateTaskDTO) -> Task:
        task = await self._task_repository.get_task_by_id(task_id)

        update_task_dict = asdict(update_task_dto)

        for key, value in update_task_dict.items():
            if value is not None:
                setattr(task, key, value)

        await self._task_repository.update_task(task)

        return task

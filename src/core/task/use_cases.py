from src.core.task.dto import CreateTaskDTO
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

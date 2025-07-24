import uuid
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Query

from src.api.task.schemas import CreateTaskSchema, TaskResponseSchema, GetTaskListSchemaFilter
from src.core.task.dto import CreateTaskDTO
from src.core.task.filters import GetTaskListFilter
from src.core.task.use_cases import CreateTaskUseCase, GetTaskListUseCase, GetTaskByIdUseCase

task_router = APIRouter(prefix="/tasks", tags=["Task"])


@task_router.post("/")
@inject
async def create_task_handler(
        schema: CreateTaskSchema,
        use_case: FromDishka[CreateTaskUseCase],
) -> TaskResponseSchema:
    dto = CreateTaskDTO(
        title=schema.title,
        description=schema.description,
        status=schema.status.value,
    )

    task = await use_case(dto)

    return TaskResponseSchema.model_validate(task, from_attributes=True)


@task_router.get("/")
@inject
async def get_task_list_handler(
        filters: Annotated[GetTaskListSchemaFilter, Query()],
        use_case: FromDishka[GetTaskListUseCase],
) -> list[TaskResponseSchema]:
    filters = GetTaskListFilter(
        status=filters.status,
    )
    task_list = await use_case(filters)

    return [
        TaskResponseSchema.model_validate(
            task,
            from_attributes=True,
        ) for task in task_list
    ]


@task_router.get("/{task_id}")
@inject
async def get_task_by_id_handler(
        task_id: uuid.UUID,
        use_case: FromDishka[GetTaskByIdUseCase],
) -> TaskResponseSchema:
    task = await use_case(task_id)

    return TaskResponseSchema.model_validate(task, from_attributes=True)

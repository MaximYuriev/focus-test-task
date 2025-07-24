from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from src.api.task.schemas import CreateTaskSchema, TaskResponseSchema
from src.core.task.dto import CreateTaskDTO
from src.core.task.use_cases import CreateTaskUseCase

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

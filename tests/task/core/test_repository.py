import uuid

import pytest
from faker import Faker

from src.core.task.entity import Task
from src.core.task.exceptions import TaskNotFoundException
from src.core.task.filters import GetTaskListFilter
from src.core.task.repository import TaskRepository


async def test_add_task(
        task: Task,
        task_repository: TaskRepository,
):
    await task_repository.add_task(task)

    assert await task_repository.get_task_by_id(task.task_id) is not None


async def test_get_task(
        task: Task,
        task_repository: TaskRepository,
):
    await task_repository.add_task(task)

    founded_task = await task_repository.get_task_by_id(task.task_id)

    assert founded_task == task


async def test_get_not_existed_task(
        task_repository: TaskRepository,
):
    with pytest.raises(TaskNotFoundException):
        await task_repository.get_task_by_id(uuid.uuid4())


async def test_update_task(
        task: Task,
        task_repository: TaskRepository,
        faker: Faker,
):
    await task_repository.add_task(task)

    updated_task = await task_repository.get_task_by_id(task.task_id)
    updated_task.title = faker.sentence()
    await task_repository.update_task(updated_task)

    founded_task = await task_repository.get_task_by_id(task.task_id)

    assert founded_task != task
    assert founded_task == updated_task


async def test_delete_task(
        task: Task,
        task_repository: TaskRepository,
):
    await task_repository.add_task(task)

    await task_repository.delete_task(task)

    with pytest.raises(TaskNotFoundException):
        await task_repository.get_task_by_id(task.task_id)


async def test_get_task_list(
        task: Task,
        task_repository: TaskRepository,
):
    await task_repository.add_task(task)
    task.task_id = uuid.uuid4()
    await task_repository.add_task(task)

    filters = GetTaskListFilter(
        status=None
    )

    assert len(await task_repository.get_task_list(filters)) == 2


async def test_get_task_list_empty(
        task_repository: TaskRepository,
):
    filters = GetTaskListFilter(status=None)
    assert len(await task_repository.get_task_list(filters)) == 0


async def test_get_task_list_with_filters(
        task: Task,
        task_repository: TaskRepository,
):
    await task_repository.add_task(task)
    task.task_id = uuid.uuid4()
    await task_repository.add_task(task)

    filters = GetTaskListFilter(
        status=task.status.value,
    )

    assert len(await task_repository.get_task_list(filters)) == 2

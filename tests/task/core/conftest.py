import random

import pytest
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.task.entity import Task, TaskStatus
from src.core.task.repository import TaskRepository, SQLAlchemyTaskRepository


@pytest.fixture
def task_repository(async_session: AsyncSession) -> TaskRepository:
    return SQLAlchemyTaskRepository(async_session)


@pytest.fixture
def task(faker: Faker) -> Task:
    return Task(
        title=faker.sentence(),
        description=random.choice(
            (faker.sentence(), None)
        ),
        status=random.choice(
            list(TaskStatus),
        )
    )

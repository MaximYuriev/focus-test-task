from typing import AsyncGenerator

import pytest
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker
from src.config import config

from src.core.commons.model import Base


@pytest.fixture(scope='session')
def async_engine() -> AsyncEngine:
    return create_async_engine(
        config.postgres.db_url,
        echo=False,
        poolclass=NullPool,
    )


@pytest.fixture(scope="session")
def async_session_maker(
        async_engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        async_engine,
        expire_on_commit=False,
    )


@pytest.fixture
async def async_session(
        async_session_maker: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@pytest.fixture(autouse=True)
async def prepare_database(async_engine: AsyncEngine):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

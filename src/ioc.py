from typing import AsyncGenerator

from dishka import Provider, from_context, Scope, provide, make_async_container
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from src.config import Config, config
from src.core.task.repository import TaskRepository, SQLAlchemyTaskRepository
from src.core.task.use_cases import CreateTaskUseCase, GetTaskListUseCase, GetTaskByIdUseCase


class SQLAlchemyProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_async_engine(self, _config: Config) -> AsyncEngine:
        return create_async_engine(_config.postgres.db_url, echo=False)

    @provide(scope=Scope.APP)
    def get_async_session_maker(
            self,
            engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self,
            session_maker: async_sessionmaker[AsyncSession],
    ) -> AsyncGenerator[AsyncSession, None]:
        async with session_maker() as session:
            yield session


class TaskProvider(Provider):
    scope = Scope.REQUEST

    task_repository = provide(SQLAlchemyTaskRepository, provides=TaskRepository)

    create_task_use_case = provide(CreateTaskUseCase)
    get_task_list_use_case = provide(GetTaskListUseCase)
    get_task_by_id_use_case = provide(GetTaskByIdUseCase)


container = make_async_container(
    SQLAlchemyProvider(),
    TaskProvider(),
    context={Config: config, }
)

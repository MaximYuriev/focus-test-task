from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.api.task.handler import task_router
from src.ioc import container


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(task_router)

    setup_dishka(container, app)

    return app

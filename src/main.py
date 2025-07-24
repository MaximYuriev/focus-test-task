from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.api.commons.exception_handler import register_exception_handler
from src.api.task.handler import task_router
from src.ioc import container


def create_app() -> FastAPI:
    app = FastAPI(
        title="Focus Test Task",
        debug=True,
    )

    register_exception_handler(app)

    app.include_router(task_router)

    setup_dishka(container, app)

    return app

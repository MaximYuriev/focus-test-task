from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.core.commons.exception import ApplicationException
from src.core.task.exceptions import TaskNotFoundException


def register_exception_handler(app: FastAPI) -> None:
    @app.exception_handler(TaskNotFoundException)
    def task_not_found_exception_handler(
            request: Request,
            exception: TaskNotFoundException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": exception.message},
        )

    @app.exception_handler(ApplicationException)
    def application_exception_handler(
            request: Request,
            exception: ApplicationException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exception.message},
        )

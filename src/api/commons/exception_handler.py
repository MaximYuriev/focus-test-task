from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.core.commons.exception import ApplicationException


def register_exception_handler(app: FastAPI) -> None:
    @app.exception_handler(ApplicationException)
    def register_handler_for_application_exception(
            request: Request,
            exception: ApplicationException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exception.message},
        )

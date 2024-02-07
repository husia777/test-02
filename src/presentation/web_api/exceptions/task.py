from fastapi import Request
from fastapi.responses import JSONResponse


async def task_not_exists_exception_handler() -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"message": "Такого сменного задания  не существует."},
    )

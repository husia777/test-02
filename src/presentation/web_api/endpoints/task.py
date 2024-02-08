from datetime import datetime
from src.domain.entities.shift_task import AvailableFilters
from fastapi import APIRouter, Depends, HTTPException
from src.presentation.web_api.dependencies.depends_stub import Stub
from src.presentation.web_api.providers.abstract.task import task_service_provider
from src.presentation.web_api.schemas.shift_task import (
    ShiftTasksCreateSchema,
    ShiftTasksUpdateSchema,
)
from src.interactors.task_service import TaskService

task_router = APIRouter(
    tags=["task"],
)


@task_router.post("/tasks/add")
async def add_shift_tasks(
    tasks: list[ShiftTasksCreateSchema],
    task_service: TaskService = Depends(Stub(task_service_provider)),
):
    return await task_service.add_tasks(tasks)


@task_router.get("/tasks/{task_id}")
async def get_task_by_id(
    task_id: int, task_service: TaskService = Depends(Stub(task_service_provider))
):
    task = await task_service.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=404, detail="Такого сменного задания  не существует."
        )
    return task


@task_router.patch("/tasks/{task_id}")
async def update_task(
    task_id: int,
    payload: ShiftTasksUpdateSchema,
    task_service: TaskService = Depends(Stub(task_service_provider)),
):
    task = await task_service.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=404, detail="Такого сменного задания  не существует."
        )
    update_data = payload.dict(exclude_unset=True)
    return await task_service.update_task_by_id(task_id, update_data)


@task_router.get("/tasks/filter")
async def get_tasks_by_filter(
    sort_field: AvailableFilters,
    skip: int = 0,
    limit: int = 100,
    task_service: TaskService = Depends(Stub(task_service_provider)),
    closure_status: bool | None = None,
    shift_task_description: str | None = None,
    line: str | None = None,
    shift: str | None = None,
    crew: str | None = None,
    batch_number: int | None = None,
    batch_date: datetime | None = None,
    nomenclature: str | None = None,
    ecn_code: str | None = None,
    rc_identifier: str | None = None,
    shift_start_time: datetime | None = None,
    shift_end_time: datetime | None = None,
):
    return await task_service.get_tasks_by_filter(
        skip,
        limit,
        sort_field,
        closure_status,
        shift_task_description,
        line,
        shift,
        crew,
        batch_number,
        batch_date,
        nomenclature,
        ecn_code,
        rc_identifier,
        shift_start_time,
        shift_end_time,
    )


@task_router.get("/tasks")
async def get_all_tasks(
    task_service: TaskService = Depends(Stub(task_service_provider)),
):
    return await task_service.get_all_tasks()

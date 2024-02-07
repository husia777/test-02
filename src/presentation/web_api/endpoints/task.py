from fastapi import APIRouter, Depends, HTTPException
from src.presentation.web_api.dependencies.depends_stub import Stub
from src.presentation.web_api.providers.abstract.task import task_service_provider
from src.presentation.web_api.schemas.shift_task import ShiftTasksCreateSchema, ShiftTasksUpdateSchema
from src.interactors.task.task_service import TaskService
task_router = APIRouter(
    tags=['users'],

)


@task_router.post('/tasks/add')
async def add_shift_tasks(tasks: list[ShiftTasksCreateSchema], task_service: TaskService = Depends(Stub(task_service_provider))):
    return await task_service.add_tasks(tasks)


@task_router.get('/tasks/{id}')
async def get_task_by_id(id: int, task_service: TaskService = Depends(Stub(task_service_provider))):
    task = await task_service.get_task_by_id(id)
    if task is None:
        raise HTTPException(
            status_code=404, detail="Такого сменного задания  не существует.")
    return task


@task_router.patch('/tasks/{task_id}')
async def update_task(task_id: int, payload: ShiftTasksUpdateSchema, task_service: TaskService = Depends(Stub(task_service_provider))):
    update_data = payload.dict(exclude_unset=True)
    return await task_service.update_task_by_id(task_id, update_data)


@task_router.get('/tasks')
async def get_all_users(task_service: TaskService = Depends(Stub(task_service_provider))):
    return await task_service.get_all_tasks()

from fastapi import APIRouter, Depends
from src.presentation.web_api.dependencies.depends_stub import Stub
from src.presentation.web_api.providers.abstract.task import task_service_provider
from src.presentation.web_api.schemas.shift_task import ShiftTasksEntity
from src.interactors.task.task_service import TaskService
task_router = APIRouter(
    tags=['users'],

)


@task_router.post('/tasks/add')
async def add_shift_tasks(tasks: list[ShiftTasksEntity], task_service: TaskService = Depends(Stub(task_service_provider))):
    return await task_service.add_tasks(tasks)


@task_router.get('/tasks/{id}')
async def get_task_by_id(id: int, task_service: TaskService = Depends(Stub(task_service_provider))):
    return await task_service.get_task_by_id(id)


@task_router.get('/tasks')
async def get_all_users(task_service: TaskService = Depends(Stub(task_service_provider))):
    return await task_service.get_all_tasks()


@task_router.delete('/users/{id}')
async def remove_user_by_id(id: int, task_service: TaskService = Depends(Stub(task_service_provider))):
    return await task_service.remove_user_by_id(id)

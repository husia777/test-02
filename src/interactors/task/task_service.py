
from src.presentation.web_api.exceptions.task import task_not_exists_exception_handler
from src.domain.entities.shift_task import ShiftTaskId, ShiftTasksEntity


class TaskService:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    async def add_tasks(self, tasks: list[ShiftTasksEntity]):
        return await self.task_repository.add_tasks(tasks)

    async def get_task_by_id(self, id: int):
        task = await self.task_repository.get_task_by_id(id)
        if task is None:
            raise task_not_exists_exception_handler
        return await self.task_repository.get_task_by_id(id)

    async def get_all_tasks(self):
        return await self.task_repository.get_all_tasks()

    async def remove_user_by_id(self, id: int):
        return await self.task_repository.remove_user_by_id(id)

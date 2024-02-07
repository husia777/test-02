
from src.domain.entities.shift_task import ShiftTaskId, ShiftTasksEntity


class TaskService:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    async def add_tasks(self, tasks: list[ShiftTasksEntity]):
        return await self.task_repository.add_tasks(tasks)

    async def get_task_by_id(self, id: int):
        return await self.task_repository.get_task_by_id(id)

    async def update_task_by_id(self, task_id: int, update_data: ShiftTasksEntity):
        return await self.task_repository.update_task_by_id(task_id, update_data)

    async def get_all_tasks(self):
        return await self.task_repository.get_all_tasks()

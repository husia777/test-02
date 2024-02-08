from src.domain.entities.shift_task import (
    AvailableFilters,
    ShiftTasksEntity,
)


class TaskService:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    async def add_tasks(self, tasks: list[ShiftTasksEntity]):
        return await self.task_repository.add_tasks(tasks)

    async def get_task_by_id(self, task_id: int):
        return await self.task_repository.get_task_by_id(task_id)

    async def update_task_by_id(self, task_id: int, update_data: ShiftTasksEntity):
        return await self.task_repository.update_task_by_id(task_id, update_data)

    async def get_tasks_by_filter(
        self,
        skip: int,
        limit: int,
        sort_field: AvailableFilters,
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
    ):
        return await self.task_repository.get_tasks_by_filter(
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

    async def get_all_tasks(self):
        return await self.task_repository.get_all_tasks()

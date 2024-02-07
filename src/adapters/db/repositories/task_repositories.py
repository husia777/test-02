from abc import ABC, abstractmethod
from datetime import datetime
from sqlalchemy import select, delete, update, insert
from sqlalchemy.orm import Session
from src.adapters.db.repositories.converters.task import task_entity_to_model
from src.adapters.db.models.shift_task import ShiftTask
from src.domain.entities.shift_task import ShiftTasksEntity, ShiftTaskId
from sqlalchemy.ext.asyncio import AsyncSession


class TaskRepositoryInterface(ABC):

    @abstractmethod
    async def add_tasks(self, user: ShiftTasksEntity):
        pass

    @abstractmethod
    async def get_task_by_id(self, id: int) -> ShiftTasksEntity:
        pass

    @abstractmethod
    async def get_all_tasks(self) -> list[ShiftTasksEntity]:
        pass

    @abstractmethod
    async def update_task_by_id(self, task_id: int, update_data: ShiftTasksEntity):
        pass


class TaskRepository(TaskRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_tasks(self, tasks: list[ShiftTasksEntity]):
        for task in tasks:

            task_in_db = await task_entity_to_model(task)
            self.session.add(task_in_db)
        await self.session.commit()

    async def get_task_by_id(self, id: int) -> ShiftTasksEntity:
        task = await self.session.execute(select(ShiftTask).where(ShiftTask.id == id))
        return task.scalars().first()

    async def update_task_by_id(self, task_id: int, update_data: ShiftTasksEntity):
        if "closure_status" in update_data:
            if update_data['closure_status']:
                update_data["closed_at"] = datetime.now()
            else:
                update_data["closed_at"] = None

        stmt = update(ShiftTask).where(ShiftTask.id == task_id).values(
            update_data).returning(ShiftTask)
        result = await self.session.execute(stmt)
        await self.session.commit()  # примените изменения в базе данных
        return result.scalar_one()

    async def get_all_tasks(self) -> list[ShiftTasksEntity]:
        tasks = await self.session.execute(select(ShiftTask))
        return tasks.scalars().all()

    async def get_user_by_id(self, id: int) -> ShiftTasksEntity:
        user = await self.session.execute(select(ShiftTask).where(ShiftTask.id == id))
        return user.scalars().first()

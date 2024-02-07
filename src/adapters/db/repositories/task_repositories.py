from abc import ABC, abstractmethod
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
    async def remove_user_by_id(self, id: int):
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

    async def get_all_tasks(self) -> list[ShiftTasksEntity]:
        tasks = await self.session.execute(select(ShiftTask))
        return tasks.scalars().all()

    async def get_user_by_id(self, id: int) -> ShiftTasksEntity:
        user = await self.session.execute(select(ShiftTask).where(ShiftTask.id == id))
        return user.scalars().first()

    async def remove_user_by_id(self, id: int):
        await self.session.execute(delete(ShiftTask).where(ShiftTask.id == id))

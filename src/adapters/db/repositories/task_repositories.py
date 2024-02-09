from abc import ABC, abstractmethod
from datetime import datetime
from sqlalchemy import select, update, and_
from sqlalchemy.orm import joinedload
from src.adapters.db.repositories.converters.task import task_entity_to_model
from src.adapters.db.models.shift_task import ShiftTask
from src.domain.entities.shift_task import (
    AvailableFilters,
    ProductEntity,
    ShiftTasksEntity,
)
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

    @abstractmethod
    async def get_tasks_by_filter(
        self,
        skip: int,
        limit: int,
        filter_by: AvailableFilters,
    ):
        pass


class TaskRepository(TaskRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_tasks(self, tasks: list[ShiftTasksEntity]):
        for task in tasks:
            task_in_db = await task_entity_to_model(task)
            self.session.add(task_in_db)
        await self.session.commit()
        return {"message": "Tasks added"}

    async def get_task_by_id(self, task_id: int) -> ShiftTasksEntity:
        task = await self.session.execute(
            select(ShiftTask).where(ShiftTask.id == task_id)
        )
        return task.unique().scalars().first()

    async def update_task_by_id(self, task_id: int, update_data: ShiftTasksEntity):
        task_in_db = await self.session.execute(
            select(ShiftTask).where(ShiftTask.id == task_id)
        )

        if "closure_status" in update_data:
            if (
                update_data["closure_status"] is True
                and task_in_db.scalars().first().closed_at is None
            ):
                update_data["closed_at"] = datetime.now()
            elif (
                update_data["closure_status"] is False
                and task_in_db.scalars().first().closed_at is not None
            ):
                update_data["closed_at"] = None
        stmt = (
            update(ShiftTask)
            .where(ShiftTask.id == task_id)
            .values(update_data)
            .returning(ShiftTask)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_tasks_by_filter(self, skip: int, limit: int, sort_field: AvailableFilters, closure_status, shift_task_description,
                                  line, shift, crew, batch_number, batch_date, nomenclature, ecn_code, rc_identifier,
                                  shift_start_time, shift_end_time) -> ShiftTasksEntity:

        filters = {
            'closure_status': closure_status,
            'shift_task_description': shift_task_description,
            'line': line,
            'shift': shift,
            'crew': crew,
            'batch_number': batch_number,
            'batch_date': batch_date,
            'nomenclature': nomenclature,
            'ecn_code': ecn_code,
            'rc_identifier': rc_identifier,
            'shift_start_time': shift_start_time,
            'shift_end_time': shift_end_time
        }

        # Создание динамического условия для фильтрации
        filter_conditions = [getattr(
            ShiftTask, field) == value for field, value in filters.items() if value is not None]

        # Получение заданий с учетом фильтров и пагинации
        filtered_tasks = await self.session.execute(select(ShiftTask).where(and_(*filter_conditions)).offset(skip).limit(limit).order_by(getattr(ShiftTask, sort_field.name)))
        return filtered_tasks.scalars().all()

    async def add_product_to_shift_task(self, product: ProductEntity):
        self.session.add(product)
        await self.session.commit()

    async def get_all_tasks(self):
        tasks = await self.session.execute(
            select(ShiftTask).options(joinedload(ShiftTask.products))
        )
        query = tasks.unique().scalars().all()
        print("------")
        print(query)
        print("------")
        return query


# Если продукция передана с несуществующей партией
# (нет сменного задания с указаным номером партии и датой партии),
# то данную продукцию можно игнорировать.

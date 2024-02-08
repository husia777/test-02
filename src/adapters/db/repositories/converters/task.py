from src.adapters.db.models.shift_task import ShiftTask
from src.domain.entities.shift_task import ShiftTasksEntity


async def task_entity_to_model(task: ShiftTasksEntity) -> ShiftTask:
    db_task = ShiftTask(
        closure_status=task.closure_status,
        shift_task_description=task.shift_task_description,
        line=task.line,
        shift=task.shift,
        crew=task.crew,
        batch_number=task.batch_number,
        batch_date=task.batch_date,
        nomenclature=task.nomenclature,
        ecn_code=task.ecn_code,
        rc_identifier=task.rc_identifier,
        shift_start_time=task.shift_start_time,
        shift_end_time=task.shift_end_time,
    )

    return db_task

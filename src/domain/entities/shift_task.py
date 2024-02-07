

from dataclasses import dataclass
from datetime import datetime
from typing import NewType

ShiftTaskId = NewType("ShiftTaskId", int)


@dataclass
class ShiftTasksEntity:
    closure_status: bool | None
    shift_task_description: str | None
    line: str | None
    shift: str | None
    crew: str | None
    batch_number: int | None
    batch_date: datetime | None
    nomenclature: str | None
    ecn_code: str | None
    rc_identifier: str | None
    shift_start_time: datetime | None
    shift_end_time: datetime | None

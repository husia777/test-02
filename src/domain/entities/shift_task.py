

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
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


class AvailableFilters(str, Enum):
    closure_status = 'Closure status'
    shift_task_description = 'Shift task description'
    line = 'Line'
    shift = 'Shift'
    crew = 'Crew'
    batch_number = 'Batch number'
    batch_date = 'Batch date'
    nomenclature = 'Nomenclature'
    ecn_code = 'ECN code'
    rc_identifier = 'RC identifier'
    shift_start_time = 'Shift start time'
    shift_end_time = 'Shift end time'

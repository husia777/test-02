

from dataclasses import dataclass
from datetime import datetime
from typing import NewType

ShiftTaskId = NewType("ShiftTaskId", int)


@dataclass
class ShiftTasksEntity:
    closure_status: bool
    shift_task_description: str
    line: str
    shift: str
    crew: str
    batch_number: int
    batch_date: datetime
    nomenclature: str
    ecn_code: str
    rc_identifier: str
    shift_start_time: datetime
    shift_end_time: datetime

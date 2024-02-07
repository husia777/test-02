from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class ShiftTasksCreateSchema(BaseModel):
    closure_status: bool = Field(..., alias="СтатусЗакрытия")
    shift_task_description: str = Field(...,
                                        alias="ПредставлениеЗаданияНаСмену")
    line: str = Field(..., alias="Линия")
    shift: str = Field(..., alias="Смена")
    crew: str = Field(..., alias="Бригада")
    batch_number: int = Field(..., alias="НомерПартии")
    batch_date: datetime = Field(..., alias="ДатаПартии")
    nomenclature: str = Field(..., alias="Номенклатура")
    ecn_code: str = Field(..., alias="КодЕКН")
    rc_identifier: str = Field(..., alias="ИдентификаторРЦ")
    shift_start_time: datetime = Field(..., alias="ДатаВремяНачалаСмены")
    shift_end_time: datetime = Field(..., alias="ДатаВремяОкончанияСмены")


class ShiftTasksUpdateSchema(BaseModel):
    closure_status: bool | None = None
    shift_task_description: str | None = None
    line: str | None = None
    shift: str | None = None
    crew: str | None = None
    batch_number: int | None = None
    batch_date: datetime | None = None
    nomenclature: str | None = None
    ecn_code: str | None = None
    rc_identifier: str | None = None
    shift_start_time: datetime | None = None
    shift_end_time: datetime | None = None





from datetime import datetime
from pydantic import BaseModel, Field


class ShiftTasksEntity(BaseModel):
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

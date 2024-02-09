from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import DateTime
from src.adapters.db.models.aggregate_all_models import Product

from src.adapters.db.connection import Base


class ShiftTask(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    products: Mapped[list[Product]] = relationship(back_populates="owner")
    closure_status: Mapped[bool] = mapped_column()
    shift_task_description: Mapped[str] = mapped_column()
    line: Mapped[str] = mapped_column()
    shift: Mapped[str] = mapped_column()
    crew: Mapped[str] = mapped_column()
    batch_number: Mapped[int] = mapped_column(unique=True)
    batch_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), unique=True)
    nomenclature: Mapped[str] = mapped_column()
    ecn_code: Mapped[str] = mapped_column()
    rc_identifier: Mapped[str] = mapped_column()
    shift_start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    shift_end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    closed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True)

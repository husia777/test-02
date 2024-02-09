from src.adapters.db.connection import Base
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.adapters.db.models.shift_task import ShiftTask


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    unique_product_code: Mapped[str] = mapped_column(unique=True)

    batch_number: Mapped[int] = mapped_column(ForeignKey("tasks.batch_number"))
    batch_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), unique=True)
    is_aggregated: Mapped[bool] = mapped_column(default=False)
    aggregated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    owner: Mapped['ShiftTask'] = relationship(back_populates="products")

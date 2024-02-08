"""Initial migration

Revision ID: 28f93ea891a0
Revises:   
Create Date: 2024-02-08 16:18:36.563019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "28f93ea891a0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("closure_status", sa.Boolean(), nullable=False),
        sa.Column("shift_task_description", sa.String(), nullable=False),
        sa.Column("line", sa.String(), nullable=False),
        sa.Column("shift", sa.String(), nullable=False),
        sa.Column("crew", sa.String(), nullable=False),
        sa.Column("batch_number", sa.Integer(), nullable=False),
        sa.Column("batch_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("nomenclature", sa.String(), nullable=False),
        sa.Column("ecn_code", sa.String(), nullable=False),
        sa.Column("rc_identifier", sa.String(), nullable=False),
        sa.Column("shift_start_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("shift_end_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("closed_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("batch_date"),
        sa.UniqueConstraint("batch_number"),
    )
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("unique_product_code", sa.String(), nullable=False),
        sa.Column("batch_number", sa.Integer(), nullable=False),
        sa.Column("batch_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("is_aggregated", sa.Boolean(), nullable=False),
        sa.Column("aggregated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["batch_number"],
            ["tasks.batch_number"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("batch_date"),
        sa.UniqueConstraint("unique_product_code"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    op.drop_table("tasks")
    # ### end Alembic commands ###

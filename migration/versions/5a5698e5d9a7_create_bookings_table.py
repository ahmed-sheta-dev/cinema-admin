"""create bookings table

Revision ID: 5a5698e5d9a7
Revises: fd4bb76cd5f8
Create Date: 2026-01-20 18:25:14.348820

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "5a5698e5d9a7"
down_revision: Union[str, Sequence[str], None] = "fd4bb76cd5f8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bookings",
        sa.Column(
            "id", mysql.INTEGER(unsigned=True), primary_key=True, autoincrement=True
        ),
        sa.Column(
            "showtime_id",
            mysql.INTEGER(unsigned=True),
            sa.ForeignKey("showtimes.id", ondelete="RESTRICT"),
            nullable=False,
        ),
        sa.Column("customer_name", sa.String(120), nullable=False),
        sa.Column("customer_phone", sa.String(30), nullable=True),
        sa.Column("seats", mysql.SMALLINT(unsigned=True), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="confirmed"),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
            server_onupdate=sa.text("CURRENT_TIMESTAMP"),
        ),
        mysql_engine="InnoDB",
    )

    op.create_index("ix_bookings_showtime_id", "bookings", ["showtime_id"])
    op.create_index("ix_bookings_created_at", "bookings", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_bookings_created_at", table_name="bookings")
    op.drop_index("ix_bookings_showtime_id", table_name="bookings")
    op.drop_table("bookings")

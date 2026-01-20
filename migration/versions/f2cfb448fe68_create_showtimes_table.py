"""create showtimes table

Revision ID: f2cfb448fe68
Revises: 181a19ee009f
Create Date: 2026-01-20 16:11:54.788050

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "f2cfb448fe68"
down_revision: Union[str, Sequence[str], None] = "181a19ee009f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "showtimes",
        sa.Column(
            "id", mysql.INTEGER(unsigned=True), primary_key=True, autoincrement=True
        ),
        sa.Column(
            "movie_id",
            mysql.INTEGER(unsigned=True),
            sa.ForeignKey("movies.id", ondelete="RESTRICT"),
            nullable=False,
        ),
        sa.Column(
            "hall_id",
            mysql.INTEGER(unsigned=True),
            sa.ForeignKey("halls.id", ondelete="RESTRICT"),
            nullable=False,
        ),
        sa.Column("starts_at", sa.DateTime(), nullable=False),
        sa.Column("price", sa.Numeric(10, 2), nullable=False, server_default="0.00"),
        sa.Column("status", sa.String(20), nullable=False, server_default="scheduled"),
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

    op.create_index("ix_showtimes_starts_at", "showtimes", ["starts_at"])
    op.create_index("ix_showtimes_movie_id", "showtimes", ["movie_id"])
    op.create_index("ix_showtimes_hall_id", "showtimes", ["hall_id"])


def downgrade() -> None:
    op.drop_index("ix_showtimes_hall_id", table_name="showtimes")
    op.drop_index("ix_showtimes_movie_id", table_name="showtimes")
    op.drop_index("ix_showtimes_starts_at", table_name="showtimes")
    op.drop_table("showtimes")

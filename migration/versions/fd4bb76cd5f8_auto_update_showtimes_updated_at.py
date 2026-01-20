"""auto update showtimes.updated_at

Revision ID: fd4bb76cd5f8
Revises: 3b6359c995e7
Create Date: 2026-01-20 16:42:58.641110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd4bb76cd5f8'
down_revision: Union[str, Sequence[str], None] = '3b6359c995e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.execute(
        """
        ALTER TABLE showtimes
        MODIFY updated_at DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE showtimes
        MODIFY updated_at DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP
        """
    )

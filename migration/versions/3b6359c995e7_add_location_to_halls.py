"""add location to halls

Revision ID: 3b6359c995e7
Revises: f2cfb448fe68
Create Date: 2026-01-20 16:16:39.318755

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3b6359c995e7"
down_revision: Union[str, Sequence[str], None] = "f2cfb448fe68"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("halls", sa.Column("location", sa.String(120), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("halls", "location")

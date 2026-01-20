"""baseline

Revision ID: 181a19ee009f
Revises:
Create Date: 2026-01-19 16:25:14.176755

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "181a19ee009f"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

"""Update user database

Revision ID: bb8b9745b20a
Revises: 828cbcfb6ddb
Create Date: 2024-11-16 00:20:52.380411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb8b9745b20a'
down_revision: Union[str, None] = '828cbcfb6ddb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('department', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'department')
    # ### end Alembic commands ###
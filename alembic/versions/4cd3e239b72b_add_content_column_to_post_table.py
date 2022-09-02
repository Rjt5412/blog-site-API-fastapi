"""add content column to post table

Revision ID: 4cd3e239b72b
Revises: af40d2eb4e9b
Create Date: 2022-09-03 00:06:07.880322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cd3e239b72b'
down_revision = 'af40d2eb4e9b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')

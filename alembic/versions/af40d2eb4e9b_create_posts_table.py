"""create posts table

Revision ID: af40d2eb4e9b
Revises: 
Create Date: 2022-09-03 00:02:22.597629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af40d2eb4e9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table('posts')

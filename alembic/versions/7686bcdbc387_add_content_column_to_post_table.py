"""add content column to post table

Revision ID: 7686bcdbc387
Revises: 28338b3cf52b
Create Date: 2023-01-26 06:55:23.673425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7686bcdbc387'
down_revision = '28338b3cf52b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    

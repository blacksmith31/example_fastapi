"""create post table

Revision ID: 28338b3cf52b
Revises: 
Create Date: 2023-01-26 06:42:54.618338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28338b3cf52b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    , sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
    

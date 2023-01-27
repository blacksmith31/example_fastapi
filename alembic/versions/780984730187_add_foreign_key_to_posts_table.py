"""add foreign key to posts table

Revision ID: 780984730187
Revises: eaa5c65349d1
Create Date: 2023-01-27 05:55:11.116828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '780984730187'
down_revision = 'eaa5c65349d1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                            local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')

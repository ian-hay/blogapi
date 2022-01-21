"""add content column to posts table

Revision ID: 6e79bffb90d6
Revises: 4f3609a5d952
Create Date: 2022-01-21 00:30:50.697328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e79bffb90d6'
down_revision = '4f3609a5d952'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

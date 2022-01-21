"""Create posts table

Revision ID: 4f3609a5d952
Revises: 
Create Date: 2022-01-20 23:48:33.054047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f3609a5d952'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), \
        sa.Column("title", sa.String(),nullable=False))
    pass

def downgrade():
    op.drop_table("posts")
    pass
"""add user table

Revision ID: 9610f704be3a
Revises: 6e79bffb90d6
Create Date: 2022-01-21 01:13:35.600453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9610f704be3a'
down_revision = '6e79bffb90d6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass

def downgrade():
    op.drop_table('users')
    pass

"""student add restrictions

Revision ID: d8272c3a9965
Revises: 05dd9f89d172
Create Date: 2022-07-06 22:55:49.093947

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'd8272c3a9965'
down_revision = '05dd9f89d172'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('student', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('student', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
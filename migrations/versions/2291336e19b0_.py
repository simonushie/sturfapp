"""empty message

Revision ID: 2291336e19b0
Revises: 4de123a0297f
Create Date: 2021-02-01 16:20:32.106224

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2291336e19b0'
down_revision = '4de123a0297f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roomie_request', 'date_of_request')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roomie_request', sa.Column('date_of_request', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
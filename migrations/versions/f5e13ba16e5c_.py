"""empty message

Revision ID: f5e13ba16e5c
Revises: 53c1f1a5fd57
Create Date: 2021-02-07 07:02:34.966824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5e13ba16e5c'
down_revision = '53c1f1a5fd57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phones', sa.Column('address', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('phones', 'address')
    # ### end Alembic commands ###

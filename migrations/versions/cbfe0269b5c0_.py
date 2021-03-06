"""empty message

Revision ID: cbfe0269b5c0
Revises: d35a68b6b369
Create Date: 2021-02-09 14:35:54.334569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbfe0269b5c0'
down_revision = 'd35a68b6b369'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phones', sa.Column('ad_type', sa.String(length=1500), nullable=True))
    op.add_column('tablets', sa.Column('ad_type', sa.String(length=1500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tablets', 'ad_type')
    op.drop_column('phones', 'ad_type')
    # ### end Alembic commands ###

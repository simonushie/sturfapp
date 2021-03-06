"""adding link column to Post table

Revision ID: 4cbedc658398
Revises: 5caec6aca4e7
Create Date: 2021-01-22 10:16:58.835753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cbedc658398'
down_revision = '5caec6aca4e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('link', sa.String(length=30000), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'link')
    # ### end Alembic commands ###

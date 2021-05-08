"""empty message

Revision ID: ca3b1b9d9536
Revises: a4b4c311fc8d
Create Date: 2021-03-23 02:43:11.453475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca3b1b9d9536'
down_revision = 'a4b4c311fc8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('claimers', sa.Column('last_interaction_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('claimers', 'last_interaction_time')
    # ### end Alembic commands ###

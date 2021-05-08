"""empty message

Revision ID: a4b4c311fc8d
Revises: de77fcf071c2
Create Date: 2021-03-23 02:40:59.599933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4b4c311fc8d'
down_revision = 'de77fcf071c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('claimers', sa.Column('last_interaction_time', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('claimers', 'last_interaction_time')
    # ### end Alembic commands ###

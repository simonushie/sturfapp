"""addding followers table

Revision ID: 5caec6aca4e7
Revises: 4d38b6637905
Create Date: 2021-01-20 09:45:44.932818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5caec6aca4e7'
down_revision = '4d38b6637905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

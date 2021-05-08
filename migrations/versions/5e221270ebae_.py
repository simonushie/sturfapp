"""empty message

Revision ID: 5e221270ebae
Revises: 408274878e04
Create Date: 2021-02-13 11:46:51.068966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e221270ebae'
down_revision = '408274878e04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('viewed__posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('viewed__posts',
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='viewed__posts_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', name='viewed__posts_pkey')
    )
    # ### end Alembic commands ###

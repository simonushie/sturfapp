"""empty message

Revision ID: cc83b161c04a
Revises: fa00134152ee
Create Date: 2021-02-13 11:32:04.890342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc83b161c04a'
down_revision = 'fa00134152ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('viewed__posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('viewed__posts',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='viewed__posts_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', 'user_id', name='viewed__posts_pkey')
    )
    # ### end Alembic commands ###
"""empty message

Revision ID: 12552f65800b
Revises: 8f4d1d17fecd
Create Date: 2021-03-02 17:11:05.869381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12552f65800b'
down_revision = '8f4d1d17fecd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reported__post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reported__post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('inappropriate_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('offensive_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('hate_speech_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('inaccurate_info_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('report_type', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='reported__post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reported__post_pkey')
    )
    # ### end Alembic commands ###

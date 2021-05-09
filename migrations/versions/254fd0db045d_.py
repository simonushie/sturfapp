"""empty message

Revision ID: 254fd0db045d
Revises: dd2886441909
Create Date: 2021-03-02 17:41:49.605700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254fd0db045d'
down_revision = 'dd2886441909'
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
    sa.Column('report_type', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('inappropriate_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('offensive_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('hate_speech_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('inaccurate_info_count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='reported__post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reported__post_pkey')
    )
    # ### end Alembic commands ###
"""empty message

Revision ID: 1ba59970c69a
Revises: 98a711efbaac
Create Date: 2021-03-02 13:50:59.561559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ba59970c69a'
down_revision = '98a711efbaac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report__post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('inappropriate_count', sa.Integer(), nullable=False),
    sa.Column('offensive_count', sa.Integer(), nullable=False),
    sa.Column('hate_speech_count', sa.Integer(), nullable=False),
    sa.Column('inaccurate_info_count', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report__post')
    # ### end Alembic commands ###

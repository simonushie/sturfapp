"""empty message

Revision ID: a38b50fc7870
Revises: 6d00ec30ba26
Create Date: 2021-02-20 17:55:58.188389

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a38b50fc7870'
down_revision = '6d00ec30ba26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roomie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roomie',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date_joined', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('religion', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('level', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('based', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('budget', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='roomie_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='roomie_pkey')
    )
    # ### end Alembic commands ###

"""empty message

Revision ID: 980adefb4fc9
Revises: 81043effa7e0
Create Date: 2021-04-01 08:24:40.563559

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '980adefb4fc9'
down_revision = '81043effa7e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('claimers__specific__message__read__time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('claimers__specific__message__read__time',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('message_sender_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_read_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['message_sender_id'], ['user.id'], name='claimers__specific__message__read__time_message_sender_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='claimers__specific__message__read__time_pkey')
    )
    # ### end Alembic commands ###

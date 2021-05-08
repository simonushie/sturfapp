"""empty message

Revision ID: 49c54b57b4d2
Revises: ca3b1b9d9536
Create Date: 2021-03-23 03:58:55.819397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c54b57b4d2'
down_revision = 'ca3b1b9d9536'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('claimers__specific__message__read__time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_sender_id', sa.Integer(), nullable=True),
    sa.Column('last_read_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['message_sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('claimers__specific__message__read__time')
    # ### end Alembic commands ###

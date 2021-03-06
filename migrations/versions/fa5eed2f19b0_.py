"""empty message

Revision ID: fa5eed2f19b0
Revises: a5d8cf9e35f6
Create Date: 2021-02-02 17:47:12.744546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa5eed2f19b0'
down_revision = 'a5d8cf9e35f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracked_messages', sa.Column('recipient_id', sa.Integer(), nullable=True))
    op.add_column('tracked_messages', sa.Column('sender_id', sa.Integer(), nullable=True))
    op.drop_constraint('tracked_messages_user_id_fkey', 'tracked_messages', type_='foreignkey')
    op.create_foreign_key(None, 'tracked_messages', 'user', ['recipient_id'], ['id'])
    op.create_foreign_key(None, 'tracked_messages', 'user', ['sender_id'], ['id'])
    op.drop_column('tracked_messages', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracked_messages', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tracked_messages', type_='foreignkey')
    op.drop_constraint(None, 'tracked_messages', type_='foreignkey')
    op.create_foreign_key('tracked_messages_user_id_fkey', 'tracked_messages', 'user', ['user_id'], ['id'])
    op.drop_column('tracked_messages', 'sender_id')
    op.drop_column('tracked_messages', 'recipient_id')
    # ### end Alembic commands ###

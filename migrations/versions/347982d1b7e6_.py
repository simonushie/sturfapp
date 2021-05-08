"""empty message

Revision ID: 347982d1b7e6
Revises: 9868727f0643
Create Date: 2021-01-30 08:33:14.001354

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '347982d1b7e6'
down_revision = '9868727f0643'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roomie_request', sa.Column('request_sender_id', sa.Integer(), nullable=True))
    op.add_column('roomie_request', sa.Column('requested_user_id', sa.Integer(), nullable=True))
    op.drop_index('ix_roomie_request_timestamp', table_name='roomie_request')
    op.drop_constraint('roomie_request_sender_id_fkey', 'roomie_request', type_='foreignkey')
    op.drop_constraint('roomie_request_recipient_id_fkey', 'roomie_request', type_='foreignkey')
    op.create_foreign_key(None, 'roomie_request', 'user', ['request_sender_id'], ['id'])
    op.create_foreign_key(None, 'roomie_request', 'user', ['requested_user_id'], ['id'])
    op.drop_column('roomie_request', 'sender_id')
    op.drop_column('roomie_request', 'body')
    op.drop_column('roomie_request', 'recipient_id')
    op.drop_column('roomie_request', 'timestamp')
    op.drop_column('roomie_request', 'id')
    op.add_column('roomies', sa.Column('roomie_followed', sa.Integer(), nullable=True))
    op.add_column('roomies', sa.Column('roomie_follower', sa.Integer(), nullable=True))
    op.drop_constraint('roomies_request_sender_id_fkey', 'roomies', type_='foreignkey')
    op.drop_constraint('roomies_requested_user_id_fkey', 'roomies', type_='foreignkey')
    op.create_foreign_key(None, 'roomies', 'user', ['roomie_follower'], ['id'])
    op.create_foreign_key(None, 'roomies', 'user', ['roomie_followed'], ['id'])
    op.drop_column('roomies', 'request_sender_id')
    op.drop_column('roomies', 'requested_user_id')
    op.drop_column('user', 'last_RoomieRequest_read_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_RoomieRequest_read_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('roomies', sa.Column('requested_user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('roomies', sa.Column('request_sender_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'roomies', type_='foreignkey')
    op.drop_constraint(None, 'roomies', type_='foreignkey')
    op.create_foreign_key('roomies_requested_user_id_fkey', 'roomies', 'user', ['requested_user_id'], ['id'])
    op.create_foreign_key('roomies_request_sender_id_fkey', 'roomies', 'user', ['request_sender_id'], ['id'])
    op.drop_column('roomies', 'roomie_follower')
    op.drop_column('roomies', 'roomie_followed')
    op.add_column('roomie_request', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('roomie_request', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('roomie_request', sa.Column('recipient_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('roomie_request', sa.Column('body', sa.VARCHAR(length=140), autoincrement=False, nullable=True))
    op.add_column('roomie_request', sa.Column('sender_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'roomie_request', type_='foreignkey')
    op.drop_constraint(None, 'roomie_request', type_='foreignkey')
    op.create_foreign_key('roomie_request_recipient_id_fkey', 'roomie_request', 'user', ['recipient_id'], ['id'])
    op.create_foreign_key('roomie_request_sender_id_fkey', 'roomie_request', 'user', ['sender_id'], ['id'])
    op.create_index('ix_roomie_request_timestamp', 'roomie_request', ['timestamp'], unique=False)
    op.drop_column('roomie_request', 'requested_user_id')
    op.drop_column('roomie_request', 'request_sender_id')
    # ### end Alembic commands ###

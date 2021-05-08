"""empty message

Revision ID: 44621b8cade0
Revises: 38c1025b32d9
Create Date: 2021-02-04 08:16:12.699179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44621b8cade0'
down_revision = '38c1025b32d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('specific__message__read__time', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('specific__message__read__time', 'message_sender_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('specific__message__read__time', 'message_sender_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('specific__message__read__time', 'id')
    # ### end Alembic commands ###

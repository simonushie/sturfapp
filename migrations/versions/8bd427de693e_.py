"""empty message

Revision ID: 8bd427de693e
Revises: a5fc14112c11
Create Date: 2021-03-07 11:49:20.702819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bd427de693e'
down_revision = 'a5fc14112c11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('allows_email_to_be_seen', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('allows_phone_number_to_be_seen', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'allows_phone_number_to_be_seen')
    op.drop_column('user', 'allows_email_to_be_seen')
    # ### end Alembic commands ###

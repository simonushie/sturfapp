"""empty message

Revision ID: da9528539910
Revises: 190a53352ef1
Create Date: 2021-02-13 10:41:25.671026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da9528539910'
down_revision = '190a53352ef1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_viewers',
    sa.Column('viewer_id', sa.Integer(), nullable=True),
    sa.Column('viewed_post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['viewed_post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['viewer_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_viewers')
    # ### end Alembic commands ###
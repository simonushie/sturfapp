"""empty message

Revision ID: 278f7a4c12a4
Revises: cbfe0269b5c0
Create Date: 2021-02-10 11:29:41.705144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '278f7a4c12a4'
down_revision = 'cbfe0269b5c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cameras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('make', sa.String(length=1500), nullable=False),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('computer__accessories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('computer__software',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=True),
    sa.Column('format', sa.String(length=1500), nullable=True),
    sa.Column('platform', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('laptops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('storage_capacity', sa.String(length=1500), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('ram', sa.String(length=1500), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('subtype', sa.String(length=1500), nullable=True),
    sa.Column('processor', sa.String(length=1500), nullable=True),
    sa.Column('number_of_cores', sa.String(length=1500), nullable=True),
    sa.Column('graphics_card', sa.String(length=1500), nullable=True),
    sa.Column('graphics_card_memory', sa.String(length=1500), nullable=True),
    sa.Column('storage_type', sa.String(length=1500), nullable=True),
    sa.Column('operating_system', sa.String(length=1500), nullable=True),
    sa.Column('screen_size', sa.String(length=1500), nullable=True),
    sa.Column('camera', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mobile__accessories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('colour', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('music__equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video__games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('platform', sa.String(length=1500), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('phones', 'address')
    op.drop_column('tablets', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tablets', sa.Column('address', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('phones', sa.Column('address', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_table('video__games')
    op.drop_table('music__equipment')
    op.drop_table('mobile__accessories')
    op.drop_table('laptops')
    op.drop_table('computer__software')
    op.drop_table('computer__accessories')
    op.drop_table('cameras')
    # ### end Alembic commands ###

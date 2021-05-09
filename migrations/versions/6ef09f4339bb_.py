"""empty message

Revision ID: 6ef09f4339bb
Revises: 278f7a4c12a4
Create Date: 2021-02-10 18:46:13.292656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ef09f4339bb'
down_revision = '278f7a4c12a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('gender', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('colour', sa.String(length=1500), nullable=True),
    sa.Column('material', sa.String(length=1500), nullable=True),
    sa.Column('closure', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bath_and_body',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clothing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('gender', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('colour', sa.String(length=1500), nullable=True),
    sa.Column('size', sa.String(length=1500), nullable=True),
    sa.Column('style', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fragrance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('gender', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('formulation', sa.String(length=1500), nullable=False),
    sa.Column('scent', sa.String(length=1500), nullable=False),
    sa.Column('volume', sa.String(length=1500), nullable=False),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hair__weaves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jewelries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('gender', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('colour', sa.String(length=1500), nullable=True),
    sa.Column('main_material', sa.String(length=1500), nullable=True),
    sa.Column('main_stone', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('makeup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('gender', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('colour', sa.String(length=1500), nullable=True),
    sa.Column('tone', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('gender', sa.String(length=1500), nullable=False),
    sa.Column('type', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('brand', sa.String(length=1500), nullable=False),
    sa.Column('colour', sa.String(length=1500), nullable=True),
    sa.Column('size', sa.String(length=1500), nullable=True),
    sa.Column('style', sa.String(length=1500), nullable=True),
    sa.Column('upper_material', sa.String(length=1500), nullable=True),
    sa.Column('outsole_material', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skin__care',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True),
    sa.Column('title', sa.String(length=1500), nullable=False),
    sa.Column('gender', sa.String(length=1500), nullable=False),
    sa.Column('date_of_post', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=1500), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('colour', sa.String(length=1500), nullable=True),
    sa.Column('type', sa.String(length=1500), nullable=True),
    sa.Column('target_area', sa.String(length=1500), nullable=True),
    sa.Column('skin_type', sa.String(length=1500), nullable=True),
    sa.Column('benefits', sa.String(length=1500), nullable=True),
    sa.Column('ad_type', sa.String(length=1500), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('cameras', sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True))
    op.add_column('computer__accessories', sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True))
    op.add_column('computer__software', sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True))
    op.add_column('mobile__accessories', sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True))
    op.add_column('music__equipment', sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True))
    op.add_column('video__games', sa.Column('image_files', sa.ARRAY(sa.String(length=1500)), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video__games', 'image_files')
    op.drop_column('music__equipment', 'image_files')
    op.drop_column('mobile__accessories', 'image_files')
    op.drop_column('computer__software', 'image_files')
    op.drop_column('computer__accessories', 'image_files')
    op.drop_column('cameras', 'image_files')
    op.drop_table('skin__care')
    op.drop_table('shoes')
    op.drop_table('makeup')
    op.drop_table('jewelries')
    op.drop_table('hair__weaves')
    op.drop_table('fragrance')
    op.drop_table('clothing')
    op.drop_table('bath_and_body')
    op.drop_table('bags')
    # ### end Alembic commands ###
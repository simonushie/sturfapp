"""empty message

Revision ID: 00d1fca1fbed
Revises: c229438f638f
Create Date: 2021-02-11 13:31:37.420503

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '00d1fca1fbed'
down_revision = 'c229438f638f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('E_commerce')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('E_commerce',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"E_commerce_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('image_file', postgresql.ARRAY(sa.VARCHAR(length=1500)), autoincrement=False, nullable=True),
    sa.Column('date_of_post', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('brand', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('condition', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('ram', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('screen_size', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('colour', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('camera', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('storage_capacity', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('subtype', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('processor', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('number_of_cores', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('graphics_card', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('graphics_card_memory', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('storage_type', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('operating_system', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('make', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('platform', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('format', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('size', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('style', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('upper_material', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('outsole_material', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('material', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('closure', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('main_material', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('main_stone', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('formulation', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('scent', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('volume', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('tone', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('target_area', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('skin_type', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('benefits', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('level', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('duration', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('service_features', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('round_the_clock_service', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('type_of_service', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('service_include', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('year_of_manufacture', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('transmission', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('mileage', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('ad_type', sa.VARCHAR(length=1500), autoincrement=False, nullable=True),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], name='E_commerce_author_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='E_commerce_pkey')
    )
    # ### end Alembic commands ###

"""Init

Revision ID: 81573e47e9f8
Revises: 
Create Date: 2024-08-31 14:54:12.220691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81573e47e9f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('zip_code', sa.String(), nullable=False),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_city'), 'address', ['city'], unique=False)
    op.create_index(op.f('ix_address_country'), 'address', ['country'], unique=False)
    op.create_index(op.f('ix_address_id'), 'address', ['id'], unique=False)
    op.create_index(op.f('ix_address_latitude'), 'address', ['latitude'], unique=False)
    op.create_index(op.f('ix_address_longitude'), 'address', ['longitude'], unique=False)
    op.create_index(op.f('ix_address_number'), 'address', ['number'], unique=False)
    op.create_index(op.f('ix_address_state'), 'address', ['state'], unique=False)
    op.create_index(op.f('ix_address_street'), 'address', ['street'], unique=False)
    op.create_index(op.f('ix_address_zip_code'), 'address', ['zip_code'], unique=False)
    op.create_table('fuel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False, comment='Price per liter'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fuel_id'), 'fuel', ['id'], unique=False)
    op.create_index(op.f('ix_fuel_type'), 'fuel', ['type'], unique=True)
    op.create_table('industry',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_industry_id'), 'industry', ['id'], unique=False)
    op.create_index(op.f('ix_industry_name'), 'industry', ['name'], unique=True)
    op.create_table('truck',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('max_tons', sa.Integer(), nullable=False, comment='Maximum tons'),
    sa.Column('axles', sa.Integer(), nullable=False, comment='Number of axles'),
    sa.Column('km_per_fuel', sa.Float(), nullable=False, comment='Kilometers per fuel'),
    sa.Column('fuel_id', sa.Integer(), nullable=False, comment='Fuel type'),
    sa.ForeignKeyConstraint(['fuel_id'], ['fuel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_truck_id'), 'truck', ['id'], unique=False)
    op.create_index(op.f('ix_truck_name'), 'truck', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_truck_name'), table_name='truck')
    op.drop_index(op.f('ix_truck_id'), table_name='truck')
    op.drop_table('truck')
    op.drop_index(op.f('ix_industry_name'), table_name='industry')
    op.drop_index(op.f('ix_industry_id'), table_name='industry')
    op.drop_table('industry')
    op.drop_index(op.f('ix_fuel_type'), table_name='fuel')
    op.drop_index(op.f('ix_fuel_id'), table_name='fuel')
    op.drop_table('fuel')
    op.drop_index(op.f('ix_address_zip_code'), table_name='address')
    op.drop_index(op.f('ix_address_street'), table_name='address')
    op.drop_index(op.f('ix_address_state'), table_name='address')
    op.drop_index(op.f('ix_address_number'), table_name='address')
    op.drop_index(op.f('ix_address_longitude'), table_name='address')
    op.drop_index(op.f('ix_address_latitude'), table_name='address')
    op.drop_index(op.f('ix_address_id'), table_name='address')
    op.drop_index(op.f('ix_address_country'), table_name='address')
    op.drop_index(op.f('ix_address_city'), table_name='address')
    op.drop_table('address')
    # ### end Alembic commands ###

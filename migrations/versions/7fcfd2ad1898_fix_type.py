"""fix type

Revision ID: 7fcfd2ad1898
Revises: 6b34b5b20bc6
Create Date: 2024-09-09 18:40:03.724817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fcfd2ad1898'
down_revision: Union[str, None] = '6b34b5b20bc6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('industry', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_comment='Price per ton',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('industry', 'price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_comment='Price per ton',
               existing_nullable=False)
    # ### end Alembic commands ###

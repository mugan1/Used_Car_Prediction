"""empty message

Revision ID: a6088cf65748
Revises: 7bd2cd16dda7
Create Date: 2022-12-18 15:35:13.663284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6088cf65748'
down_revision = '7bd2cd16dda7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('input', sa.Column('price', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('input', 'price')
    # ### end Alembic commands ###

"""empty message

Revision ID: 7bd2cd16dda7
Revises: e9750667ead4
Create Date: 2022-12-18 15:30:20.768673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bd2cd16dda7'
down_revision = 'e9750667ead4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    op.add_column('input', sa.Column('price', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('input', 'price')
    op.create_table('car',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.Column('year', sa.INTEGER(), nullable=True),
    sa.Column('km', sa.INTEGER(), nullable=True),
    sa.Column('fuel', sa.VARCHAR(length=64), nullable=True),
    sa.Column('amount', sa.INTEGER(), nullable=True),
    sa.Column('ratio', sa.FLOAT(), nullable=True),
    sa.Column('drive', sa.VARCHAR(length=64), nullable=True),
    sa.Column('torque', sa.FLOAT(), nullable=True),
    sa.Column('insurance', sa.VARCHAR(length=64), nullable=True),
    sa.Column('factory', sa.VARCHAR(length=64), nullable=True),
    sa.Column('horse', sa.FLOAT(), nullable=True),
    sa.Column('guarantee', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='CAR_PK')
    )
    # ### end Alembic commands ###
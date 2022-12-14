"""empty message

Revision ID: 0607991b1306
Revises: 
Create Date: 2022-12-14 23:00:16.424984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0607991b1306'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('input',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('km', sa.Integer(), nullable=False),
    sa.Column('fuel', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('ratio', sa.Float(), nullable=False),
    sa.Column('drive', sa.Integer(), nullable=False),
    sa.Column('torque', sa.Float(), nullable=False),
    sa.Column('insurance', sa.Integer(), nullable=False),
    sa.Column('factory', sa.Integer(), nullable=False),
    sa.Column('horse', sa.Float(), nullable=False),
    sa.Column('guarantee', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('input')
    # ### end Alembic commands ###

"""empty message

Revision ID: d23a07f3fdfd
Revises: 3ce27b9d43cc
Create Date: 2024-01-31 20:01:30.026378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd23a07f3fdfd'
down_revision = '3ce27b9d43cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=False),
    sa.Column('starship_class', sa.String(length=250), nullable=False),
    sa.Column('manufacturer', sa.String(length=250), nullable=False),
    sa.Column('length', sa.String(length=250), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=250), nullable=False),
    sa.Column('crew', sa.String(length=250), nullable=False),
    sa.Column('passengers', sa.String(length=250), nullable=False),
    sa.Column('max_atmosphering_speed', sa.String(length=250), nullable=False),
    sa.Column('hiper_drive_rating', sa.String(length=250), nullable=False),
    sa.Column('MGLT', sa.String(length=250), nullable=False),
    sa.Column('cargo_capacity', sa.String(length=250), nullable=False),
    sa.Column('consumables', sa.String(length=250), nullable=False),
    sa.Column('created', sa.String(length=250), nullable=False),
    sa.Column('edited', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starships')
    # ### end Alembic commands ###
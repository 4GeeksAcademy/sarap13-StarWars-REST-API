"""empty message

Revision ID: 70c268903874
Revises: 94f6817a6071
Create Date: 2024-01-31 19:39:27.488119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70c268903874'
down_revision = '94f6817a6071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('classification', sa.String(length=250), nullable=False),
    sa.Column('designation', sa.String(length=250), nullable=False),
    sa.Column('average_heigth', sa.String(length=250), nullable=False),
    sa.Column('average_lifespan', sa.String(length=250), nullable=False),
    sa.Column('eye_colors', sa.String(length=250), nullable=False),
    sa.Column('hair_colors', sa.String(length=250), nullable=False),
    sa.Column('skin_colors', sa.String(length=250), nullable=False),
    sa.Column('language', sa.String(length=250), nullable=False),
    sa.Column('homeworld', sa.String(length=250), nullable=False),
    sa.Column('created', sa.String(length=250), nullable=False),
    sa.Column('edited', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_species', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('id_vehicles', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'species', ['id_species'], ['id'])
        batch_op.create_foreign_key(None, 'vehicles', ['id_vehicles'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id_vehicles')
        batch_op.drop_column('id_species')

    op.drop_table('species')
    # ### end Alembic commands ###

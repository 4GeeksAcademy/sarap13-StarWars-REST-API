"""empty message

Revision ID: 575cd79047dc
Revises: 2367f32dd383
Create Date: 2024-01-31 20:43:07.407000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '575cd79047dc'
down_revision = '2367f32dd383'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_constraint('vehicles_id_people_fkey', type_='foreignkey')
        batch_op.drop_column('id_people')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_people', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('vehicles_id_people_fkey', 'people', ['id_people'], ['id'])

    # ### end Alembic commands ###
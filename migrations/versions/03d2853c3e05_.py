"""empty message

Revision ID: 03d2853c3e05
Revises: 1a4f54cf5353
Create Date: 2021-01-25 23:09:32.099238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03d2853c3e05'
down_revision = '1a4f54cf5353'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('weatherdata_user_defined_id_key', 'weatherdata', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('weatherdata_user_defined_id_key', 'weatherdata', ['user_defined_id'])
    # ### end Alembic commands ###

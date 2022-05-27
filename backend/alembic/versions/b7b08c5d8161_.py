"""empty message

Revision ID: b7b08c5d8161
Revises: 8c7a95cc1e42
Create Date: 2022-05-27 22:19:22.677865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7b08c5d8161'
down_revision = '8c7a95cc1e42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sport')
    op.drop_column('users', 'lieux')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lieux', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('sport', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

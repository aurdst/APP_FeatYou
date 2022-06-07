"""empty message

Revision ID: d38df8b8d954
Revises: f98a3859595f
Create Date: 2022-06-07 11:07:28.719705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd38df8b8d954'
down_revision = 'f98a3859595f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('sport', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'sport')
    # ### end Alembic commands ###

"""empty message

Revision ID: d0cf9637c1f7
Revises: None
Create Date: 2017-11-08 23:30:33.771582

"""

# revision identifiers, used by Alembic.
revision = 'd0cf9637c1f7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('content_items')
    # ### end Alembic commands ###

"""Create tables owners, pets

Revision ID: 49ca9fa1eeec
Revises: 
Create Date: 2023-09-02 20:36:00.950151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ca9fa1eeec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name=op.f('fk_pets_owner_id_owners')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    op.drop_table('owners')
    # ### end Alembic commands ###

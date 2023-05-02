"""init

Revision ID: 08014d3a56e8
Revises: 
Create Date: 2023-05-02 13:56:07.458696

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '08014d3a56e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drink',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=30), nullable=True),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drink_description'), 'drink', ['description'], unique=False)
    op.create_index(op.f('ix_drink_id'), 'drink', ['id'], unique=False)
    op.create_index(op.f('ix_drink_name'), 'drink', ['name'], unique=False)
    op.create_index(op.f('ix_drink_price'), 'drink', ['price'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_drink_price'), table_name='drink')
    op.drop_index(op.f('ix_drink_name'), table_name='drink')
    op.drop_index(op.f('ix_drink_id'), table_name='drink')
    op.drop_index(op.f('ix_drink_description'), table_name='drink')
    op.drop_table('drink')
    # ### end Alembic commands ###
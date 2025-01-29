"""empty message

Revision ID: 0759a97f0cfa
Revises: c0c24dfe4dae
Create Date: 2025-01-29 00:14:02.889348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0759a97f0cfa'
down_revision = 'c0c24dfe4dae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('password_hash', sa.String(), nullable=False))
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('password_hash')
        batch_op.drop_column('username')

    # ### end Alembic commands ###

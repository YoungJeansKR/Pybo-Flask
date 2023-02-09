"""empty message

Revision ID: 5b320a028109
Revises: 1d7b5801a8dd
Create Date: 2023-02-07 14:15:31.164028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b320a028109'
down_revision = '1d7b5801a8dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###

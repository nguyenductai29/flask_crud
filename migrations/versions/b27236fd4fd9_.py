"""empty message

Revision ID: b27236fd4fd9
Revises:
Create Date: 2023-06-19 11:41:52.199461

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b27236fd4fd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mst_tbl_product')
    op.drop_table('tbl_order_detail')
    op.drop_table('tbl_order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_order',
    sa.Column('order_no', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('category_code', sa.VARCHAR(length=3), autoincrement=False, nullable=False),
    sa.Column('order_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('order_no', name='tbl_order_pkey')
    )
    op.create_table('tbl_order_detail',
    sa.Column('order_detail_no', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_no', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_code', sa.VARCHAR(length=6), autoincrement=False, nullable=True),
    sa.Column('order_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_delete', postgresql.BIT(length=1), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('updated_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('order_detail_no', name='tbl_order_detail_pkey')
    )
    op.create_table('mst_tbl_product',
    sa.Column('product_code', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('category_code', sa.VARCHAR(length=3), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_delete', postgresql.BIT(length=1), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('updated_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('product_code', name='mst_tbl_product_pkey')
    )
    # ### end Alembic commands ###

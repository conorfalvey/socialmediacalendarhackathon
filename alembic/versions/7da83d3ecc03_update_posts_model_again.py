"""Update posts model again

Revision ID: 7da83d3ecc03
Revises: 153e024d4084
Create Date: 2023-02-23 18:39:48.880384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7da83d3ecc03"
down_revision = "153e024d4084"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("posts", "delivery_time")
    op.add_column("posts", sa.Column("delivery_time", sa.String(), nullable=False))
    op.add_column("posts", sa.Column("post_hash", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("posts", "post_hash")
    op.drop_column("posts", "delivery_time")
    op.add_column(
        "posts", sa.Column("delivery_time", sa.DateTime(timezone=False), nullable=False)
    )
    # ### end Alembic commands ###

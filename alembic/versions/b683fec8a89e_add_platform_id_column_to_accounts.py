"""Add platform id column to accounts

Revision ID: b683fec8a89e
Revises: 7da83d3ecc03
Create Date: 2023-02-23 22:03:37.016978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b683fec8a89e"
down_revision = "7da83d3ecc03"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("accounts", sa.Column("platform_id", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("accounts", "platform_id")
    # ### end Alembic commands ###
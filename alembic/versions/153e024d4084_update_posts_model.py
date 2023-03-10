"""Update posts model

Revision ID: 153e024d4084
Revises: 59c0ad4f6c43
Create Date: 2023-02-23 18:35:09.401250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "153e024d4084"
down_revision = "59c0ad4f6c43"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("posts", sa.Column("platform_id", sa.UUID(), nullable=False))
    op.add_column("posts", sa.Column("user_id", sa.UUID(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("posts", "user_id")
    op.drop_column("posts", "platform_id")
    # ### end Alembic commands ###

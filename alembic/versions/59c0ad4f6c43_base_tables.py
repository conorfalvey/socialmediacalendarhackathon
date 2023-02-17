"""Base tables

Revision ID: 59c0ad4f6c43
Revises:
Create Date: 2023-02-16 21:01:32.593748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "59c0ad4f6c43"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accounts",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("token", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "platforms",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("char_limit", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "posts",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("delivery_time", sa.DateTime(), nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.Column("frequency", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("pass_hash", sa.String(), nullable=False),
        sa.Column("notification_time", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_table("posts")
    op.drop_table("platforms")
    op.drop_table("accounts")
    # ### end Alembic commands ###

"""D65 initial schema migration

Crea la tabla dimensional `dim_customer` como parte del esquema base
del microservicio de migraciones automatizadas.

Revision ID: 94d6ae5879b9
Revises:
Create Date: 2026-03-15 00:00:00.000000
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# --- Identificadores de revisión requeridos por Alembic ---
revision: str = "94d6ae5879b9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Aplica el cambio de esquema: crea la tabla dim_customer."""
    op.create_table(
        "dim_customer",
        sa.Column("customer_id", sa.Integer(), nullable=False),
        sa.Column("customer_name", sa.String(), nullable=False),
        sa.Column("country", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("customer_id"),
    )
    op.create_index(
        op.f("ix_dim_customer_customer_id"),
        "dim_customer",
        ["customer_id"],
        unique=False,
    )


def downgrade() -> None:
    """Revierte el cambio de esquema: elimina la tabla dim_customer."""
    op.drop_index(op.f("ix_dim_customer_customer_id"), table_name="dim_customer")
    op.drop_table("dim_customer")
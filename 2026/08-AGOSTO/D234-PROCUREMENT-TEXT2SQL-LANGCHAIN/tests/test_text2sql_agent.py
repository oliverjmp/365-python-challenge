"""Pruebas unitarias para validar la lógica del motor DuckDB y el parser de SQL."""

import pytest
from unittest.mock import MagicMock, patch
from src.database_engine import ProcurementDatabaseManager
from src.text2sql_agent import ProcurementText2SQLAgent


@pytest.fixture
def db_manager():
    return ProcurementDatabaseManager(record_count=1000)


def test_database_seeding(db_manager):
    df = db_manager.execute_query("SELECT COUNT(*) as total FROM purchase_orders;")
    assert df["total"].iloc[0] == 1000


def test_sql_security_guardrails(db_manager):
    with pytest.raises(ValueError, match="Seguridad SQL: Operación restringida"):
        db_manager.execute_query("DROP TABLE purchase_orders;")


def test_sql_cleaning_formatting():
    raw_llm_output = "```sql\nSELECT category, SUM(total_amount) FROM purchase_orders GROUP BY 1;\n```"
    cleaned = ProcurementText2SQLAgent._extract_sql_from_response(raw_llm_output)
    assert cleaned == "SELECT category, SUM(total_amount) FROM purchase_orders GROUP BY 1;"
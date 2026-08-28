import pandas as pd
import pytest
from src.anonymizer import DuckDBAnonymizer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "id": [1, 2],
        "nombre": ["Carlos Pérez", "Ana Gómez"],
        "tarjeta_credito": ["1234-5678-9876-5432", "9876-5432-1234-8765"],
        "email": ["carlos.perez@empresa.com", "ana.gomez@empresa.com"],
        "pais": ["España", "México"],
        "monto": [150.50, 300.00]
    })

def test_anonymizer_pipeline(sample_data):
    anonymizer = DuckDBAnonymizer()
    anonymizer.load_dataframe_as_table(sample_data, "clientes")
    
    result_df = anonymizer.anonymize_pii("clientes")
    
    assert len(result_df) == 2
    assert result_df.iloc[0]["nombre_anonimo"] == "C***"
    assert result_df.iloc[0]["tarjeta_anonima"] == "****-****-****-5432"
    assert len(result_df.iloc[0]["email_hash"]) == 64  # SHA256 hex length
    
    anonymizer.close()
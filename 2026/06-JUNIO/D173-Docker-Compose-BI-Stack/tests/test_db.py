from unittest.mock import patch
import pandas as pd
from src.db_connector import get_database_url, fetch_bi_data
from unittest.mock import patch
import pandas as pd
from src.db_connector import fetch_bi_data

def test_get_database_url():
    url = get_database_url()
    assert "postgresql://" in url

@patch("src.db_connector.create_engine")
def test_fetch_bi_data_exception(mock_create_engine):
    # Simular un error de conexión para probar la robustez del conector
    mock_create_engine.side_effect = Exception("Connection refused")
    df = fetch_bi_data("SELECT * FROM dummy")
    assert isinstance(df, pd.DataFrame)
    assert df.empty is True



@patch("src.db_connector.create_engine")
def test_fetch_bi_data_success(mock_create_engine):
    # Mockear el motor, la conexión y la ejecución de pd.read_sql
    mock_conn = mock_create_engine.return_value.connect.return_value.__enter__.return_value
    
    with patch("pandas.read_sql", return_value=pd.DataFrame({"id": [1], "metric": ["test"]})):
        df = fetch_bi_data("SELECT * FROM kpis_operativos")
        assert not df.empty
        assert df.iloc[0]["id"] == 1
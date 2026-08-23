import pandas as pd
from models.database import fetch_data_from_db

def load_kpi_data(query: str) -> tuple[pd.DataFrame, bool]:
    """Controla la obtención de datos y verifica si la consulta fue exitosa."""
    df = fetch_data_from_db(query)
    if not df.empty:
        return df, True
    return pd.DataFrame(), False
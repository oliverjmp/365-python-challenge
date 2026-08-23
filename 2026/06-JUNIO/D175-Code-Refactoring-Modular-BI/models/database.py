import os
import pandas as pd
from sqlalchemy import create_engine, text

def get_database_url() -> str:
    """Construye la URL de conexión a PostgreSQL usando variables de entorno."""
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "postgres_db")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "bi_database")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"

def fetch_data_from_db(query: str) -> pd.DataFrame:
    """Ejecuta la consulta SQL y retorna los datos en un DataFrame."""
    try:
        engine = create_engine(get_database_url())
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
        return df
    except Exception:
        return pd.DataFrame()
import os
import pandas as pd
from sqlalchemy import create_engine, text

def get_database_url() -> str:
    """
    Construye la URL de conexión a PostgreSQL usando variables de entorno o valores por defecto.
    """
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "postgres_db")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "bi_database")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"

def fetch_bi_data(query: str = "SELECT 1 AS id, 'sample' AS metric") -> pd.DataFrame:
    """
    Ejecuta una consulta SQL en PostgreSQL y retorna los resultados como un DataFrame de Pandas.
    """
    try:
        engine = create_engine(get_database_url())
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
        return df
    except Exception as e:
        # Retorna un DataFrame vacío en caso de fallo de conexión para la resiliencia de la app
        return pd.DataFrame()
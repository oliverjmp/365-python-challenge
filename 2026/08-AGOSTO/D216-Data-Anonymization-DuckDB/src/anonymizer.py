import duckdb
import pandas as pd
import pyarrow as pa

class DuckDBAnonymizer:
    """Motor de anonimización y enmascaramiento de datos PII utilizando DuckDB SQL."""
    
    def __init__(self, db_path: str = ":memory:"):
        self.conn = duckdb.connect(db_path)

    def load_dataframe_as_table(self, df: pd.DataFrame, table_name: str = "raw_data"):
        # Convertimos el DataFrame a Arrow Table para evitar conflictos de tipos con DuckDB
        arrow_table = pa.Table.from_pandas(df)
        self.conn.register("temp_df", arrow_table)
        self.conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM temp_df")

    def anonymize_pii(self, source_table: str = "raw_data") -> pd.DataFrame:
        """Aplica técnicas SQL de enmascaramiento: hash de emails, enmascaramiento de tarjetas y truncado de nombres."""
        query = f"""
            SELECT 
                id,
                -- Enmascarar nombre mostrando solo la inicial
                SUBSTR(nombre, 1, 1) || '***' AS nombre_anonimo,
                -- Enmascarar tarjeta de crédito mostrando solo los últimos 4 dígitos
                '****-****-****-' || RIGHT(tarjeta_credito, 4) AS tarjeta_anonima,
                -- Hash SHA256 para el correo electrónico preservando unicidad sin revelar PII
                SHA256(LOWER(TRIM(email))) AS email_hash,
                pais,
                monto
            FROM {source_table}
        """
        return self.conn.execute(query).fetchdf()

    def close(self):
        self.conn.close()
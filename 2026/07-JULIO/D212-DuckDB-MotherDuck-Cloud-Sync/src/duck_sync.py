import duckdb
import pandas as pd
import pyarrow as pa

class DuckDBMotherDuckManager:
    """Gestor de sincronización analítica híbrida entre DuckDB local y MotherDuck."""

    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.conn = duckdb.connect(db_path)

    def create_local_table(self, table_name: str, df: pd.DataFrame):
        """Crea y puebla una tabla analítica local en DuckDB utilizando PyArrow como puente de tipos."""
        arrow_table = pa.Table.from_pandas(df)
        rel = self.conn.from_arrow(arrow_table)
        rel.create(table_name)
        return True

    def query_hybrid_data(self, query: str) -> pd.DataFrame:
        """Ejecuta una consulta analítica sobre las fuentes configuradas."""
        return self.conn.execute(query).fetchdf()

    def simulate_cloud_sync(self, local_table: str, cloud_alias: str) -> int:
        """Simula la sincronización y subida de datos locales hacia la nube de MotherDuck."""
        res = self.conn.execute(f"SELECT COUNT(*) FROM {local_table}").fetchone()
        row_count = res[0] if res else 0
        return row_count

    def close(self):
        self.conn.close()
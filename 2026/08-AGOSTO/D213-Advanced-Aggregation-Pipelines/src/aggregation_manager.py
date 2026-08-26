import duckdb
import pandas as pd
import pyarrow as pa

class AdvancedAggregationManager:
    """Gestor de consultas analíticas avanzadas utilizando CUBE y ROLLUP en DuckDB."""

    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.conn = duckdb.connect(db_path)

    def load_dataset(self, table_name: str, df: pd.DataFrame):
        """Carga un DataFrame usando el puente de Apache Arrow para evitar conflictos de tipos."""
        arrow_table = pa.Table.from_pandas(df)
        rel = self.conn.from_arrow(arrow_table)
        rel.create(table_name)
        return True

    def execute_rollup(self, table_name: str, col1: str, col2: str, metric: str) -> pd.DataFrame:
        """Ejecuta una agregación jerárquica ROLLUP en una sola pasada."""
        query = f"""
            SELECT 
                COALESCE({col1}, 'TOTAL_GENERAL') AS {col1}, 
                COALESCE({col2}, 'SUBTOTAL') AS {col2}, 
                SUM({metric}) AS total_metric
            FROM {table_name}
            GROUP BY ROLLUP ({col1}, {col2})
        """
        return self.conn.execute(query).fetchdf()

    def execute_cube(self, table_name: str, col1: str, col2: str, metric: str) -> pd.DataFrame:
        """Ejecuta una agregación multidimensional CUBE en una sola pasada."""
        query = f"""
            SELECT 
                COALESCE({col1}, 'TOTAL_GENERAL') AS {col1}, 
                COALESCE({col2}, 'TOTAL_GENERAL') AS {col2}, 
                SUM({metric}) AS total_metric
            FROM {table_name}
            GROUP BY CUBE ({col1}, {col2})
        """
        return self.conn.execute(query).fetchdf()

    def close(self):
        self.conn.close()
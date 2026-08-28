import duckdb
import pandas as pd
import pyarrow as pa

class DataQualityEngine:
    """Motor enterprise de validación de calidad y restricciones (Constraints) usando DuckDB."""

    def __init__(self, db_path: str = ":memory:"):
        self.conn = duckdb.connect(db_path)

    def create_validated_table(self, df: pd.DataFrame, table_name: str = "validated_transactions"):
        """Crea una tabla en DuckDB aplicando restricciones estrictas de dominio y negocio (Constraints)."""
        arrow_table = pa.Table.from_pandas(df)
        self.conn.register("temp_raw", arrow_table)
        
        # Creamos la tabla aplicando restricciones nativas de integridad SQL
        query = f"""
            CREATE TABLE {table_name} (
                transaction_id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                amount DECIMAL(12,2) CHECK (amount > 0.0),
                status VARCHAR CHECK (status IN ('COMPLETED', 'PENDING', 'FAILED')),
                event_date DATE NOT NULL
            );
        """
        self.conn.execute(query)
        
        # Insertar datos válidos; los que incumplan constraints lanzarán excepciones controladas
        self.conn.execute(f"INSERT INTO {table_name} SELECT * FROM temp_raw;")

    def run_data_assertions(self, table_name: str = "validated_transactions") -> dict:
        """Ejecuta un conjunto de aserciones de calidad analítica sobre el dataset."""
        metrics = {}
        
        # 1. Test de nulidad en columnas críticas
        null_counts = self.conn.execute(f"""
            SELECT 
                COUNT(*) FILTER (WHERE customer_id IS NULL) AS null_customers,
                COUNT(*) FILTER (WHERE amount IS NULL) AS null_amounts
            FROM {table_name}
        ​""").fetchone()
        
        metrics["null_customers"] = null_counts[0]
        metrics["null_amounts"] = null_counts[1]
        
        # 2. Test de valores atípicos (Anomalías de negocio)
        outliers = self.conn.execute(f"""
            SELECT COUNT(*) FROM {table_name} WHERE amount > 50000.00
        """).fetchone()
        metrics["high_amount_outliers"] = outliers[0]
        
        # 3. Total de registros validados correctamente
        total_rows = self.conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
        metrics["total_valid_rows"] = total_rows[0]
        
        return metrics

    def close(self):
        self.conn.close()
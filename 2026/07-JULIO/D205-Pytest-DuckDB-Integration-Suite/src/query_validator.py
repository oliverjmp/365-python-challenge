import duckdb
import pandas as pd

class QueryValidator:
    """Validador de consultas analíticas avanzadas utilizando DuckDB in-memory."""

    def __init__(self, db_conn: duckdb.DuckDBPyConnection):
        self.conn = db_conn

    def calcular_total_por_estado(self) -> list:
        """Calcula la suma de montos y totales agrupados por estado de transacción."""
        query = """
            SELECT 
                estado,
                COUNT(*) as total_transacciones,
                ROUND(SUM(monto), 2) as monto_acumulado,
                ROUND(AVG(monto), 2) as monto_promedio
            FROM transactions
            GROUP BY estado
            ORDER BY monto_acumulado DESC;
        """
        df = self.conn.execute(query).fetchdf()
        return df.to_dict(orient="records")

    def filtrar_por_categoria(self, categoria: str) -> list:
        """Filtra transacciones corporativas por una categoría específica de manera segura."""
        query = """
            SELECT id, categoria, monto, fecha, estado
            FROM transactions
            WHERE LOWER(categoria) = LOWER(?);
        """
        df = self.conn.execute(query, [categoria]).fetchdf()
        return df.to_dict(orient="records")
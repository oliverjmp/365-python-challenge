import duckdb
import pandas as pd
import os

class AnalyticsService:
    """Servicio analítico empresarial que procesa archivos montados en volúmenes usando DuckDB."""

    def __init__(self, data_path: str = "/app/data/source_data.csv"):
        self.data_path = data_path
        self.conn = duckdb.connect(database=":memory:")

    def obtener_resumen(self) -> list:
        """Ejecuta una consulta analítica avanzada agrupando por categoría y región."""
        path_to_use = self.data_path
        if not os.path.exists(path_to_use):
            local_path = "data/source_data.csv"
            if os.path.exists(local_path):
                path_to_use = local_path

        query = f"""
            SELECT 
                categoria,
                region,
                COUNT(*) as total_transacciones,
                ROUND(SUM(monto), 2) as monto_total,
                ROUND(AVG(monto), 2) as monto_promedio
            FROM read_csv_auto('{path_to_use}')
            GROUP BY categoria, region
            ORDER BY monto_total DESC;
        """
        df = self.conn.execute(query).fetchdf()
        return df.to_dict(orient="records")
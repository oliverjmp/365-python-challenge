import duckdb
import pandas as pd

class AnalyticsEngine:
    """Motor analítico optimizado con DuckDB para auditorías corporativas."""

    def __init__(self, conn: duckdb.DuckDBPyConnection):
        self.conn = conn

    def obtener_gasto_por_departamento(self) -> list:
        """Calcula el gasto total y promedio agrupado por departamento."""
        query = """
            SELECT 
                departamento,
                COUNT(*) as total_registros,
                ROUND(SUM(gasto), 2) as gasto_total,
                ROUND(AVG(gasto), 2) as gasto_promedio
            FROM audit_data
            GROUP BY departamento
            ORDER BY gasto_total DESC;
        """
        df = self.conn.execute(query).fetchdf()
        return df.to_dict(orient="records")

    def filtrar_por_estado_aprobacion(self, aprobado: bool) -> list:
        """Filtra registros de auditoría según su estado de aprobación."""
        query = """
            SELECT id, departamento, gasto, fecha, aprobado
            FROM audit_data
            WHERE aprobado = ?;
        """
        df = self.conn.execute(query, [aprobado]).fetchdf()
        return df.to_dict(orient="records")
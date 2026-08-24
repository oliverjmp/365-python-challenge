import pandas as pd
from database import obtener_conexion_readonly

class AnaliticaVentasService:
    """
    Capa de servicio encargada de encapsular la lógica de negocio y
    las consultas analíticas sobre DuckDB en modo Read-Only.
    """

    @staticmethod
    def obtener_todas_las_ventas(limit: int = 10) -> list:
        conn = obtener_conexion_readonly()
        try:
            query = "SELECT * FROM ventas_analiticas LIMIT ?"
            df = conn.execute(query, [limit]).df()
            return df.to_dict(orient="records")
        finally:
            conn.close()

    @staticmethod
    def obtener_resumen_por_departamento() -> list:
        conn = obtener_conexion_readonly()
        try:
            query = """
                SELECT 
                    departamento,
                    SUM(monto) AS total_monto,
                    COUNT(id_transaccion) AS transacciones_count
                FROM ventas_analiticas
                WHERE estado = 'COMPLETADO'
                GROUP BY departamento
                ORDER BY total_monto DESC;
            """
            df = conn.execute(query).df()
            return df.to_dict(orient="records")
        finally:
            conn.close()
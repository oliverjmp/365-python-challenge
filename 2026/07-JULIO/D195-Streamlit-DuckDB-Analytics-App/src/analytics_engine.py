import os
import duckdb
import pandas as pd
from typing import Dict, Any

class DuckDBAnalyticsEngine:
    """Motor analítico de alto rendimiento impulsado por DuckDB para el Data Lake."""
    
    def __init__(self, db_path: str = "data_lake/analytics_warehouse.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._inicializar_almacen()

    def _inicializar_almacen(self):
        """Crea y puebla el almacén analítico con datos de transacciones si está vacío."""
        conn = duckdb.connect(self.db_path)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ventas (
                id_transaccion INTEGER,
                categoria VARCHAR,
                region VARCHAR,
                monto DOUBLE,
                fecha DATE
            );
        """)
        
        count = conn.execute("SELECT COUNT(*) FROM ventas;").fetchone()[0]
        if count == 0:
            conn.execute("""
                INSERT INTO ventas VALUES 
                (1, 'Tecnología', 'Norte', 1200.50, '2026-07-01'),
                (2, 'Hogar', 'Sur', 450.00, '2026-07-01'),
                (3, 'Tecnología', 'Este', 850.75, '2026-07-02'),
                (4, 'Ropa', 'Oeste', 200.00, '2026-07-02'),
                (5, 'Hogar', 'Norte', 620.30, '2026-07-03'),
                (6, 'Tecnología', 'Sur', 1500.00, '2026-07-03');
            """)
        conn.close()

    def ejecutar_consulta_resumen(self) -> pd.DataFrame:
        """Obtiene un resumen de ventas agrupado por categoría."""
        conn = duckdb.connect(self.db_path, read_only=True)
        query = """
            SELECT categoria, COUNT(*) as total_transacciones, SUM(monto) as ventas_totales, AVG(monto) as ticket_promedio
            FROM ventas
            GROUP BY categoria
            ORDER BY ventas_totales DESC;
        """
        df = conn.execute(query).fetchdf()
        conn.close()
        return df

    def obtener_metricas_globales(self) -> Dict[str, Any]:
        """Calcula métricas clave globales del negocio."""
        conn = duckdb.connect(self.db_path, read_only=True)
        res = conn.execute("""
            SELECT COUNT(*), SUM(monto), AVG(monto) FROM ventas;
        """).fetchone()
        conn.close()
        return {
            "total_transacciones": res[0],
            "monto_total": res[1],
            "ticket_promedio": res[2]
        }
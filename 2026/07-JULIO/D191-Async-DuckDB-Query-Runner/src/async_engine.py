import asyncio
import time
import os
import duckdb
from typing import List, Dict, Any

class AsyncDuckDBRunner:
    """Motor para ejecutar consultas analíticas de forma concurrente usando DuckDB persistente en el Data Lake."""
    
    def __init__(self, db_path: str = "data_lake/async_analytics.db"):
        self.db_path = db_path
        
        # Asegurar que la carpeta data_lake exista físicamente
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        # Inicializar y poblar datos físicos si no existen
        self._inicializar_datos_si_no_existen()

    def _inicializar_datos_si_no_existen(self):
        """Crea y puebla la base de datos persistente en el data_lake si está vacía."""
        conn = duckdb.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ventas_analiticas (
                id INTEGER,
                categoria VARCHAR,
                monto DOUBLE,
                fecha DATE
            );
        """)
        
        count = conn.execute("SELECT COUNT(*) FROM ventas_analiticas;").fetchone()[0]
        if count == 0:
            conn.execute("""
                INSERT INTO ventas_analiticas VALUES 
                (1, 'Tecnología', 150.5, '2026-07-01'),
                (2, 'Hogar', 89.9, '2026-07-02'),
                (3, 'Tecnología', 1200.0, '2026-07-03'),
                (4, 'Moda', 45.0, '2026-07-04'),
                (5, 'Hogar', 210.0, '2026-07-05'),
                (6, 'Tecnología', 430.0, '2026-07-06');
            """)
        conn.close()

    def _ejecutar_query_sincrona(self, query: str) -> List[tuple]:
        """Ejecuta una consulta bloqueante conectándose de forma segura al archivo físico."""
        conn = duckdb.connect(self.db_path, read_only=True)
        cursor = conn.execute(query)
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    async def ejecutar_consulta_async(self, query_id: str, query: str, delay: float = 0.1) -> Dict[str, Any]:
        """Envía una consulta analítica al ejecutor en hilos de forma no bloqueante."""
        inicio = time.time()
        await asyncio.sleep(delay)
        
        # asyncio.to_thread permite que la consulta bloqueante de DuckDB corra en paralelo
        resultado = await asyncio.to_thread(self._ejecutar_query_sincrona, query)
        
        duracion = (time.time() - inicio) * 1000
        return {
            "query_id": query_id,
            "duracion_ms": round(duracion, 2),
            "filas_obtenidas": len(resultado),
            "data": resultado
        }

    async def ejecutar_lote_concurrente(self, tareas_queries: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """Ejecuta múltiples consultas analíticas simultáneamente usando asyncio.gather."""
        tareas = [
            self.ejecutar_consulta_async(t["id"], t["query"], t.get("delay", 0.1))
            for t in tareas_queries
        ]
        resultados = await asyncio.gather(*tareas)
        return resultados
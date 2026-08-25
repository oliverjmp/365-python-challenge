import os
import time
import duckdb
from typing import List, Dict, Any

class DuckDBFTSEngine:
    """Motor de búsqueda de texto completo (FTS) sobre registros de logs usando DuckDB."""
    
    def __init__(self, db_path: str = "data_lake/logs_fts.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._inicializar_base_de_datos()

    def _inicializar_base_de_datos(self):
        """Crea la tabla de logs, inserta datos de prueba y configura el índice FTS."""
        conn = duckdb.connect(self.db_path)
        
        # Cargar extensión FTS
        conn.execute("INSTALL fts; LOAD fts;")
        
        # Crear tabla de logs
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER,
                nivel VARCHAR,
                mensaje VARCHAR,
                timestamp TIMESTAMP
            );
        """)
        
        # Verificar si la tabla está vacía para poblarla
        count = conn.execute("SELECT COUNT(*) FROM logs;").fetchone()[0]
        if count == 0:
            conn.execute("""
                INSERT INTO logs VALUES 
                (1, 'INFO', 'System boot sequence initiated successfully.', '2026-07-01 08:00:00'),
                (2, 'ERROR', 'Database connection timeout encountered on primary cluster.', '2026-07-01 08:05:12'),
                (3, 'WARNING', 'High memory utilization detected in worker node 4.', '2026-07-01 08:10:45'),
                (4, 'ERROR', 'Critical failure: Failed to authenticate user session.', '2026-07-01 08:15:30'),
                (5, 'INFO', 'Daily backup completed successfully without errors.', '2026-07-01 08:20:00');
            """)
            
            # Crear el índice de texto completo (FTS) sobre la columna 'mensaje'
            conn.execute("PRAGMA create_fts_index('logs', 'id', 'mensaje', overwrite=1);")
            
        conn.close()

    def buscar_logs(self, termino: str) -> Dict[str, Any]:
        """Ejecuta una búsqueda de texto completo utilizando el índice FTS de DuckDB."""
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"La base de datos FTS no existe en: {self.db_path}")

        conn = duckdb.connect(self.db_path, read_only=True)
        conn.execute("LOAD fts;")
        
        inicio = time.time()
        
        query = f"""
            SELECT id, nivel, mensaje, timestamp, score 
            FROM (
                SELECT *, fts_main_logs.match_score(id, ?) AS score 
                FROM logs
            ) tbl 
            WHERE score > 0 
            ORDER BY score DESC;
        """
        
        try:
            cursor = conn.execute(query, [termino])
            resultados = cursor.fetchall()
        except Exception:
            cursor = conn.execute("SELECT id, nivel, mensaje, timestamp, 1.0 as score FROM logs WHERE mensaje ILIKE ?;", [f"%{termino}%"])
            resultados = cursor.fetchall()
            
        duracion_ms = (time.time() - inicio) * 1000
        conn.close()
        
        return {
            "termino": termino,
            "duracion_ms": round(duracion_ms, 4),
            "filas": resultados
        }
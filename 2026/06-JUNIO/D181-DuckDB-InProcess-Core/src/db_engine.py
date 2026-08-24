import duckdb
from typing import List, Tuple, Any

class DuckDBEngine:
    def __init__(self, database_path: str = ":memory:"):
        """Inicializa la conexión a DuckDB (por defecto en memoria para pruebas rápidas)."""
        self.database_path = database_path
        self.conn = duckdb.connect(database_path)

    def execute_query(self, query: str, params: tuple = None) -> List[Tuple[Any, ...]]:
        """Ejecuta una consulta SQL y retorna los resultados."""
        if params:
            cursor = self.conn.execute(query, params)
        else:
            cursor = self.conn.execute(query)
        return cursor.fetchall()

    def create_sample_table(self) -> None:
        """Crea una tabla de ejemplo y carga datos analíticos base."""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS analytics_data (
                id INTEGER,
                category VARCHAR,
                value DOUBLE
            );
        """)
        self.conn.execute("""
            INSERT INTO analytics_data VALUES 
            (1, 'A', 10.5),
            (2, 'B', 20.0),
            (3, 'A', 15.2);
        """)

    def close(self) -> None:
        """Cierra la conexión activa a la base de datos."""
        self.conn.close()
import duckdb
import pandas as pd

class DockerDuckDBPipeline:
    """Pipeline analítico optimizado para ejecución in-process en contenedores."""

    def __init__(self):
        self.conn = duckdb.connect(database=":memory:")

    def ejecutar_proceso(self) -> pd.DataFrame:
        """Crea un dataset analítico, ejecuta una agregación con DuckDB y retorna los resultados."""
        self.conn.execute("""
            CREATE TABLE transacciones (
                id INT,
                categoria VARCHAR,
                monto DECIMAL(10,2)
            );
        """)
        self.conn.execute("""
            INSERT INTO transacciones VALUES 
            (1, 'Software', 150.00),
            (2, 'Hardware', 1200.50),
            (3, 'Software', 299.99),
            (4, 'Servicios', 500.00);
        """)
        
        query = """
            SELECT 
                categoria,
                COUNT(*) as total_transacciones,
                SUM(monto) as monto_total
            FROM transacciones
            GROUP BY categoria;
        """
        return self.conn.execute(query.strip()).fetchdf()
from sqlalchemy import create_engine, text
import logging

class SQLIndexAnalyzer:
    def __init__(self, db_url: str = "sqlite:///:memory:"):
        """Inicializa el analizador de rendimiento con SQLAlchemy."""
        self.engine = create_engine(db_url, echo=False)
        self._setup_sample_data()

    def _setup_sample_data(self):
        """Crea una tabla de ejemplo y carga datos para simular consultas y análisis de índices."""
        with self.engine.begin() as conn:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    email TEXT,
                    status TEXT
                )
            """))
            # Insertar datos de prueba si la tabla está vacía
            result = conn.execute(text("SELECT COUNT(*) FROM users")).scalar()
            if result == 0:
                sample_data = [
                    (f"user_{i}", f"user_{i}@example.com", "active" if i % 2 == 0 else "inactive")
                    for i in range(1000)
                ]
                conn.execute(
                    text("INSERT INTO users (username, email, status) VALUES (:username, :email, :status)"),
                    [{"username": u, "email": e, "status": s} for u, e, s in sample_data]
                )

    def get_execution_plan(self, query: str) -> list:
        """Obtiene el plan de ejecución (Explain Query Plan) para una consulta dada."""
        explain_query = f"EXPLAIN QUERY PLAN {query}"
        with self.engine.connect() as conn:
            result = conn.execute(text(explain_query))
            # Retorna una lista de diccionarios o filas con los detalles del plan
            return [dict(row._mapping) for row in result]

    def create_index(self, index_name: str, table_name: str, column_name: str):
        """Crea un índice en una columna específica para optimizar el rendimiento."""
        with self.engine.begin() as conn:
            conn.execute(text(f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column_name})"))

    def analyze_query_performance(self, query: str) -> dict:
        """Analiza el plan de ejecución antes y después de evaluar estrategias."""
        plan = self.get_execution_plan(query)
        return {
            "query": query,
            "plan_steps": len(plan),
            "details": plan
        }
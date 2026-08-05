import logging
from typing import Generator
import duckdb

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Gestor de conexión para DuckDB con patrón Singleton simplificado."""
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path

    def get_connection(self) -> duckdb.DuckDBPyConnection:
        logger.info(f"Conectando a DuckDB en: {self.db_path}")
        return duckdb.connect(self.db_path)
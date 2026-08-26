import threading
import duckdb

class DuckDBConnectionSingleton:
    """Implementación segura del patrón Singleton para la gestión de conexiones DuckDB in-process."""
    
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_path: str = ":memory:"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DuckDBConnectionSingleton, cls).__new__(cls)
                # Inicializar la conexión subyacente
                cls._instance._connection = duckdb.connect(database=db_path)
        return cls._instance

    @property
    def connection(self) -> duckdb.DuckDBPyConnection:
        """Retorna la instancia única de la conexión DuckDB."""
        return self._connection

    @classmethod
    def reset_instance(cls):
        """Método exclusivo para control de pruebas y aislamiento de estado."""
        with cls._lock:
            if cls._instance is not None:
                try:
                    cls._instance._connection.close()
                except Exception: # pragma: no cover
                    pass
                cls._instance = None
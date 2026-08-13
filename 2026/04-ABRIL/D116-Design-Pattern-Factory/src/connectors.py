from abc import ABC, abstractmethod
from typing import Dict, Any

class DatabaseConnector(ABC):
    """Interfaz abstracta para los conectores de datos."""
    @abstractmethod
    def connect(self) -> str:
        pass

class PostgreSQLConnector(DatabaseConnector):
    def connect(self) -> str:
        return "Conectado exitosamente a PostgreSQL."

class MySQLConnector(DatabaseConnector):
    def connect(self) -> str:
        return "Conectado exitosamente a MySQL."

class MongoDBConnector(DatabaseConnector):
    def connect(self) -> str:
        return "Conectado exitosamente a MongoDB."

class ConnectorFactory:
    """Factoría dinámica para la instanciación de conectores de bases de datos."""
    _registry: Dict[str, Any] = {
        "postgresql": PostgreSQLConnector,
        "mysql": MySQLConnector,
        "mongodb": MongoDBConnector
    }

    @classmethod
    def register_connector(cls, db_type: str, connector_class: Any) -> None:
        """Permite registrar nuevos conectores en tiempo de ejecución."""
        cls._registry[db_type.lower()] = connector_class

    @classmethod
    def create_connector(cls, db_type: str) -> DatabaseConnector:
        """Crea y retorna una instancia del conector solicitado."""
        connector_class = cls._registry.get(db_type.lower())
        if not connector_class:
            raise ValueError(f"Conector no soportado o no registrado: '{db_type}'")
        return connector_class()
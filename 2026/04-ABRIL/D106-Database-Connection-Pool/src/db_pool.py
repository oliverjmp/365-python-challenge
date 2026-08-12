from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import logging

class DatabaseConnectionPool:
    def __init__(self, db_url: str = "sqlite:///:memory:", pool_size: int = 5, max_overflow: int = 10):
        """Inicializa el motor de SQLAlchemy utilizando QueuePool para soportar control de concurrencia."""
        self.engine = create_engine(
            db_url,
            poolclass=QueuePool,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_recycle=3600,
            echo=False
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_connection_status(self) -> dict:
        """Obtiene métricas básicas del estado actual del pool."""
        pool = self.engine.pool
        return {
            "size": pool.size(),
            "checkedin": pool.checkedin(),
            "checkedout": pool.checkedout(),
            "overflow": pool.overflow()
        }

    def execute_query(self, query_str: str = "SELECT 1"):
        """Ejecuta una consulta utilizando una conexión del pool."""
        with self.engine.connect() as connection:
            result = connection.execute(text(query_str))
            return result.scalar()
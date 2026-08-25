import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class ClienteModel(Base):
    """Modelo ORM para representar clientes en DuckDB."""
    __tablename__ = "clientes"
    
    # Indicamos autoincrement=False para evitar que SQLAlchemy intente usar SERIAL
    id = Column(Integer, primary_key=True, autoincrement=False)
    nombre = Column(String, nullable=False)
    segmento = Column(String, nullable=False)
    limite_credito = Column(Float, nullable=False, default=0.0)

class DuckDBORMManager:
    """Gestor de conexiones y operaciones ORM utilizando SQLAlchemy y DuckDB."""
    
    def __init__(self, db_path: str = "data_lake/orm_warehouse.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(os.path.abspath(self.db_path)), exist_ok=True)
        
        # Conexión usando el dialecto duckdb-engine
        connection_url = f"duckdb:///{self.db_path}"
        self.engine = create_engine(connection_url, echo=False)
        self.SessionLocal = sessionmaker(bind=self.engine)
        self._inicializar_base()

    def _inicializar_base(self):
        """Crea las tablas definidas en la base declarativa."""
        Base.metadata.create_all(self.engine)

    def guardar_cliente(self, nombre: str, segmento: str, limite_credito: float) -> int:
        """Inserta un cliente y retorna su ID asignado."""
        session = self.SessionLocal()
        try:
            max_id = session.query(ClienteModel).count()
            nuevo_id = max_id + 1
            
            nuevo_cliente = ClienteModel(
                id=nuevo_id, 
                nombre=nombre, 
                segmento=segmento, 
                limite_credito=limite_credito
            )
            session.add(nuevo_cliente)
            session.commit()
            session.refresh(nuevo_cliente)
            return nuevo_cliente.id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def obtener_todos_los_clientes(self) -> list:
        """Obtiene la lista de todos los clientes registrados."""
        session = self.SessionLocal()
        try:
            clientes = session.query(ClienteModel).all()
            return [
                {
                    "id": c.id, 
                    "nombre": c.nombre, 
                    "segmento": c.segmento, 
                    "limite_credito": c.limite_credito
                } 
                for c in clientes
            ]
        finally:
            session.close()
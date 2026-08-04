from datetime import datetime
from typing import List, Optional
from pathlib import Path
import logging

from sqlalchemy import String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("SQLAlchemy-ORM-Core")

# Configuración de ruta absoluta para la base de datos SQLite local
DB_PATH = Path(__file__).resolve().parent / "enterprise_database.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Base Declarativa moderna para SQLAlchemy v2.0+
class Base(DeclarativeBase):
    pass

class DepartmentModel(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relación uno a muchos con empleados
    employees: Mapped[List["EmployeeModel"]] = relationship(
        back_populates="department", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Department(id={self.id}, name='{self.name}')>"

class EmployeeModel(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=False)
    hired_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relación inversa
    department: Mapped["DepartmentModel"] = relationship(back_populates="employees")

    def __repr__(self) -> str:
        return f"<Employee(id={self.id}, name='{self.full_name}', salary={self.salary})>"

def init_database() -> sessionmaker:
    """Inicializa el motor de base de datos y crea las tablas basadas en los modelos ORM."""
    engine = create_engine(DATABASE_URL, echo=False, future=True)
    Base.metadata.create_all(engine)
    logger.info(f"Base de datos inicializada correctamente en: {DB_PATH}")
    return sessionmaker(bind=engine, expire_on_commit=False)

def seed_and_query_data(SessionLocal: sessionmaker) -> None:
    """Ejecuta transacciones seguras e inserción de datos relacionales."""
    with SessionLocal() as session:
        try:
            # 1. Crear departamentos
            dept_data = DepartmentModel(name="Data Engineering & Analytics")
            
            # 2. Crear empleados vinculados transaccionalmente
            emp1 = EmployeeModel(
                full_name="Oliver Morales",
                email="oliver.morales@enterprise.com",
                salary=4500.0,
                department=dept_data
            )
            emp2 = EmployeeModel(
                full_name="Sofía Valenzuela",
                email="sofia.valenzuela@enterprise.com",
                salary=4800.0,
                department=dept_data
            )

            session.add_all([dept_data, emp1, emp2])
            session.commit()
            logger.info("[SUCCESS] Transacción ORM completada: Registros persistidos.")

        except Exception as e:
            session.rollback()
            logger.error(f"Fallo crítico en la transacción, rollback ejecutado: {str(e)}")
            raise

    # Consultar datos de forma relacional
    with SessionLocal() as session:
        dept = session.query(DepartmentModel).filter_by(name="Data Engineering & Analytics").first()
        if dept:
            logger.info(f"Departamento: {dept.name} cuenta con {len(dept.employees)} empleados:")
            for emp in dept.employees:
                logger.info(f" -> Empleado: {emp.full_name} | Salario: €{emp.salary}")

if __name__ == "__main__":
    Session = init_database()
    seed_and_query_data(Session)
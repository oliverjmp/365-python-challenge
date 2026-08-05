from dataclasses import dataclass
import os
import pandas as pd
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base declarativa para el ORM de SQLAlchemy
Base = declarative_base()


class TransactionModel(Base):
    """Modelo ORM corporativo para la persistencia transaccional local en SQLite."""

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(50), nullable=False)
    transaction_date = Column(String(20), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)


@dataclass(frozen=True)
class AnalyticsDTO:
    customer_id: str
    transaction_date: str
    amount: float
    rolling_avg_3m: float
    customer_rank: int


def get_sqlite_engine() -> object:
    """Inicializa el motor SQLite asegurando que el archivo de base de datos

    se ubique de manera determinista en el directorio actual del script D62.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "enterprise_database.db")

    engine = create_engine(f"sqlite:///{db_path}", echo=False)
    Base.metadata.create_all(engine)
    return engine


def seed_sample_data(engine) -> None:
    """Inserta datos transaccionales de prueba si la tabla se encuentra vacía."""
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(TransactionModel).count() == 0:
        sample_records = [
            TransactionModel(
                customer_id="CUST_001",
                transaction_date="2026-01-15",
                amount=1200.0,
                status="COMPLETED",
            ),
            TransactionModel(
                customer_id="CUST_001",
                transaction_date="2026-02-15",
                amount=1500.0,
                status="COMPLETED",
            ),
            TransactionModel(
                customer_id="CUST_001",
                transaction_date="2026-03-15",
                amount=1800.0,
                status="COMPLETED",
            ),
            TransactionModel(
                customer_id="CUST_002",
                transaction_date="2026-02-10",
                amount=950.0,
                status="COMPLETED",
            ),
            TransactionModel(
                customer_id="CUST_002",
                transaction_date="2026-03-10",
                amount=2200.0,
                status="COMPLETED",
            ),
        ]
        session.add_all(sample_records)
        session.commit()
    session.close()


def execute_orm_analytics(min_amount: float) -> pd.DataFrame:
    """Ejecuta analítica avanzada delegando el cálculo de ventanas en SQL

    y estructurando el resultado mediante Pandas con tipado estricto.
    """
    engine = get_sqlite_engine()
    seed_sample_data(engine)

    query = f"""
        SELECT 
            customer_id,
            transaction_date,
            amount,
            AVG(amount) OVER (
                PARTITION BY customer_id 
                ORDER BY transaction_date 
                ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
            ) AS rolling_avg_3m,
            RANK() OVER (
                PARTITION BY transaction_date 
                ORDER BY amount DESC
            ) AS customer_rank
        FROM transactions
        WHERE status = 'COMPLETED' AND amount >= {min_amount}
        ORDER BY transaction_date DESC;
    """

    df = pd.read_sql_query(query, con=engine)
    return df


if __name__ == "__main__":
    print("🚀 [Día 62] Ejecutando pipeline ORM con SQLAlchemy y SQLite...")
    try:
        df_result = execute_orm_analytics(min_amount=900.0)
        print(
            f"✅ Extracción exitosa. Registros procesados: {len(df_result)}"
        )
        print(df_result.to_string(index=False))
    except Exception as err:
        print(f"❌ Error crítico de ejecución: {err}")
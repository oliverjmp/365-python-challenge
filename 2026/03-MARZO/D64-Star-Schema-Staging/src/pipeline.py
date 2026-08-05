import logging
from pathlib import Path
import pandas as pd
from pydantic import BaseModel, Field
from src.database import DatabaseManager

logger = logging.getLogger(__name__)

class TransactionRecord(BaseModel):
    """Modelo Pydantic para validación estricta de la capa staging."""
    customer_id: int
    customer_name: str
    country: str
    product_id: int
    product_name: str
    category: str
    date: str
    quantity: int = Field(gt=0, description="La cantidad debe ser mayor a cero")
    total_amount: float = Field(ge=0.0, description="El monto total no puede ser negativo")


class StarSchemaETL:
    """ETL empresarial para la construcción de un Star Schema optimizado en DuckDB."""

    def __init__(self, db_manager: DatabaseManager, csv_path: str | Path) -> None:
        self.db_manager = db_manager
        self.csv_path = Path(csv_path)

    def _create_tables(self, conn) -> None:
        """Crea el esquema dimensional y de hechos usando DDL nativo de DuckDB."""
        logger.info("Construyendo DDL del modelo dimensional en estrella...")
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS dim_customer (
                customer_id INTEGER PRIMARY KEY,
                customer_name VARCHAR,
                country VARCHAR
            );
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS dim_product (
                product_id INTEGER PRIMARY KEY,
                product_name VARCHAR,
                category VARCHAR
            );
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS dim_date (
                date_key INTEGER PRIMARY KEY,
                full_date DATE,
                year INTEGER,
                month INTEGER,
                day INTEGER
            );
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS fact_transaction (
                transaction_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                date_key INTEGER,
                quantity INTEGER,
                total_amount DOUBLE,
                FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
                FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
                FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
            );
        """)

    def run_pipeline(self) -> None:
        """Ejecuta el flujo completo de extracción, transformación y carga (ETL)."""
        logger.info("Iniciando pipeline ETL para Star Schema en DuckDB...")
        
        if not self.csv_path.exists():
            logger.error(f"El fichero CSV no existe en la ruta: {self.csv_path}")
            raise FileNotFoundError(f"No se encuentra el archivo: {self.csv_path}")

        conn = self.db_manager.get_connection()
        
        try:
            # 1. Crear tablas relacionales
            self._create_tables(conn)

            # 2. Cargar datos crudos y registrar vista virtual en DuckDB
            logger.info(f"Leyendo datos fuente desde: {self.csv_path}")
            df_raw = pd.read_csv(self.csv_path)
            conn.register("raw_transactions", df_raw)

            # 3. Población de dimensiones y hechos mediante SQL analítico optimizado
            logger.info("Poplando dimensión de clientes (dim_customer)...")
            conn.execute("""
                INSERT OR IGNORE INTO dim_customer (customer_id, customer_name, country)
                SELECT DISTINCT customer_id, customer_name, country FROM raw_transactions;
            """)

            logger.info("Poplando dimensión de productos (dim_product)...")
            conn.execute("""
                INSERT OR IGNORE INTO dim_product (product_id, product_name, category)
                SELECT DISTINCT product_id, product_name, category FROM raw_transactions;
            """)

            logger.info("Poplando dimensión de tiempo (dim_date)...")
            conn.execute("""
                INSERT OR IGNORE INTO dim_date (date_key, full_date, year, month, day)
                SELECT DISTINCT 
                    CAST(strftime(CAST(date AS DATE), '%Y%m%d') AS INTEGER) AS date_key,
                    CAST(date AS DATE) AS full_date,
                    EXTRACT(YEAR FROM CAST(date AS DATE)) AS year,
                    EXTRACT(MONTH FROM CAST(date AS DATE)) AS month,
                    EXTRACT(DAY FROM CAST(date AS DATE)) AS day
                FROM raw_transactions;
            """)

            logger.info("Poplando tabla de hechos (fact_transaction)...")
            conn.execute("""
                INSERT INTO fact_transaction (transaction_id, customer_id, product_id, date_key, quantity, total_amount)
                SELECT 
                    ROW_NUMBER() OVER () AS transaction_id,
                    customer_id,
                    product_id,
                    CAST(strftime(CAST(date AS DATE), '%Y%m%d') AS INTEGER) AS date_key,
                    quantity,
                    total_amount
                FROM raw_transactions;
            """)

            logger.info("Pipeline ETL completado exitosamente.")

        except Exception as e:
            logger.exception(f"Error crítico durante la ejecución del pipeline ETL: {e}")
            raise
        finally:
            conn.close()
            logger.info("Conexión con DuckDB cerrada correctamente.")
import logging
import sqlite3
from pathlib import Path

# Configuración de logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("DatabaseManager")


def init_database(db_path: str = "analytics.db") -> sqlite3.Connection:
    """Inicializa la base de datos SQLite local de forma persistente,

    crea la tabla transaccional e inserta datos de prueba si está vacía.
    Incorpora manejo robusto de excepciones.
    """
    try:
        logger.info(
            f"Estableciendo conexión con la base de datos SQLite en: {db_path}"
        )
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Creación de tabla transaccional
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS financial_transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)

        # Verificar si la tabla ya contiene registros
        cursor.execute("SELECT COUNT(*) FROM financial_transactions")
        count = cursor.fetchone()[0]

        if count == 0:
            logger.info(
                "La tabla está vacía. Poblando con dataset transaccional simulado..."
            )
            sample_data = [
                ("2026-01-01", "Revenue", 1500.0),
                ("2026-01-02", "Revenue", 1700.0),
                ("2026-01-03", "Revenue", 1600.0),
                ("2026-01-04", "Revenue", 1400.0),
                ("2026-01-05", "Revenue", 1900.0),
                ("2026-01-06", "Revenue", 2100.0),
                ("2026-01-07", "Revenue", 2000.0),
                ("2026-01-08", "Revenue", 2200.0),
                ("2026-01-09", "Revenue", 2150.0),
                ("2026-01-10", "Revenue", 2500.0),
                ("2026-01-11", "Revenue", 2400.0),
                ("2026-01-12", "Revenue", 2600.0),
                ("2026-01-13", "Revenue", 2700.0),
                ("2026-01-14", "Revenue", 2550.0),
            ]
            cursor.executemany(
                """
                INSERT INTO financial_transactions (transaction_date, category, amount)
                VALUES (?, ?, ?)
            """,
                sample_data,
            )
            conn.commit()
            logger.info("Dataset de prueba insertado y confirmado exitosamente.")
        else:
            logger.info(
                f"La base de datos ya contiene {count} registros existentes."
            )

        return conn

    except sqlite3.Error as e:
        logger.error(
            f"Error crítico en la inicialización o conexión de la base de datos: {e}"
        )
        raise
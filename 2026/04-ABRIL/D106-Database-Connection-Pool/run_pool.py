import logging
from src.db_pool import DatabaseConnectionPool

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Gestor de Pool de Conexiones SQLAlchemy (D106) ===")
    
    # Instanciar el pool con base de datos en memoria para pruebas rápidas
    pool_manager = DatabaseConnectionPool(db_url="sqlite:///:memory:", pool_size=4, max_overflow=2)
    
    # Consultar estado inicial
    status_init = pool_manager.get_connection_status()
    logging.info(f"Estado inicial del Pool: {status_init}")
    
    # Ejecutar consulta de prueba
    val = pool_manager.execute_query("SELECT 100")
    logging.info(f"Resultado de consulta ejecutada desde el pool: {val}")
    
    # Estado final
    status_final = pool_manager.get_connection_status()
    logging.info(f"Estado final del Pool: {status_final}")
    logging.info("=== Hito D106 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()
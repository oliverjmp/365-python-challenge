import logging
from src.connectors import ConnectorFactory

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Patrón Factoría de Conectores (D116) ===")
    
    db_types = ["postgresql", "mysql", "mongodb"]
    
    for db_type in db_types:
        logging.info(f"Instanciando conector para: {db_type}...")
        connector = ConnectorFactory.create_connector(db_type)
        status = connector.connect()
        logging.info(f"Resultado: {status}")
        
    logging.info("=== Hito D116 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()
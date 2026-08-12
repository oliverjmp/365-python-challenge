import logging
from src.archiver import AutomatedFileArchiver

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("=== Iniciando Ejecución Manual de D97 Automated File Archiver ===")
    
    archiver = AutomatedFileArchiver(base_dir="./data")
    archiver.process_files()
    
    logging.info("=== Proceso Finalizado con Éxito ===")
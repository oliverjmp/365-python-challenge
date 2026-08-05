from src.database import DatabaseManager
from src.pipeline import StarSchemaETL

if __name__ == "__main__":
    # Inicializamos el gestor de base de datos (puede ser en memoria o un fichero persistente .db)
    db_manager = DatabaseManager(db_path="warehouse.db")
    
    # Instanciamos y ejecutamos el ETL
    etl = StarSchemaETL(db_manager=db_manager, csv_path="data/source_transactions.csv")
    etl.run_pipeline()
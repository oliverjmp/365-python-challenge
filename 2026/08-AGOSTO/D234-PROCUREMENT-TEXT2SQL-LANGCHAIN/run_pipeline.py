"""Punto de entrada autónomo por consola para validar la canalización de procesamiento."""

import os
import sys
import logging
from dotenv import load_dotenv
from src.database_engine import ProcurementDatabaseManager
from src.text2sql_agent import ProcurementText2SQLAgent

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    print("==================================================================")
    print("  ENTERPRISE PROCUREMENT TEXT-TO-SQL PIPELINE (DUCKDB + LANGCHAIN)")
    print("==================================================================")

    # 1. Inicialización del motor DuckDB
    db = ProcurementDatabaseManager(record_count=50000)
    
    # 2. Validación de credenciales
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logging.error("No se encontró GEMINI_API_KEY en las variables de entorno.")
        sys.exit(1)

    agent = ProcurementText2SQLAgent(db_manager=db, api_key=api_key)

    # 3. Pregunta analítica de prueba
    test_question = "¿Cuáles son las 5 categorías con mayor gasto total en órdenes aprobadas?"
    print(f"\n[Pregunta de Negocio]: {test_question}\n")

    try:
        sql, df_results = agent.query_and_analyze(test_question)
        print("------------------------------------------------------------------")
        print("[SQL GENERADO POR LANGCHAIN]:")
        print(sql)
        print("------------------------------------------------------------------")
        print("[RESULTADOS DE DUCKDB]:")
        print(df_results.to_string(index=False))
        print("------------------------------------------------------------------")
    except Exception as e:
        logging.error("Error durante la ejecución de la consulta: %s", e)


if __name__ == "__main__":
    main()
import logging
from src.analyzer import SQLIndexAnalyzer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Analizador de Rendimiento SQL (Hito D107) ===")
    
    analyzer = SQLIndexAnalyzer(db_url="sqlite:///:memory:")
    
    query = "SELECT * FROM users WHERE email = 'user_888@example.com'"
    
    logging.info(f"Analizando consulta: '{query}'")
    plan_inicial = analyzer.get_execution_plan(query)
    logging.info(f"Plan de ejecución inicial (Sin índice dedicado): {plan_inicial}")
    
    # Crear índice para optimizar la columna email
    logging.info("Creando índice 'idx_users_email' sobre la columna 'email'...")
    analyzer.create_index("idx_users_email", "users", "email")
    
    plan_optimizado = analyzer.get_execution_plan(query)
    logging.info(f"Plan de ejecución optimizado (Con índice): {plan_optimizado}")
    
    logging.info("=== Hito D107 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()
from src.query_runner import DuckDBQueryRunner
from src.exceptions import SQLSyntaxError, QueryExecutionError

def main():
    print("🚀 Iniciando demostración de Error Boundary con DuckDB...")
    runner = DuckDBQueryRunner()

    print("\n1️⃣ Probando consulta exitosa...")
    try:
        runner.ejecutar_query("CREATE TABLE demo (val INT);")
        print("   -> Tabla 'demo' creada con éxito.")
    except Exception as e:
        print(f"   -> Error inesperado: {e}")

    print("\n2️⃣ Probando error de sintaxis controlado...")
    try:
        runner.ejecutar_query("SELEC * FROM demo;") # Error adrede
    except SQLSyntaxError as e:
        print(f"   -> Excepción capturada correctamente:\n      {e}")

    print("\n3️⃣ Probando error de ejecución controlado (tabla inexistente)...")
    try:
        runner.ejecutar_query("SELECT * FROM tabla_inexistente;")
    except QueryExecutionError as e:
        print(f"   -> Excepción capturada correctamente:\n      {e}")

    print("\n✨ ¡Demostración de D199 finalizada con éxito!")

if __name__ == "__main__":
    main()
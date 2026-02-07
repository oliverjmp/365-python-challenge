import sqlite3
import pandas as pd
from pathlib import Path

def buscador_de_incidencias():
    # 1. Rutas
    carpeta_actual = Path(__file__).parent
    ruta_db = carpeta_actual.parent / "23-ENERO" / "sistema_bi_oliver.db"

    print("\n" + "🔍 " * 15)
    print("BUSCADOR INTELIGENTE SQL - DÍA 28")
    print("🔍 " * 15)

    if not ruta_db.exists():
        print("❌ Error: Base de datos no encontrada.")
        return

    # 2. Interacción con el usuario
    palabra_clave = input("\n🔎 ¿Qué término deseas buscar en las quejas? (ej: 'caída', 'lenta', 'diseño'): ")

    # 3. Consulta con Filtro Avanzado
    conexion = sqlite3.connect(ruta_db)
    
    # Usamos %palabra% para que busque la palabra en cualquier parte del texto
    query = f"SELECT id, usuario, comentario, estado FROM AlertasCriticas WHERE comentario LIKE '%{palabra_clave}%'"
    
    df_resultados = pd.read_sql_query(query, conexion)
    conexion.close()

    # 4. Mostrar Resultados
    print(f"\n--- Resultados para: '{palabra_clave}' ---")
    if df_resultados.empty:
        print(f"🤷 No se encontraron registros que contengan '{palabra_clave}'.")
    else:
        print(df_resultados)
        print(f"\n✅ Se encontraron {len(df_resultados)} coincidencias.")

if __name__ == "__main__":
    buscador_de_incidencias()
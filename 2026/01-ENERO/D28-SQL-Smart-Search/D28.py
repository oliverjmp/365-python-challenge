import sqlite3
import pandas as pd
from pathlib import Path

def buscador_de_incidencias():
    # 1. LOCALIZADOR INTELIGENTE (Busca la DB en todo el reto 365)
    ruta_script = Path(__file__).resolve()
    try:
        raiz_proyecto = next(p for p in ruta_script.parents if p.name == "365-python-challenge")
    except StopIteration:
        raiz_proyecto = ruta_script.parent.parent.parent

    print("\n" + "🔍 " * 15)
    print("BUSCADOR INTELIGENTE SQL - DÍA 28")
    print("🔍 " * 15)

    # Buscamos la base de datos de forma recursiva
    posibles_dbs = list(raiz_proyecto.rglob("sistema_bi_oliver.db"))

    if not posibles_dbs:
        print(f"❌ Error: No se encontró la base de datos en {raiz_proyecto}")
        return

    ruta_db = posibles_dbs[0]
    print(f"✅ Conectado a: {ruta_db.name}")

    # 2. Interacción con el usuario
    palabra_clave = input("\n🔎 ¿Qué término deseas buscar en las quejas? (ej: 'caída', 'lenta', 'diseño'): ")

    if not palabra_clave.strip():
        print("⚠️ Por favor, ingresa un término de búsqueda válido.")
        return

    # 3. Consulta con Filtro Seguro (Parametrizada)
    conexion = sqlite3.connect(ruta_db)
    
    # La forma segura de usar LIKE con parámetros para evitar SQL Injection
    query = "SELECT id, usuario, comentario, estado FROM AlertasCriticas WHERE comentario LIKE ?"
    parametro = f"%{palabra_clave}%"
    
    df_resultados = pd.read_sql_query(query, conexion, params=(parametro,))
    conexion.close()

    # 4. Mostrar Resultados con Formato
    print(f"\n--- Resultados para: '{palabra_clave}' ---")
    if df_resultados.empty:
        print(f"🤷 No se encontraron registros que contengan '{palabra_clave}'.")
    else:
        # Ajustamos el ancho de las columnas para que se vea bien en consola
        pd.set_option('display.max_colwidth', 50)
        print(df_resultados.to_string(index=False))
        print(f"\n✅ Se encontraron {len(df_resultados)} coincidencias.")

if __name__ == "__main__":
    buscador_de_incidencias()
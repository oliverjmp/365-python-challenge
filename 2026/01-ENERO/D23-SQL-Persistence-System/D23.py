import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime

def gestionar_base_datos_bi():
    # 1. LOCALIZACIÓN INTELIGENTE (Para evitar el error de ruta)
    ruta_script = Path(__file__).resolve()
    # Buscamos la raíz del proyecto para olfatear el CSV
    raiz_proyecto = next((p for p in ruta_script.parents if p.name == "365-python-challenge"), ruta_script.parent.parent)
    
    print("\n" + "🗄️ " * 15)
    print("SISTEMA DE PERSISTENCIA SQL - DÍA 23")
    print("🗄️ " * 15)

    # Buscamos el reporte de sentimientos
    posibles_rutas = list(raiz_proyecto.rglob("reporte_sentimientos_final.csv"))
    
    if not posibles_rutas:
        print("❌ Error: No se encontró el archivo CSV en ninguna carpeta.")
        return

    ruta_datos = posibles_rutas[0]
    ruta_db = ruta_script.parent / "sistema_bi_oliver.db"

    # 2. Conexión y Creación de Tabla
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AlertasCriticas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            usuario TEXT,
            comentario TEXT,
            score REAL,
            estado TEXT DEFAULT 'PENDIENTE'
        )
    ''')
    
    # 3. Procesamiento de datos
    df = pd.read_csv(ruta_datos)
    # Aseguramos que las columnas existan (manejo de errores robusto)
    col_user = 'usuario' if 'usuario' in df.columns else (df.columns[0] if len(df.columns) > 0 else 'N/A')
    alertas = df[df['score'] <= -0.7]

    # 4. Inserción de datos
    if not alertas.empty:
        fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for _, fila in alertas.iterrows():
            cursor.execute('''
                INSERT INTO AlertasCriticas (fecha, usuario, comentario, score)
                VALUES (?, ?, ?, ?)
            ''', (fecha_registro, str(fila.get(col_user, 'N/A')), fila['comentario'], fila['score']))
        
        conexion.commit()
        print(f"✅ ÉXITO: {len(alertas)} registros guardados en SQL.")
    else:
        print("✅ No hay alertas nuevas que procesar.")

    # 5. Consulta de Verificación
    print("\n📋 VISTA PREVIA DE LA BASE DE DATOS (Últimos 5):")
    df_db = pd.read_sql_query("SELECT id, usuario, score, estado FROM AlertasCriticas ORDER BY id DESC LIMIT 5", conexion)
    print(df_db)

    conexion.close()
    print(f"\n📂 Base de datos actualizada: {ruta_db.name}")

if __name__ == "__main__":
    gestionar_base_datos_bi()
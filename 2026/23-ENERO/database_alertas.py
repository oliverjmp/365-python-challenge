import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime

def gestionar_base_datos_bi():
    # 1. Rutas y Conexión
    carpeta_actual = Path(__file__).parent
    ruta_datos = carpeta_actual.parent / "20-ENERO" / "reporte_sentimientos_final.csv"
    ruta_db = carpeta_actual / "sistema_bi_oliver.db"

    print("\n" + "🗄️ " * 15)
    print("SISTEMA DE PERSISTENCIA SQL - DÍA 23")
    print("🗄️ " * 15)

    # 2. Conectar a SQLite (Crea el archivo si no existe)
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    # 3. Crear la tabla de Alertas si no existe (Lenguaje SQL puro)
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
    
    # 4. Leer datos y filtrar críticos
    if not ruta_datos.exists():
        print("❌ Error: No se encontraron datos del Día 20.")
        return

    df = pd.read_csv(ruta_datos)
    alertas = df[df['score'] <= -0.7]

    # 5. Insertar datos en la Base de Datos
    if not alertas.empty:
        fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for _, fila in alertas.iterrows():
            # Insertamos solo si el comentario no existe para evitar duplicados sencillos
            cursor.execute('''
                INSERT INTO AlertasCriticas (fecha, usuario, comentario, score)
                VALUES (?, ?, ?, ?)
            ''', (fecha_registro, fila['usuario'], fila['comentario'], fila['score']))
        
        conexion.commit()
        print(f"✅ Se han insertado {len(alertas)} registros en la base de datos.")
    else:
        print("✅ No hay alertas nuevas para guardar.")

    # 6. Verificación: Consultar la DB para demostrar que funciona
    print("\n📋 ÚLTIMOS REGISTROS EN LA BASE DE DATOS:")
    query = "SELECT id, usuario, score, estado FROM AlertasCriticas ORDER BY id DESC LIMIT 5"
    df_db = pd.read_sql_query(query, conexion)
    print(df_db)

    conexion.close()
    print(f"\n📂 Base de datos lista: {ruta_db.name}")

if __name__ == "__main__":
    gestionar_base_datos_bi()
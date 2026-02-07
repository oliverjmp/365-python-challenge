import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime

def ingesta_datos_nuevos():
    # 1. LOCALIZADOR INTELIGENTE (Buscador de DB)
    ruta_script = Path(__file__).resolve()
    raiz_proyecto = next((p for p in ruta_script.parents if p.name == "365-python-challenge"), ruta_script.parent.parent)
    
    posibles_dbs = list(raiz_proyecto.rglob("sistema_bi_oliver.db"))
    if not posibles_dbs:
        print("❌ Error: Ejecuta primero el Día 23 para crear la DB.")
        return
    ruta_db = posibles_dbs[0]

    print("\n" + "📥 " * 15)
    print("INGESTA INCREMENTAL DE DATOS - DÍA 27")
    print(f"📂 Usando DB en: {ruta_db.name}")
    print("📥 " * 15)

    # 2. Datos nuevos (Simulación)
    datos_nuevos = [
        {'usuario': 'Cliente_F', 'comentario': 'El sistema se cayó otra vez, es terrible.', 'score': -0.9},
        {'usuario': 'Cliente_G', 'comentario': 'Me encanta la nueva función, muy útil!', 'score': 0.9}
    ]
    df_nuevos = pd.DataFrame(datos_nuevos)

    # 3. Conexión e Inserción
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    contador = 0

    for _, fila in df_nuevos.iterrows():
        if fila['score'] <= -0.7:
            cursor.execute('''
                INSERT INTO AlertasCriticas (fecha, usuario, comentario, score, estado)
                VALUES (?, ?, ?, ?, 'PENDIENTE')
            ''', (fecha_hoy, fila['usuario'], fila['comentario'], fila['score']))
            contador += 1

    conexion.commit()
    print(f"✅ Proceso terminado. Se añadieron {contador} nuevas alertas críticas.")
    
    # 4. Verificación
    df_final = pd.read_sql_query("SELECT id, usuario, score, estado FROM AlertasCriticas ORDER BY id DESC LIMIT 5", conexion)
    print("\n📊 ÚLTIMOS REGISTROS EN LA DB:")
    print(df_final)
    conexion.close()

if __name__ == "__main__":
    ingesta_datos_nuevos()
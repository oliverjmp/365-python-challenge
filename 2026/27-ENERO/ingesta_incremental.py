import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime

def ingesta_datos_nuevos():
    carpeta_actual = Path(__file__).parent
    ruta_db = carpeta_actual.parent / "23-ENERO" / "sistema_bi_oliver.db"

    print("\n" + "📥 " * 15)
    print("INGESTA INCREMENTAL DE DATOS - DÍA 27")
    print("📥 " * 15)

    # 1. Simulación de datos nuevos que llegan hoy
    # En la vida real, esto vendría de un nuevo CSV o una API
    datos_nuevos = [
        {'usuario': 'Cliente_F', 'comentario': 'El sistema se cayó otra vez, es terrible.', 'score': -0.9},
        {'usuario': 'Cliente_G', 'comentario': 'Me encanta la nueva función, muy útil!', 'score': 0.9}
    ]
    df_nuevos = pd.DataFrame(datos_nuevos)

    # 2. Conectar a la DB
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    # 3. Filtrar y Cargar (Solo los críticos van a la tabla de Alertas)
    fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    contador = 0

    for _, fila in df_nuevos.iterrows():
        if fila['score'] <= -0.7:
            # Solo insertamos si es crítico (nuestra regla de negocio)
            cursor.execute('''
                INSERT INTO AlertasCriticas (fecha, usuario, comentario, score, estado)
                VALUES (?, ?, ?, ?, 'PENDIENTE')
            ''', (fecha_hoy, fila['usuario'], fila['comentario'], fila['score']))
            contador += 1

    conexion.commit()
    
    # 4. Mostrar impacto en la DB
    print(f"✅ Proceso terminado. Se añadieron {contador} nuevas alertas críticas.")
    
    print("\n📊 ESTADO ACTUAL DE LA BASE DE DATOS (Top 5):")
    df_final = pd.read_sql_query("SELECT id, usuario, score, estado FROM AlertasCriticas ORDER BY id DESC", conexion)
    print(df_final.head(5))

    conexion.close()

if __name__ == "__main__":
    ingesta_datos_nuevos()
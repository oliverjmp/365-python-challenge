import sqlite3
import pandas as pd
from pathlib import Path

def exportar_datos_a_excel():
    # 1. LOCALIZADOR INTELIGENTE (Busca la DB en todo el reto)
    ruta_script = Path(__file__).resolve()
    try:
        raiz_proyecto = next(p for p in ruta_script.parents if p.name == "365-python-challenge")
    except StopIteration:
        raiz_proyecto = ruta_script.parent.parent.parent

    print("\n" + "📊 " * 15)
    print("EXPORTADOR MAESTRO A EXCEL - DÍA 30")
    print("📊 " * 15)

    posibles_dbs = list(raiz_proyecto.rglob("sistema_bi_oliver.db"))
    if not posibles_dbs:
        print("❌ Error: No se encontró la base de datos.")
        return
    
    ruta_db = posibles_dbs[0]
    ruta_excel = ruta_script.parent / "Reporte_Final_Enero_Oliver.xlsx"

    # 2. Extraer datos con SQL
    conexion = sqlite3.connect(ruta_db)
    df = pd.read_sql_query("SELECT * FROM AlertasCriticas", conexion)
    conexion.close()

    if df.empty:
        print("⚠️ No hay datos para exportar.")
        return

    # 3. Exportación Profesional
    try:
        # Separamos datos por estado para crear pestañas útiles
        df_pendientes = df[df['estado'] == 'PENDIENTE']
        df_resueltos = df[df['estado'] == 'RESUELTO']

        with pd.ExcelWriter(ruta_excel, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='TODO_EL_MES')
            df_pendientes.to_excel(writer, index=False, sheet_name='PENDIENTES_CRITICOS')
            df_resueltos.to_excel(writer, index=False, sheet_name='HISTORIAL_RESUELTOS')

        print(f"✅ ¡ÉXITO TOTAL! Reporte generado: {ruta_excel.name}")
        print(f"📈 Total procesado: {len(df)} registros.")
        print(f"📂 Pestañas creadas: 'TODO_EL_MES', 'PENDIENTES_CRITICOS', 'HISTORIAL_RESUELTOS'")
        
        # Un toque de humor para celebrar
        print("\n🏆 ¡FELICIDADES OLIVER! HAS COMPLETADO LOS PRIMEROS 30 DÍAS.")
        
    except Exception as e:
        print(f"❌ Error al exportar: {e}")

if __name__ == "__main__":
    exportar_datos_a_excel()
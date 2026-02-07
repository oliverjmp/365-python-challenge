import sqlite3
import pandas as pd
from pathlib import Path

def exportar_datos_a_excel():
    # 1. Rutas
    carpeta_actual = Path(__file__).parent
    ruta_db = carpeta_actual.parent / "23-ENERO" / "sistema_bi_oliver.db"
    ruta_excel = carpeta_actual / "Reporte_Final_Enero.xlsx"

    print("\n" + "📊 " * 15)
    print("EXPORTADOR MAESTRO A EXCEL - DÍA 30")
    print("📊 " * 15)

    if not ruta_db.exists():
        print("❌ Error: No se encontró la base de datos.")
        return

    # 2. Extraer todo de SQL con Pandas
    conexion = sqlite3.connect(ruta_db)
    df = pd.read_sql_query("SELECT * FROM AlertasCriticas", conexion)
    conexion.close()

    if df.empty:
        print("⚠️ No hay datos para exportar.")
        return

    # 3. Exportación con estilo
    # Usamos el motor openpyxl para crear un Excel real
    try:
        with pd.ExcelWriter(ruta_excel, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Alertas_Enero')
            
            # Aquí podrías añadir más hojas si tuvieras más tablas
            # df_kpi.to_excel(writer, sheet_name='Resumen_KPI')

        print(f"✅ ¡Éxito! Reporte generado correctamente.")
        print(f"📁 Ubicación: {ruta_excel.name}")
        print(f"📈 Total de filas exportadas: {len(df)}")
        
    except Exception as e:
        print(f"❌ Error al exportar a Excel: {e}")

if __name__ == "__main__":
    exportar_datos_a_excel()
import sqlite3
import pandas as pd
from pathlib import Path

def generar_reporte_kpi():
    # 1. Rutas y Conexión
    carpeta_actual = Path(__file__).parent
    ruta_db = carpeta_actual.parent / "23-ENERO" / "sistema_bi_oliver.db"

    print("\n" + "📊 " * 15)
    print("REPORTE DE PERFORMANCE (KPI) - DÍA 26")
    print("📊 " * 15)

    if not ruta_db.exists():
        print("❌ Error: No se encontró la base de datos.")
        return

    conexion = sqlite3.connect(ruta_db)
    
    # 2. Cargar todos los datos para análisis
    df = pd.read_sql_query("SELECT * FROM AlertasCriticas", conexion)
    conexion.close()

    if df.empty:
        print("⚠️ No hay datos para analizar.")
        return

    # 3. Cálculos de KPI
    total_tickets = len(df)
    resueltos = len(df[df['estado'] == 'RESUELTO'])
    pendientes = len(df[df['estado'] == 'PENDIENTE'])
    
    # KPI 1: Tasa de Resolución
    tasa_resolucion = (resueltos / total_tickets) * 100

    # KPI 2: Sentimiento Promedio por Estado
    sentimiento_promedio = df.groupby('estado')['score'].mean()

    # 4. Presentación Ejecutiva
    print(f"\n📈 RESUMEN EJECUTIVO:")
    print(f"{"-"*30}")
    print(f"Total de Incidencias:  {total_tickets}")
    print(f"Tickets Resueltos:     {resueltos} ✅")
    print(f"Tickets Pendientes:    {pendientes} ⏳")
    print(f"TASA DE RESOLUCIÓN:    {tasa_resolucion:.1f}%")
    print(f"{"-"*30}")
    
    print("\n🧠 ANÁLISIS DE GRAVEDAD (Sentiment Score):")
    for estado, score in sentimiento_promedio.items():
        gravedad = "ALTA 🔴" if score < -0.5 else "MEDIA 🟡"
        print(f"Estado {estado}: {score:.2f} (Prioridad {gravedad})")

    # 5. Guardar KPI en un resumen rápido
    with open(carpeta_actual / "resumen_ejecutivo.txt", "w", encoding="utf-8") as f:
        f.write(f"REPORTE BI - DÍA 26\nTasa de Resolución: {tasa_resolucion:.1f}%\nTotal: {total_tickets}")

if __name__ == "__main__":
    generar_reporte_kpi()
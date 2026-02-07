import sqlite3
import pandas as pd
from pathlib import Path

def generar_reporte_kpi():
    # 1. LOCALIZADOR INTELIGENTE (Busca la DB en todo el reto 365)
    ruta_script = Path(__file__).resolve()
    # Buscamos la carpeta raíz del proyecto para no fallar con las rutas
    try:
        raiz_proyecto = next(p for p in ruta_script.parents if p.name == "365-python-challenge")
    except StopIteration:
        # Plan B si no encuentra la carpeta raíz por nombre
        raiz_proyecto = ruta_script.parent.parent.parent

    print("\n" + "📊 " * 15)
    print("REPORTE DE PERFORMANCE (KPI) - DÍA 26")
    print("📊 " * 15)

    # Buscamos el archivo de la base de datos de forma recursiva
    posibles_dbs = list(raiz_proyecto.rglob("sistema_bi_oliver.db"))

    if not posibles_dbs:
        print(f"❌ Error: No se encontró 'sistema_bi_oliver.db' en {raiz_proyecto}")
        print("👉 Asegúrate de haber ejecutado el Día 23 para crear la base de datos.")
        return

    ruta_db = posibles_dbs[0]
    print(f"✅ Conectado a la base de datos en: {ruta_db.name}")

    # 2. Cargar datos con SQL y Pandas
    conexion = sqlite3.connect(ruta_db)
    df = pd.read_sql_query("SELECT * FROM AlertasCriticas", conexion)
    conexion.close()

    if df.empty:
        print("⚠️ La base de datos está vacía. No hay métricas que calcular.")
        return

    # 3. Cálculo de KPIs (Métricas Clave)
    total_tickets = len(df)
    resueltos = len(df[df['estado'] == 'RESUELTO'])
    pendientes = len(df[df['estado'] == 'PENDIENTE'])
    
    # KPI 1: Tasa de Resolución (Evitamos división por cero)
    tasa_resolucion = (resueltos / total_tickets) * 100 if total_tickets > 0 else 0

    # KPI 2: Sentimiento Promedio por Estado (Group By)
    sentimiento_promedio = df.groupby('estado')['score'].mean()

    # 4. Presentación Ejecutiva en Consola
    print(f"\n📈 RESUMEN DE OPERACIONES:")
    print(f"{'-'*40}")
    print(f"📋 Total de Incidencias:  {total_tickets}")
    print(f"✅ Tickets Resueltos:     {resueltos}")
    print(f"⏳ Tickets Pendientes:    {pendientes}")
    print(f"🚀 TASA DE RESOLUCIÓN:    {tasa_resolucion:.1f}%")
    print(f"{'-'*40}")
    
    print("\n🧠 ANÁLISIS DE GRAVEDAD POR ESTADO:")
    for estado, score in sentimiento_promedio.items():
        # Lógica de prioridad basada en el score de sentimiento
        prioridad = "CRÍTICA 🔴" if score <= -0.8 else "ALTA 🟡"
        print(f"• Estado {estado}: Score Promedio {score:.2f} (Prioridad {prioridad})")

    # 5. Exportación del Resumen Rápido (TXT)
    ruta_resumen = ruta_script.parent / "resumen_ejecutivo.txt"
    with open(ruta_resumen, "w", encoding="utf-8") as f:
        f.write(f"--- REPORTE BI OLIVER - DÍA 26 ---\n")
        f.write(f"Fecha: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Tasa de Resolución: {tasa_resolucion:.1f}%\n")
        f.write(f"Tickets Pendientes: {pendientes}\n")
        f.write(f"Estado de Salud: {'Sano' if tasa_resolucion > 70 else 'Crítico'}")

    print(f"\n📂 Resumen guardado en: {ruta_resumen.name}")

if __name__ == "__main__":
    generar_reporte_kpi()
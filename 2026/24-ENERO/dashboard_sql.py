import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generar_dashboard_desde_sql():
    # 1. Rutas y Conexión
    carpeta_actual = Path(__file__).parent
    ruta_db = carpeta_actual.parent / "23-ENERO" / "sistema_bi_oliver.db"

    print("\n" + "📈 " * 15)
    print("DASHBOARD PROFESIONAL (SQL) - DÍA 24")
    print("📈 " * 15)

    if not ruta_db.exists():
        print("❌ Error: No se encontró la base de datos del Día 23.")
        return

    # 2. Conectar y Extraer datos con SQL
    conexion = sqlite3.connect(ruta_db)
    
    # Esta query cuenta cuántos hay de cada estado (PENDIENTE/RESUELTO)
    query = "SELECT estado, COUNT(*) as total FROM AlertasCriticas GROUP BY estado"
    df_stats = pd.read_sql_query(query, conexion)
    
    conexion.close()

    if df_stats.empty:
        print("⚠️ No hay datos suficientes en la DB para graficar.")
        return

    # 3. Crear Visualización de Gestión
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df_stats['estado'], df_stats['total'], color=['#e74c3c', '#3498db'])
    
    # Añadir etiquetas de datos sobre las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom', fontweight='bold')

    plt.title('Estado de Gestión de Alertas Críticas (Fuente: SQL)', fontsize=14)
    plt.xlabel('Estado del Ticket')
    plt.ylabel('Cantidad de Alertas')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 4. Guardar y Mostrar
    ruta_img = carpeta_actual / "reporte_gestion_sql.png"
    plt.savefig(ruta_img)
    print(f"✅ Dashboard actualizado y guardado como: {ruta_img.name}")
    
    print("\n🚀 Desplegando visualización de base de datos...")
    plt.show()

if __name__ == "__main__":
    generar_dashboard_desde_sql()
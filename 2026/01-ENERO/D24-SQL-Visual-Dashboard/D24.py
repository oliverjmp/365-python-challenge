import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generar_dashboard_desde_sql():
    # 1. LOCALIZADOR INTELIGENTE (Buscador de DB)
    ruta_script = Path(__file__).resolve()
    # Buscamos la raíz del reto
    raiz_proyecto = next((p for p in ruta_script.parents if p.name == "365-python-challenge"), ruta_script.parent.parent)
    
    print("\n" + "📈 " * 15)
    print("DASHBOARD PROFESIONAL (SQL) - DÍA 24")
    print("📈 " * 15)

    # Buscamos el archivo de la base de datos en cualquier subcarpeta
    posibles_dbs = list(raiz_proyecto.rglob("sistema_bi_oliver.db"))

    if not posibles_dbs:
        print(f"❌ Error: No se encontró la base de datos en {raiz_proyecto}")
        print("👉 Asegúrate de haber ejecutado el script del Día 23 primero.")
        return

    ruta_db = posibles_dbs[0]
    print(f"✅ Base de datos detectada en: {ruta_db.relative_to(raiz_proyecto)}")

    # 2. Conectar y Extraer datos con SQL
    conexion = sqlite3.connect(ruta_db)
    
    # Query de agregación: Contamos por estado
    query = "SELECT estado, COUNT(*) as total FROM AlertasCriticas GROUP BY estado"
    df_stats = pd.read_sql_query(query, conexion)
    conexion.close()

    if df_stats.empty:
        print("⚠️ La base de datos está vacía. Inserta datos en el Día 23 antes de graficar.")
        return

    # 3. Crear Visualización Profesional
    plt.figure(figsize=(10, 6))
    
    # Mapeo de colores: Rojo para PENDIENTE, Azul/Verde para otros
    colores = ['#e74c3c' if x == 'PENDIENTE' else '#3498db' for x in df_stats['estado']]
    
    bars = plt.bar(df_stats['estado'], df_stats['total'], color=colores)
    
    # Etiquetas de datos
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, int(yval), 
                 ha='center', va='bottom', fontweight='bold', fontsize=12)

    plt.title('ESTADO DE GESTIÓN DE ALERTAS (BI DASHBOARD)', fontsize=14, fontweight='bold')
    plt.ylabel('Cantidad de Tickets')
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    # 4. Guardar y Mostrar
    ruta_img = ruta_script.parent / "reporte_gestion_sql.png"
    plt.savefig(ruta_img)
    print(f"\n✅ Imagen profesional generada: {ruta_img.name}")
    
    print("🚀 Abriendo ventana de visualización...")
    plt.show()

if __name__ == "__main__":
    generar_dashboard_desde_sql()
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generar_grafico_bi():
    # 1. Rutas Seguras
    carpeta_actual = Path(__file__).parent
    ruta_entrada = carpeta_actual / "reporte_sentimientos_final.csv"
    ruta_grafico = carpeta_actual / "dashboard_sentimientos.png"

    print("\n" + "="*50)
    print("📊 DASHBOARD GENERATOR - DÍA 20")
    print("="*50)

    # 2. Cargar datos del Día 19
    if not ruta_entrada.exists():
        print("❌ Error: No se encontró el reporte del Día 19.")
        return

    df = pd.read_csv(ruta_entrada)
    
    # 3. Contar sentimientos para el gráfico
    conteo = df['sentimiento'].value_counts()
    
    # 4. Configurar el diseño del gráfico
    colores = {'POSITIVO': '#2ecc71', 'NEGATIVO': '#e74c3c', 'NEUTRO': '#f1c40f'}
    mis_colores = [colores.get(x, '#95a5a6') for x in conteo.index]

    plt.figure(figsize=(8, 6))
    plt.pie(
        conteo, 
        labels=conteo.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=mis_colores,
        explode=[0.05] * len(conteo) # Separa un poco las tajadas
    )
    
    plt.title('Distribución de Sentimientos de Clientes', fontsize=14, fontweight='bold')

    # 5. Guardar y Mostrar
    plt.savefig(ruta_grafico) # Guarda una imagen profesional
    print(f"✅ Imagen guardada: {ruta_grafico.name}")
    
    print("\n🚀 Abriendo ventana de visualización...")
    plt.show() # Abre la ventana con el gráfico

if __name__ == "__main__":
    generar_grafico_bi()
"""
Proyecto: 365 Python Challenge
Día 56: Data Visualization & Absolute Pathing
Objetivo: Generar un dashboard visual y guardarlo correctamente en la carpeta del día.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

class DataVisualizer:
    def __init__(self):
        # 1. Definimos las rutas usando Pathlib para evitar archivos perdidos
        self.directorio_actual = Path(__file__).parent.absolute()
        self.ruta_imagen = self.directorio_actual / 'dashboard_negocio.png'

        # 2. Dataset para el análisis (Mismas métricas del D55)
        data = {
            'Departamento': ['Tech', 'Hogar', 'Tech', 'Hogar', 'Tech', 'Moda', 'Moda', 'Tech'],
            'Ventas_USD': [1500, 800, 600, 450, 1200, 100, 250, 150],
            'Beneficio': [400, 200, 200, 150, 400, 60, 150, 70]
        }
        self.df = pd.DataFrame(data)
        self.report = self.df.groupby('Departamento').sum()

    def create_dashboard(self):
        print(f"🎨 Iniciando motor gráfico...")
        print(f"📁 Destino: {self.ruta_imagen}")

        # Configuramos una figura con dos subgráficos (1 fila, 2 columnas)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('📊 Dashboard Ejecutivo: Análisis de Rendimiento Q1', fontsize=16, fontweight='bold')

        # --- GRÁFICO 1: Barras para Ventas Totales ---
        self.report['Ventas_USD'].plot(kind='bar', ax=ax1, color='#3498db', edgecolor='black')
        ax1.set_title('Ventas Totales por Dept.', pad=15)
        ax1.set_ylabel('USD ($)')
        ax1.set_xlabel('Departamento')
        ax1.grid(axis='y', linestyle='--', alpha=0.7)

        # --- GRÁFICO 2: Tarta para Distribución de Beneficios ---
        colores = ['#e74c3c', '#2ecc71', '#f1c40f']
        self.report['Beneficio'].plot(
            kind='pie', 
            ax=ax2, 
            autopct='%1.1f%%', 
            startangle=140, 
            colors=colores,
            explode=[0.05, 0.05, 0.05], # Separa un poco los trozos
            shadow=True
        )
        ax2.set_title('Margen de Beneficio por Categoría (%)', pad=15)
        ax2.set_ylabel('') # Limpia el eje Y para mejor estética

        # Ajuste de márgenes para que todo quepa perfectamente
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # 3. Guardado robusto en la carpeta del script
        plt.savefig(self.ruta_imagen, dpi=300) # dpi=300 para alta calidad profesional
        print(f"✅ Dashboard generado con éxito: 'dashboard_negocio.png'")
        
        # Mostrar ventana (opcional si estás en entorno con GUI)
        plt.show()

if __name__ == "__main__":
    try:
        visualizer = DataVisualizer()
        visualizer.create_dashboard()
        
        print("\n" + "═"*50)
        print("🚀 HITO D56 COMPLETADO: Visualización Profesional")
        print("═"*50)
    except Exception as e:
        print(f"❌ Error crítico en el motor gráfico: {e}")
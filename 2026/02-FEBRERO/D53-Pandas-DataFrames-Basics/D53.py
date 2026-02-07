"""
Proyecto: 365 Python Challenge
Día 53: Pandas DataFrames Basics
Objetivo: Crear, filtrar y analizar un dataset de ventas e inventario.
"""

import pandas as pd

class DataAnalyzer:
    def __init__(self):
        # 1. Creamos un dataset de prueba (Simulando lo que extraeríamos de una web)
        self.data = {
            'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Cámara', 'Micro', 'Cable HDMI'],
            'Categoría': ['Electrónica', 'Accesorios', 'Electrónica', 'Accesorios', 'Video', 'Audio', 'Accesorios'],
            'Precio': [1200, 25, 300, 45, 150, 80, 15],
            'Stock': [15, 120, 10, 50, 8, 25, 100],
            'Ventas': [5, 45, 2, 30, 4, 12, 60]
        }
        self.df = pd.DataFrame(self.data)

    def basic_exploration(self):
        print("\n" + "═"*50)
        print("📊 VISTA PREVIA DEL DATAFRAME")
        print("═"*50)
        # Mostramos las primeras 5 filas
        print(self.df.head())

        print("\n🔍 RESUMEN ESTADÍSTICO")
        # El método describe() es magia pura para análisis rápido
        print(self.df.describe())

    def filter_and_calculate(self):
        print("\n" + "═"*50)
        print("🧪 FILTRADO Y CÁLCULOS")
        print("═"*50)

        # 1. Calcular una nueva columna: Ingresos Totales
        self.df['Ingresos'] = self.df['Precio'] * self.df['Ventas']
        
        # 2. Filtrar productos con Precio mayor a 100
        premium_products = self.df[self.df['Precio'] > 100]
        
        print(f"💰 Productos Premium (>100 USD):\n{premium_products[['Producto', 'Precio']]}")

        # 3. Calcular el ingreso total de toda la tienda
        total_global = self.df['Ingresos'].sum()
        print(f"\n💵 Ingreso Total Global: ${total_global}")

if __name__ == "__main__":
    # Asegúrate de tener instalado pandas: pip install pandas
    try:
        analyzer = DataAnalyzer()
        analyzer.basic_exploration()
        analyzer.filter_and_calculate()
    except ImportError:
        print("❌ Error: Necesitas instalar pandas. Ejecuta: pip install pandas")

    print("\n" + "═"*50)
    print("✨ Hito D53: Dominio de DataFrames Completado")
    print("═"*50)
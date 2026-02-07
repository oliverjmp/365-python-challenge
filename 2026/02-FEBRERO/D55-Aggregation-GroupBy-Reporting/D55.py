"""
Proyecto: 365 Python Challenge
Día 55: Aggregation & GroupBy
Objetivo: Generar un reporte de ventas por categoría y calcular métricas de rendimiento.
"""

import pandas as pd

class BusinessReporter:
    def __init__(self):
        # 1. Dataset expandido para análisis de grupos
        data = {
            'Departamento': ['Tech', 'Hogar', 'Tech', 'Hogar', 'Tech', 'Moda', 'Moda', 'Tech'],
            'Producto': ['Laptop', 'Sofá', 'Tablet', 'Mesa', 'Cámara', 'Camisa', 'Zapatos', 'Teclado'],
            'Ventas_USD': [1500, 800, 600, 450, 1200, 100, 250, 150],
            'Costo_USD': [1100, 600, 400, 300, 800, 40, 100, 80],
            'Unidades': [5, 2, 8, 3, 10, 25, 12, 15]
        }
        self.df = pd.DataFrame(data)

    def generate_report(self):
        print("\n" + "═"*50)
        print("🚀 REPORTE ESTRATÉGICO POR DEPARTAMENTO")
        print("═"*50)

        # 2. Calculamos el beneficio individual primero
        self.df['Beneficio'] = self.df['Ventas_USD'] - self.df['Costo_USD']

        # 3. Aplicamos GroupBy con múltiples agregaciones
        # Queremos: Suma de ventas, promedio de beneficio y total de unidades.
        report = self.df.groupby('Departamento').agg({
            'Ventas_USD': 'sum',
            'Beneficio': 'mean',
            'Unidades': 'sum'
        }).rename(columns={
            'Ventas_USD': 'Total_Ventas',
            'Beneficio': 'Promedio_Margen',
            'Unidades': 'Stock_Vendido'
        })

        print(report)

        # 4. Análisis de Rentabilidad (Orden descendente)
        print("\n🏆 DEPARTAMENTOS POR RENTABILIDAD TOTAL:")
        rentabilidad = self.df.groupby('Departamento')['Beneficio'].sum().sort_values(ascending=False)
        print(rentabilidad)

    def pivot_analysis(self):
        print("\n" + "═"*50)
        print("🧭 TABLA PIVOTE: PRODUCTO VS DEPARTAMENTO")
        print("═"*50)
        # Una tabla pivote es como un GroupBy pero en dos dimensiones
        pivot = self.df.pivot_table(values='Ventas_USD', index='Departamento', columns='Producto', fill_value=0)
        print(pivot)

if __name__ == "__main__":
    reporter = BusinessReporter()
    reporter.generate_report()
    reporter.pivot_analysis()
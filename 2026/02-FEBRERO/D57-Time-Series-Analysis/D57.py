"""
Proyecto: 365 Python Challenge
Día 57: Time Series Analysis
Objetivo: Analizar la evolución de ventas diarias y detectar tendencias visuales.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

class TimeSeriesAnalyzer:
    def __init__(self):
        # 1. Gestión de rutas profesional
        self.directorio = Path(__file__).parent.absolute()
        self.ruta_grafica = self.directorio / "tendencia_ventas.png"

        # 2. Generamos un dataset de ventas diarias (15 días simulados)
        data = {
            'Fecha': pd.date_range(start='2026-02-01', periods=15, freq='D'),
            'Ventas': [200, 220, 210, 250, 300, 280, 260, 310, 350, 400, 380, 420, 450, 440, 500]
        }
        self.df = pd.DataFrame(data)
        
        # 3. CRUCIAL: Establecer la fecha como el índice
        self.df.set_index('Fecha', inplace=True)

    def analyze_trends(self):
        print("📈 Analizando evolución temporal...")
        
        # Calculamos algunas métricas rápidas
        crecimiento_total = ((self.df['Ventas'].iloc[-1] - self.df['Ventas'].iloc[0]) / self.df['Ventas'].iloc[0]) * 100
        print(f"✅ Crecimiento en 15 días: {crecimiento_total:.2f}%")

        # 4. Creación del gráfico de tendencia
        plt.figure(figsize=(10, 6))
        plt.plot(self.df.index, self.df['Ventas'], marker='o', linestyle='-', color='#2c3e50', linewidth=2)
        
        # Estética profesional
        plt.title('Evolución de Ventas Diarias - Febrero 2026', fontsize=14, fontweight='bold')
        plt.xlabel('Día del Mes')
        plt.ylabel('Ventas (USD)')
        plt.grid(True, linestyle='--', alpha=0.6)
        
        # Rotar las fechas para que se lean mejor
        plt.xticks(rotation=45)
        
        # Guardado y cierre
        plt.tight_layout()
        plt.savefig(self.ruta_grafica, dpi=300)
        print(f"💾 Gráfica de tendencia guardada en: {self.ruta_grafica.name}")
        plt.show()

if __name__ == "__main__":
    analyzer = TimeSeriesAnalyzer()
    analyzer.analyze_trends()

    print("\n" + "═"*50)
    print("✨ HITO D57: Análisis Temporal Completado")
    print("═"*50)
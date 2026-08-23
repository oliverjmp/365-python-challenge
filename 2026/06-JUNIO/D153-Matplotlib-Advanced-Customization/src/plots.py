from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes

class CorporateDashboardPlotter:
    """Generador de gráficos analíticos avanzados usando la OOP API de Matplotlib."""
    
    def __init__(self, primary_color: str = "#1f77b4", secondary_color: str = "#ff7f0e") -> None:
        self.primary_color = primary_color
        self.secondary_color = secondary_color

    def create_dual_axis_analytics_chart(self, x_data: np.ndarray, y1_data: np.ndarray, y2_data: np.ndarray) -> Figure:
        """Crea un gráfico de doble eje con control milimétrico de capas y diseño corporativo."""
        # Creación explícita de Figure y Axes (OOP API)
        fig, ax1 = plt.subplots(figsize=(10, 5), dpi=100)

        # Capa 1: Gráfico de Líneas Principal (Eje Y Izquierdo)
        line = ax1.plot(
            x_data, y1_data, 
            color=self.primary_color, 
            linewidth=2.5, 
            marker='o', 
            label='Métrica Principal (Volumen)'
        )
        ax1.set_xlabel('Período Temporal', fontsize=12, fontweight='bold', labelpad=10)
        ax1.set_ylabel('Volumen Operativo', color=self.primary_color, fontsize=12, fontweight='bold')
        ax1.tick_params(axis='y', labelcolor=self.primary_color)
        ax1.grid(True, linestyle='--', alpha=0.5)

        # Capa 2: Eje Y Secundario superpuesto (Twin Axes)
        ax2 = ax1.twinx()
        bar = ax2.bar(
            x_data, y2_data, 
            color=self.secondary_color, 
            alpha=0.4, 
            width=0.4, 
            label='Métrica Secundaria (Eficiencia %)'
        )
        ax2.set_ylabel('Eficiencia (%)', color=self.secondary_color, fontsize=12, fontweight='bold')
        ax2.tick_params(axis='y', labelcolor=self.secondary_color)
        ax2.set_ylim(0, 100)
        
        # Eliminar rejilla secundaria para evitar saturación visual en el gráfico
        ax2.grid(False)

        # Título y diseño general limpio
        fig.suptitle('Dashboard Analítico Corporativo - Rendimiento Global', fontsize=14, fontweight='bold', y=0.98)
        
        # Unificación de leyendas de ambas capas de forma limpia
        lines_1, labels_1 = ax1.get_legend_handles_labels()
        lines_2, labels_2 = ax2.get_legend_handles_labels()
        ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', frameon=True, facecolor='white', edgecolor='none')

        fig.tight_layout()
        return fig
from __future__ import annotations
import matplotlib
matplotlib.use('Agg')  # ¡Fuerza el backend no interactivo para evitar errores de Tcl/Tk en Windows!

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class SeabornStatisticalPlotter:
    """Generador de gráficos estadísticos avanzados utilizando Seaborn y NumPy."""

    def __init__(self, random_state: int = 42) -> None:
        self.random_state = random_state
        sns.set_theme(style="whitegrid")

    def generate_synthetic_dataset(self, n_samples: int = 300) -> pd.DataFrame:
        """Genera un dataset sintético con correlaciones controladas usando NumPy."""
        np.random.seed(self.random_state)
        
        feature_a = np.random.normal(loc=50, scale=10, size=n_samples)
        feature_b = feature_a * 0.8 + np.random.normal(loc=10, scale=5, size=n_samples)
        feature_c = np.random.normal(loc=30, scale=15, size=n_samples)
        feature_d = -feature_a * 0.5 + np.random.normal(loc=100, scale=8, size=n_samples)

        df = pd.DataFrame({
            'Variable_A': feature_a,
            'Variable_B': feature_b,
            'Variable_C': feature_c,
            'Variable_D': feature_d
        })
        return df

    def create_correlation_heatmap(self, data: pd.DataFrame) -> Figure:
        """Crea un mapa de calor de correlación (correlation heatmap) estilizado."""
        corr_matrix = data.corr(method='pearson')
        
        fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
        sns.heatmap(
            corr_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap="coolwarm", 
            vmin=-1, 
            vmax=1, 
            cbar_kws={'label': 'Coeficiente de Correlación de Pearson'},
            ax=ax,
            linewidths=0.5
        )
        ax.set_title("Mapa de Calor de Correlación Estadística", fontsize=14, fontweight='bold', pad=15)
        fig.tight_layout()
        return fig

    def create_bivariate_distribution_plot(self, data: pd.DataFrame, x_col: str, y_col: str) -> Figure:
        """Crea un gráfico de distribución bivariada avanzado con KDE (Kernel Density Estimation)."""
        g = sns.jointplot(
            data=data, 
            x=x_col, 
            y=y_col, 
            kind="kde", 
            fill=True, 
            cmap="mako", 
            thresh=0.05
        )
        g.fig.suptitle(f"Distribución Bivariada y Densidad: {x_col} vs {y_col}", fontsize=12, fontweight='bold', y=1.03)
        g.fig.tight_layout()
        return g.fig
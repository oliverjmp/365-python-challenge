from __future__ import annotations
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class PlotlyInteractiveVisualizer:
    """Generador de gráficos interactivos avanzados con Plotly Express y Graph Objects."""

    def __init__(self, random_state: int = 42) -> None:
        self.random_state = random_state

    def generate_time_series_dataset(self, n_days: int = 100) -> pd.DataFrame:
        """Genera un dataset sintético de series temporales con tendencias y ruido."""
        np.random.seed(self.random_state)
        dates = pd.date_range(start="2026-01-01", periods=n_days, freq="D")
        
        base_trend = np.linspace(50, 150, n_days)
        noise_a = np.random.normal(loc=0, scale=10, size=n_days)
        noise_b = np.random.normal(loc=0, scale=15, size=n_days)
        
        series_a = base_trend + noise_a
        series_b = (base_trend * 0.8) + noise_b

        df = pd.DataFrame({
            'Fecha': dates,
            'Metrica_Principal': series_a,
            'Metrica_Secundaria': series_b,
            'Categoria': np.random.choice(['Alpha', 'Beta'], size=n_days)
        })
        return df

    def create_interactive_scatter(self, data: pd.DataFrame) -> go.Figure:
        """Crea un gráfico de dispersión interactivo con Plotly Express y tooltips dinámicos."""
        fig = px.scatter(
            data,
            x="Metrica_Principal",
            y="Metrica_Secundaria",
            color="Categoria",
            size="Metrica_Principal",
            hover_data=["Fecha"],
            title="Dispersión Interactiva con Tooltips Dinámicos",
            template="plotly_white"
        )
        fig.update_layout(
            xaxis_title="Métrica Principal (Eje X)",
            yaxis_title="Métrica Secundaria (Eje Y)",
            font=dict(family="Arial", size=12)
        )
        return fig

    def create_synchronized_subplots(self, data: pd.DataFrame) -> go.Figure:
        """Crea un gráfico de doble eje con subplots sincronizados usando Graph Objects."""
        fig = make_subplots(
            rows=2, cols=1, 
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=("Evolución Métrica Principal", "Evolución Métrica Secundaria")
        )

        # Trazado superior
        fig.add_trace(
            go.Scatter(
                x=data['Fecha'], 
                y=data['Metrica_Principal'],
                mode='lines+markers',
                name='Principal',
                line=dict(color='#1f77b4', width=2)
            ),
            row=1, col=1
        )

        # Trazado inferior
        fig.add_trace(
            go.Scatter(
                x=data['Fecha'], 
                y=data['Metrica_Secundaria'],
                mode='lines',
                name='Secundaria',
                line=dict(color='#ff7f0e', width=2),
                fill='tozeroy'
            ),
            row=2, col=1
        )

        fig.update_layout(
            title="Panel de Series Temporales con Ejes Sincronizados",
            hovermode="x unified",
            template="plotly_white",
            showlegend=False
        )
        return fig
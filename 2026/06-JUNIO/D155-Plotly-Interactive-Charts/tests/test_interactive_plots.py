import pytest
import pandas as pd
import plotly.graph_objects as go
from src.interactive_plots import PlotlyInteractiveVisualizer

@pytest.fixture
def visualizer():
    return PlotlyInteractiveVisualizer()

@pytest.fixture
def sample_data(visualizer):
    return visualizer.generate_time_series_dataset(n_days=50)

def test_generate_time_series_dataset(visualizer):
    """Valida la generación correcta del dataset de series temporales."""
    df = visualizer.generate_time_series_dataset(n_days=30)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 30
    assert 'Fecha' in df.columns
    assert 'Metrica_Principal' in df.columns

def test_create_interactive_scatter(visualizer, sample_data):
    """Valida que el gráfico de dispersión devuelva una instancia de go.Figure."""
    fig = visualizer.create_interactive_scatter(sample_data)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0

def test_create_synchronized_subplots(visualizer, sample_data):
    """Valida que el panel sincronizado devuelva una instancia de go.Figure con subplots."""
    fig = visualizer.create_synchronized_subplots(sample_data)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 2
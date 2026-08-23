import pytest
import pandas as pd
from matplotlib.figure import Figure
from src.stats_plots import SeabornStatisticalPlotter

@pytest.fixture
def plotter():
    return SeabornStatisticalPlotter()

@pytest.fixture
def sample_dataframe(plotter):
    return plotter.generate_synthetic_dataset(n_samples=100)

def test_generate_synthetic_dataset(plotter):
    """Valida la correcta creación del dataset sintético."""
    df = plotter.generate_synthetic_dataset(n_samples=50)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 50
    assert list(df.columns) == ['Variable_A', 'Variable_B', 'Variable_C', 'Variable_D']

def test_create_correlation_heatmap(plotter, sample_dataframe):
    """Valida que el mapa de calor retorne una instancia válida de Figure."""
    fig = plotter.create_correlation_heatmap(sample_dataframe)
    assert isinstance(fig, Figure)
    assert len(fig.axes) >= 1
    plt_close_safe(fig)

def test_create_bivariate_distribution_plot(plotter, sample_dataframe):
    """Valida que la distribución bivariada retorne una instancia válida de Figure."""
    fig = plotter.create_bivariate_distribution_plot(sample_dataframe, 'Variable_A', 'Variable_B')
    assert isinstance(fig, Figure)
    assert len(fig.axes) >= 1
    plt_close_safe(fig)

def plt_close_safe(fig):
    import matplotlib.pyplot as plt
    plt.close(fig)
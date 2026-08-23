import pytest
import numpy as np
import matplotlib.pyplot as plt  # <-- Asegúrate de incluir esta línea
from matplotlib.figure import Figure
from src.plots import CorporateDashboardPlotter

@pytest.fixture
def plotter():
    return CorporateDashboardPlotter(primary_color="#0A2540", secondary_color="#635BFF")

@pytest.fixture
def sample_data():
    x = np.array([1, 2, 3, 4, 5])
    y1 = np.array([100, 250, 400, 350, 500])
    y2 = np.array([45, 60, 85, 70, 95])
    return x, y1, y2

def test_create_dual_axis_chart_returns_figure(plotter, sample_data):
    """Valida que el método retorne una instancia válida de la clase Figure de Matplotlib."""
    x, y1, y2 = sample_data
    fig = plotter.create_dual_axis_analytics_chart(x, y1, y2)
    
    assert isinstance(fig, Figure)
    # Verificar que contenga al menos un eje principal y un eje gemelo
    assert len(fig.axes) >= 2
    
    # Cerrar la figura para liberar memoria en el entorno de pruebas
    plt.close(fig)

def test_plotter_custom_colors(plotter):
    """Valida la correcta asignación de paletas corporativas iniciales."""
    assert plotter.primary_color == "#0A2540"
    assert plotter.secondary_color == "#635BFF"
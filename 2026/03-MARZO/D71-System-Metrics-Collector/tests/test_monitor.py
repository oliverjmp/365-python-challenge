import pytest
from src.monitor import SystemMonitor

def test_monitor_inicializa_correctamente():
    monitor = SystemMonitor(cpu_threshold=50.0)
    assert monitor.cpu_threshold == 50.0

def test_check_metrics_devuelve_datos():
    monitor = SystemMonitor()
    metrics = monitor.check_metrics()
    assert "cpu" in metrics
    assert "memory" in metrics
    assert "disk" in metrics
    assert isinstance(metrics["cpu"], float)
def test_check_metrics_dispara_alerta():
    """Fuerza la ejecución de los bloques de advertencia (alertas) configurando umbrales mínimos."""
    # Configuramos umbrales en 0 para garantizar que cualquier uso de CPU o memoria active la alerta
    monitor = SystemMonitor(cpu_threshold=0.0, memory_threshold=0.0)
    metrics = monitor.check_metrics()
    
    # Verificamos que las métricas se obtuvieron y las alertas se evaluaron sin errores
    assert isinstance(metrics, dict)
    assert metrics["cpu"] >= 0.0
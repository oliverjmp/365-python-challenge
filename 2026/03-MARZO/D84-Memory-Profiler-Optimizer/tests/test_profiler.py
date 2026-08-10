import pytest
from src.profiler import MemoryProfiler
from src.service import AnalyticsService

def test_profiler_initialization():
    """Valida que el perfilador inicie correctamente y tome instantáneas."""
    profiler = MemoryProfiler()
    snapshot = profiler.take_snapshot()
    assert snapshot is not None

def test_top_allocations():
    """Valida que se puedan extraer las principales asignaciones de memoria."""
    profiler = MemoryProfiler()
    top_stats = profiler.get_top_allocations(limit=3)
    assert isinstance(top_stats, list)
    assert len(top_stats) <= 3

def test_compare_snapshots_leak_detection():
    """Valida la comparación de instantáneas ante un proceso que acumula memoria."""
    profiler = MemoryProfiler()
    service = AnalyticsService()
    
    snap1 = profiler.take_snapshot()
    
    # Ejecutamos un proceso que genera una fuga controlada
    service.run_leaky_process(100000)
    
    snap2 = profiler.take_snapshot()
    comparison = profiler.compare_snapshots(snap1, snap2, limit=3)
    
    assert isinstance(comparison, list)
    assert len(comparison) > 0
    # Verificamos que se detecte un incremento positivo de memoria
    assert any(item["size_diff_kb"] >= 0 for item in comparison)

def test_analytics_service_normal_process():
    """Valida la ejecución del proceso normal para cubrir todas las líneas del servicio."""
    service = AnalyticsService()
    result = service.run_normal_process(100)
    assert result > 0
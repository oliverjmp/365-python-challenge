import pytest
from src.analyzer import SQLIndexAnalyzer

def test_analyzer_initialization_and_data():
    """Valida la correcta inicialización, carga de datos de prueba y planes de ejecución."""
    analyzer = SQLIndexAnalyzer(db_url="sqlite:///:memory:")
    plan = analyzer.get_execution_plan("SELECT * FROM users WHERE username = 'user_500'")
    
    assert len(plan) > 0
    assert any("SCAN" in str(step.get("detail", "")).upper() or "SEARCH" in str(step.get("detail", "")).upper() for step in plan)

def test_create_index_and_optimization():
    """Valida la creación de índices y cómo se comporta el análisis de rendimiento."""
    analyzer = SQLIndexAnalyzer(db_url="sqlite:///:memory:")
    
    # Evaluar rendimiento antes de crear índice dedicado
    perf_before = analyzer.analyze_query_performance("SELECT * FROM users WHERE status = 'active'")
    assert perf_before["query"] != ""
    assert perf_before["plan_steps"] > 0

    # Crear índice en la columna status
    analyzer.create_index("idx_users_status", "users", "status")
    
    # Evaluar rendimiento después de crear el índice
    perf_after = analyzer.analyze_query_performance("SELECT * FROM users WHERE status = 'active'")
    assert perf_after["plan_steps"] > 0
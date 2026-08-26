import pytest
from src.metrics_decorator import MetricsAnalyzer

def test_ejecutar_consulta_analitica(duckdb_metrics_conn):
    analyzer = MetricsAnalyzer(duckdb_metrics_conn)
    resultados = analyzer.ejecutar_consulta_analitica()
    
    assert isinstance(resultados, list)
    assert len(resultados) == 3  # SELECT, INSERT, UPDATE
    assert resultados[0]["operacion"] == "SELECT"
    assert resultados[0]["total_filas"] == 650

def test_filtrar_por_operacion(duckdb_metrics_conn):
    analyzer = MetricsAnalyzer(duckdb_metrics_conn)
    resultados = analyzer.filtrar_por_operacion("SELECT")
    
    assert isinstance(resultados, list)
    assert len(resultados) == 2
    for row in resultados:
        assert row["operacion"] == "SELECT"

def test_decorador_manejo_excepciones_cobertura(duckdb_metrics_conn):
    analyzer = MetricsAnalyzer(duckdb_metrics_conn)
    # Llama explícitamente al método decorado que lanza la excepción para activar las líneas 20-23 y 65-67
    with pytest.raises(Exception):
        analyzer.ejecutar_consulta_fallida()
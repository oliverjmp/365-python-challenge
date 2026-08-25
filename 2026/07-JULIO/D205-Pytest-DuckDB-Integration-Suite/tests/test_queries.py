import pytest
from src.query_validator import QueryValidator

def test_calcular_total_por_estado(duckdb_memory_conn):
    validator = QueryValidator(duckdb_memory_conn)
    resultados = validator.calcular_total_por_estado()
    
    assert isinstance(resultados, list)
    assert len(resultados) == 2  # 'Completado' y 'Pendiente'
    
    # Validar el primer renglón correspondiente al mayor volumen acumulado
    assert resultados[0]["estado"] == "Completado"
    assert resultados[0]["total_transacciones"] == 5
    assert resultados[0]["monto_acumulado"] == 3391.48  # <-- Corregido a 3391.48

def test_filtrar_por_categoria(duckdb_memory_conn):
    validator = QueryValidator(duckdb_memory_conn)
    resultados = validator.filtrar_por_categoria("Hardware")
    
    assert isinstance(resultados, list)
    assert len(resultados) == 2
    for row in resultados:
        assert row["categoria"] == "Hardware"

def test_filtrar_por_categoria_case_insensitive(duckdb_memory_conn):
    validator = QueryValidator(duckdb_memory_conn)
    resultados = validator.filtrar_por_categoria("software")
    
    assert isinstance(resultados, list)
    assert len(resultados) == 2
    for row in resultados:
        assert row["categoria"] == "Software"
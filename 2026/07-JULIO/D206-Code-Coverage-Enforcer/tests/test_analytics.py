import pytest
from src.analytics_engine import AnalyticsEngine

def test_obtener_gasto_por_departamento(duckdb_audit_conn):
    engine = AnalyticsEngine(duckdb_audit_conn)
    resultado = engine.obtener_gasto_por_departamento()
    
    assert isinstance(resultado, list)
    assert len(resultado) == 3  # Ingeniería, Marketing, Ventas
    assert resultado[0]["departamento"] == "Ingeniería"
    assert resultado[0]["gasto_total"] == 5350.25

def test_filtrar_por_estado_aprobacion_true(duckdb_audit_conn):
    engine = AnalyticsEngine(duckdb_audit_conn)
    resultado = engine.filtrar_por_estado_aprobacion(True)
    
    assert isinstance(resultado, list)
    assert len(resultado) == 3
    for row in resultado:
        assert row["aprobado"] is True

def test_filtrar_por_estado_aprobacion_false(duckdb_audit_conn):
    engine = AnalyticsEngine(duckdb_audit_conn)
    resultado = engine.filtrar_por_estado_aprobacion(False)
    
    assert isinstance(resultado, list)
    assert len(resultado) == 2
    for row in resultado:
        assert row["aprobado"] is False
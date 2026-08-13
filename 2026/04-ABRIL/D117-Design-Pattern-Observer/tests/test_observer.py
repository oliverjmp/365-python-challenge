import pytest
from src.pipeline_observer import DataPipeline, LoggingObserver, MetricsObserver

def test_observer_attach_and_notify():
    pipeline = DataPipeline("etl_ventas")
    metrics_obs = MetricsObserver()
    
    pipeline.attach(metrics_obs)
    pipeline.run(100)
    
    assert "pipeline_started" in metrics_obs.events_received
    assert "pipeline_success" in metrics_obs.events_received

def test_observer_detach():
    pipeline = DataPipeline("etl_clientes")
    metrics_obs = MetricsObserver()
    
    pipeline.attach(metrics_obs)
    pipeline.detach(metrics_obs)
    pipeline.run(50)
    
    assert len(metrics_obs.events_received) == 0

def test_observer_detach_non_existent():
    """Valida la rama de código cuando se intenta desvincular un observador que no está registrado (Cubre línea 11)."""
    pipeline = DataPipeline("etl_edge_case")
    log_obs = LoggingObserver()
    
    # Intentamos remover un observador que nunca fue agregado
    pipeline.detach(log_obs)
    assert True

def test_pipeline_failure_notification():
    pipeline = DataPipeline("etl_fallido")
    metrics_obs = MetricsObserver()
    
    pipeline.attach(metrics_obs)
    pipeline.run(0) # Forzar error
    
    assert "pipeline_failed" in metrics_obs.events_received

def test_logging_observer():
    pipeline = DataPipeline("etl_logs")
    log_obs = LoggingObserver()
    
    pipeline.attach(log_obs)
    pipeline.run(10)
    assert True # Valida que no lance excepciones al notificar

def test_observer_detach_existing():
    """Valida la rama de código cuando se remueve un observador existente (Cubre línea 11)."""
    pipeline = DataPipeline("etl_edge_case")
    log_obs = LoggingObserver()
    
    # Agregamos el observador
    pipeline.attach(log_obs)
    assert len(pipeline._observers) == 1
    
    # Lo desvinculamos (esto ejecuta la línea 11 de remove con éxito)
    pipeline.detach(log_obs)
    assert len(pipeline._observers) == 0
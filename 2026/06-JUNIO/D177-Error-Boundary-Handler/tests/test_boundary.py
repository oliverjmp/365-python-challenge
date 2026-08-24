import pytest
from src.error_boundary import ErrorBoundary, ComponentRenderError, InterfaceError

def faulty_component():
    raise ComponentRenderError("Falló la carga de datos del widget.")

def normal_component(val: int):
    return val * 2

def test_error_boundary_catches_custom_exception():
    boundary = ErrorBoundary(fallback_message="Componente deshabilitado temporalmente.")
    
    result = boundary.catch(faulty_component)
    
    assert boundary.has_error is True
    assert isinstance(boundary.last_exception, ComponentRenderError)
    assert "Componente deshabilitado temporalmente" in result

def test_error_boundary_passes_normal_execution():
    boundary = ErrorBoundary()
    
    result = boundary.catch(normal_component, 21)
    
    assert boundary.has_error is False
    assert boundary.last_exception is None
    assert result == 42

def test_error_boundary_catches_generic_exception():
    """Valida que el boundary capture cualquier excepción general (Exception) y registre un error crítico."""
    boundary = ErrorBoundary(fallback_message="Error crítico recuperado.")
    
    def faulty_general_component():
        raise RuntimeError("Fallo inesperado del sistema.")
        
    result = boundary.catch(faulty_general_component)
    
    assert boundary.has_error is True
    assert isinstance(boundary.last_exception, RuntimeError)
    assert "Error crítico recuperado" in result
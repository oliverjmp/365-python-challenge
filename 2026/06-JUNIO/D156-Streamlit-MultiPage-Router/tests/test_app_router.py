import pytest
from src.app_router import StreamlitRouter

def dummy_view():
    pass

def test_router_initialization():
    """Valida la correcta inicialización del router."""
    router = StreamlitRouter()
    assert isinstance(router.routes, dict)
    assert len(router.routes) == 0

def test_register_route_success():
    """Valida el registro exitoso de una vista."""
    router = StreamlitRouter()
    router.register_route("Admin", dummy_view)
    assert "Admin" in router.routes
    assert router.routes["Admin"] == dummy_view

def test_register_route_invalid_raises_error():
    """Valida que un nombre de ruta vacío o función no ejecutable lance ValueError."""
    router = StreamlitRouter()
    with pytest.raises(ValueError):
        router.register_route("", dummy_view)
    with pytest.raises(ValueError):
        router.register_route("Invalid", "not_a_function") # type: ignore

def test_render_navigation_success(monkeypatch):
    """Valida la ejecución correcta de una ruta registrada."""
    router = StreamlitRouter()
    executed = []
    
    def mock_view():
        executed.append(True)

    router.register_route("Cliente", mock_view)
    router.render_navigation("Cliente")
    
    assert len(executed) == 1
    assert executed[0] is True

def test_render_navigation_not_found_raises_error():
    """Valida que buscar una ruta inexistente lance KeyError."""
    router = StreamlitRouter()
    with pytest.raises(KeyError):
        router.render_navigation("RutaInexistente")
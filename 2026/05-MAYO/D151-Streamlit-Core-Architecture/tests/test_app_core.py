import pytest
from src.app_core import StreamlitCoreManager

def test_initialize_state():
    """Valida que el estado inicial se configure con valores por defecto."""
    manager = StreamlitCoreManager()
    fake_state = {}
    
    manager.initialize_state(fake_state)
    assert fake_state["counter"] == 0
    assert fake_state["user_name"] == "Invitado"

def test_increment_counter():
    """Valida el incremento correcto del contador en el estado."""
    manager = StreamlitCoreManager()
    fake_state = {"counter": 5}
    
    new_val = manager.increment_counter(fake_state)
    assert new_val == 6
    assert fake_state["counter"] == 6

def test_increment_counter_missing_state():
    """Valida que incremente desde cero si la clave no existe en el estado."""
    manager = StreamlitCoreManager()
    fake_state = {}
    
    new_val = manager.increment_counter(fake_state)
    assert new_val == 1
    assert fake_state["counter"] == 1

def test_update_user_name():
    """Valida la actualización correcta del nombre de usuario."""
    manager = StreamlitCoreManager()
    fake_state = {"user_name": "Invitado"}
    
    updated = manager.update_user_name(fake_state, "Oliver")
    assert updated == "Oliver"
    assert fake_state["user_name"] == "Oliver"

def test_update_user_name_empty():
    """Valida que un nombre vacío o nulo asigne por defecto 'Invitado'."""
    manager = StreamlitCoreManager()
    fake_state = {}
    
    updated = manager.update_user_name(fake_state, "   ")
    assert updated == "Invitado"
    assert fake_state["user_name"] == "Invitado"
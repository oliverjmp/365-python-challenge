import pytest
import streamlit as st
from src.views_admin import render_admin_view
from src.views_client import render_client_view

def test_render_admin_view(monkeypatch):
    """Valida la ejecución correcta de la vista de administración."""
    # Mock de las funciones de Streamlit para evitar llamadas reales a UI en entorno de test headless
    monkeypatch.setattr(st, "header", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "write", lambda *args, **kwargs: None)
    
    # Mock de columnas y métricas
    class MockColumn:
        def metric(self, *args, **kwargs):
            pass

    monkeypatch.setattr(st, "columns", lambda n: [MockColumn() for _ in range(n)])
    
    # Ejecución sin excepciones
    render_admin_view()
    assert True

def test_render_client_view(monkeypatch):
    """Valida la ejecución correcta de la vista de clientes."""
    monkeypatch.setattr(st, "header", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "write", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "info", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "selectbox", lambda label, options: options[0])
    
    # Ejecución sin excepciones
    render_client_view()
    assert True
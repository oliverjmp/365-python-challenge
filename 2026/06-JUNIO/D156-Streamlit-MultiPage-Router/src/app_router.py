from __future__ import annotations
import streamlit as st
from typing import Callable, Dict

class StreamlitRouter:
    """Gestor de rutas y navegación multipágina basado en perfiles de usuario."""

    def __init__(self) -> None:
        self.routes: Dict[str, Callable[[], None]] = {}

    def register_route(self, page_name: str, render_func: Callable[[], None]) -> None:
        """Registra una vista asociada a una ruta o rol."""
        if not page_name or not callable(render_func):
            raise ValueError("El nombre de la página debe ser válido y la vista ejecutable.")
        self.routes[page_name] = render_func

    def render_navigation(self, selected_page: str) -> None:
        """Renderiza la página seleccionada validando su existencia en el sistema."""
        if selected_page not in self.routes:
            raise KeyError(f"La ruta '{selected_page}' no se encuentra registrada en el router.")
        
        view_func = self.routes[selected_page]
        view_func()
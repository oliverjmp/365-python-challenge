import logging
from typing import Callable, Any

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class InterfaceError(Exception):
    """Excepción base para errores ocurridos en la interfaz de usuario."""
    pass

class ComponentRenderError(InterfaceError):
    """Lanzada cuando un componente de la interfaz falla al renderizarse."""
    pass

class ErrorBoundary:
    """Implementación del patrón Error Boundary para captura y gestión segura de excepciones."""
    
    def __init__(self, fallback_message: str = "Ha ocurrido un error inesperado en este componente."):
        self.fallback_message = fallback_message
        self.has_error = False
        self.last_exception = None

    def catch(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        """Ejecuta una función envuelta en un límite de error (try-except seguro)."""
        try:
            self.has_error = False
            self.last_exception = None
            return func(*args, **kwargs)
        except InterfaceError as e:
            self.has_error = True
            self.last_exception = e
            logging.error(f"[InterfaceError Capturada]: {e}")
            return self._render_fallback()
        except Exception as e:
            self.has_error = True
            self.last_exception = e
            logging.critical(f"[Error Crítico No Controlado]: {e}")
            return self._render_fallback()

    def _render_fallback(self) -> str:
        """Retorna un componente o mensaje alternativo de respaldo (UI Fallback)."""
        return f"⚠️ [Error Boundary Active]: {self.fallback_message}"
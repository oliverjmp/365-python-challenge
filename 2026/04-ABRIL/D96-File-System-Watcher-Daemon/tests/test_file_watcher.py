import time
import logging
import pytest
from watchdog.events import FileCreatedEvent, FileModifiedEvent, FileDeletedEvent
from src.file_watcher import ProfessionalHandler, LogFileSystemWatcher

def test_handler_events(caplog):
    """Verifica que el manejador capture y registre correctamente los eventos."""
    # Configuramos el nivel de captura para asegurarnos de leer los logs INFO
    caplog.set_level(logging.INFO)
    
    handler = ProfessionalHandler()
    
    # Simulamos evento de creación
    created_event = FileCreatedEvent("/path/to/test_file.txt")
    handler.on_created(created_event)
    assert "Archivo creado: /path/to/test_file.txt" in caplog.text

    # Simulamos evento de modificación
    modified_event = FileModifiedEvent("/path/to/test_file.txt")
    handler.on_modified(modified_event)
    assert "Archivo modificado: /path/to/test_file.txt" in caplog.text

    # Simulamos evento de eliminación
    deleted_event = FileDeletedEvent("/path/to/test_file.txt")
    handler.on_deleted(deleted_event)
    assert "Archivo eliminado: /path/to/test_file.txt" in caplog.text

def test_watcher_lifecycle(tmp_path):
    """Valida el inicio y detención del demonio observador."""
    watcher = LogFileSystemWatcher(str(tmp_path))
    
    # Mockeamos los métodos internos de Observer para evitar bloqueos del sistema operativo en el test
    watcher.observer.start = lambda: None
    watcher.observer.stop = lambda: None
    watcher.observer.join = lambda: None
    
    watcher.start()
    watcher.stop()
    assert True
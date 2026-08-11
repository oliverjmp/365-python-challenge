import time
import logging
import shutil
import os
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent

# Configuración básica de logs profesionales
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ExcelProcessorHandler(FileSystemEventHandler):
    """Manejador que detecta archivos de Excel y procesa su contenido mediante copias temporales."""
    
    def _process_excel(self, file_path: str) -> None:
        """Lee el Excel copiándolo previamente a un archivo temporal para evitar bloqueos de Windows."""
        temp_file = file_path + ".tmp"
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                # Damos un pequeño respiro para estabilidad del sistema operativo
                time.sleep(0.5)
                
                # Usamos shutil para copiar el archivo original de forma segura
                shutil.copy2(file_path, temp_file)
                
                # Leemos la copia temporal usando pandas
                df = pd.read_excel(temp_file)
                
                logging.info(f"--- Procesando contenido del Excel: {file_path} ---")
                logging.info(f"Dimensiones de la tabla: {df.shape[0]} filas y {df.shape[1]} columnas.")
                if not df.empty:
                    logging.info(f"Primeras filas:\n{df.head(3)}")
                else:
                    logging.info("El archivo de Excel está vacío actualmente.")
                
                # Usamos os para eliminar el archivo temporal limpiamente
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                return 

            except PermissionError:
                if attempt < max_retries - 1:
                    logging.warning(f"Archivo bloqueado por Excel (Intento {attempt + 1}/{max_retries}). Reintentando...")
                    time.sleep(1.0)
                else:
                    logging.error(f"No se pudo acceder a {file_path} porque sigue abierto en Excel.")
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
            except Exception as e:
                logging.error(f"Error inesperado al procesar el archivo: {e}")
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                break

    def on_created(self, event: FileSystemEvent) -> None:
        if not event.is_directory and event.src_path.endswith(('.xlsx', '.xls')):
            logging.info(f"Nuevo archivo Excel detectado: {event.src_path}")
            self._process_excel(event.src_path)

    def on_modified(self, event: FileSystemEvent) -> None:
        if not event.is_directory and event.src_path.endswith(('.xlsx', '.xls')):
            logging.info(f"Archivo Excel modificado: {event.src_path}")
            self._process_excel(event.src_path)

    def on_deleted(self, event: FileSystemEvent) -> None:
        if not event.is_directory and event.src_path.endswith(('.xlsx', '.xls')):
            logging.info(f"Archivo Excel eliminado: {event.src_path}")


class LogFileSystemWatcher:
    """Controlador principal del demonio de monitoreo."""
    
    def __init__(self, watch_directory: str):
        self.watch_directory = watch_directory
        self.event_handler = ExcelProcessorHandler()
        self.observer = Observer()

    def start(self) -> None:
        """Inicia el observador en segundo plano."""
        self.observer.schedule(self.event_handler, path=self.watch_directory, recursive=False)
        self.observer.start()
        logging.info(f"Iniciando monitoreo de archivos Excel en: {self.watch_directory}")

    def stop(self) -> None:
        """Detiene de forma segura el observador."""
        self.observer.stop()
        self.observer.join()
        logging.info("Monitoreo detenido.")
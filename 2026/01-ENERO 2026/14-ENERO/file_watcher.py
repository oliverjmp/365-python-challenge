import time
import logging
import os
from datetime import datetime

# -----------------------------------------
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# -----------------------------------------
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "file_watcher.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------------
# FUNCIÓN PRINCIPAL DE MONITOREO
# -----------------------------------------
def monitorear_carpeta(ruta, intervalo=3):
    """
    Monitorea una carpeta y detecta:
    - Nuevos archivos
    - Archivos eliminados
    - Archivos modificados
    """

    print(f"🔍 Monitoreando carpeta: {ruta}")
    logging.info(f"Iniciando monitoreo en: {ruta}")

    # Estado inicial
    estado_anterior = {}

    # Cargar estado inicial
    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            estado_anterior[archivo] = os.path.getmtime(ruta_archivo)

    # Loop infinito de monitoreo
    while True:
        time.sleep(intervalo)
        estado_actual = {}

        for archivo in os.listdir(ruta):
            ruta_archivo = os.path.join(ruta, archivo)
            if os.path.isfile(ruta_archivo):
                estado_actual[archivo] = os.path.getmtime(ruta_archivo)

        # Detectar nuevos archivos
        nuevos = set(estado_actual.keys()) - set(estado_anterior.keys())
        for archivo in nuevos:
            mensaje = f"🟢 Nuevo archivo detectado: {archivo}"
            print(mensaje)
            logging.info(mensaje)

        # Detectar archivos eliminados
        eliminados = set(estado_anterior.keys()) - set(estado_actual.keys())
        for archivo in eliminados:
            mensaje = f"🔴 Archivo eliminado: {archivo}"
            print(mensaje)
            logging.warning(mensaje)

        # Detectar archivos modificados
        for archivo in estado_actual:
            if archivo in estado_anterior:
                if estado_actual[archivo] != estado_anterior[archivo]:
                    mensaje = f"🟡 Archivo modificado: {archivo}"
                    print(mensaje)
                    logging.info(mensaje)

        estado_anterior = estado_actual.copy()


# -----------------------------------------
# EJECUCIÓN DIRECTA
# -----------------------------------------
if __name__ == "__main__":
    carpeta_a_monitorear = "watch_folder"

    # Crear carpeta si no existe
    os.makedirs(carpeta_a_monitorear, exist_ok=True)

    monitorear_carpeta(carpeta_a_monitorear)

import os
import shutil
import json
import logging
from datetime import datetime

# -----------------------------------------
# Cargar configuración
# -----------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

SOURCE_PATH = os.path.join(BASE_DIR, config["source_path"])
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
MAX_BACKUPS = config["max_backups"]

# -----------------------------------------
# Configuración de logs
# -----------------------------------------
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "backup.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------------
# Crear backup con timestamp
# -----------------------------------------
def crear_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"

    destino = os.path.join(BACKUP_DIR, backup_name)
    os.makedirs(BACKUP_DIR, exist_ok=True)

    try:
        if os.path.isfile(SOURCE_PATH):
            shutil.copy2(SOURCE_PATH, destino)
        else:
            shutil.copytree(SOURCE_PATH, destino)

        logging.info(f"Backup creado: {backup_name}")
        print(f"🟢 Backup creado: {backup_name}")

    except Exception as e:
        logging.error(f"Error creando backup: {e}")
        print(f"🔴 Error creando backup: {e}")

# -----------------------------------------
# Limpiar backups antiguos
# -----------------------------------------
def limpiar_backups():
    backups = sorted(os.listdir(BACKUP_DIR))

    if len(backups) > MAX_BACKUPS:
        excedentes = backups[:-MAX_BACKUPS]

        for backup in excedentes:
            ruta = os.path.join(BACKUP_DIR, backup)
            try:
                if os.path.isfile(ruta):
                    os.remove(ruta)
                else:
                    shutil.rmtree(ruta)

                logging.info(f"Backup eliminado: {backup}")
                print(f"🟡 Backup eliminado: {backup}")

            except Exception as e:
                logging.error(f"Error eliminando backup: {e}")
                print(f"🔴 Error eliminando backup: {e}")

# -----------------------------------------
# Ejecución principal
# -----------------------------------------
if __name__ == "__main__":
    crear_backup()
    limpiar_backups()

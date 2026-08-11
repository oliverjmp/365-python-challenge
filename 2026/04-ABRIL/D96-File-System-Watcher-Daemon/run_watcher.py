import time
import os
from src.file_watcher import LogFileSystemWatcher

if __name__ == "__main__":
    # Apuntamos a la carpeta 'entrada' que acabamos de crear
    target_directory = "./entrada"
    
    # Nos aseguramos de que la carpeta exista físicamente
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Iniciamos el observador
    watcher = LogFileSystemWatcher(target_directory)
    watcher.start()

    print(f"\n[MONITOREO ACTIVO] Observando la carpeta: {os.path.abspath(target_directory)}")
    print("Coloca, modifica o guarda tu archivo 'product.xlsx' dentro de esta carpeta.")
    print("Presiona Ctrl + C para salir...\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()
        print("\n[MONITOREO DETENIDO] El demonio se ha cerrado correctamente.")
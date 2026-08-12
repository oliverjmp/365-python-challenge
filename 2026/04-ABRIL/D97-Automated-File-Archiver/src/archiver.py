import shutil
from pathlib import Path
from datetime import datetime
import logging

class AutomatedFileArchiver:
    def __init__(self, base_dir: str = "./data"):
        self.base_path = Path(base_dir)
        self.entrada = self.base_path / "entrada"
        self.clasificados = self.base_path / "clasificados"
        self.respaldos = self.base_path / "respaldos"

    def process_files(self):
        logging.info(f"[*] Iniciando proceso de archivado en: {self.base_path}")
        
        # Asegurar directorios
        self.entrada.mkdir(parents=True, exist_ok=True)
        self.clasificados.mkdir(parents=True, exist_ok=True)
        self.respaldos.mkdir(parents=True, exist_ok=True)
        
        # 1. Clasificar archivos
        archivos_movidos = 0
        for archivo in self.entrada.iterdir():
            if archivo.is_file():
                ext = archivo.suffix.lower().replace(".", "")
                if not ext:
                    ext = "sin_extension"
                dest_dir = self.clasificados / ext
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                shutil.move(str(archivo), str(dest_dir / archivo.name))
                logging.info(f"[+] Clasificado: {archivo.name} -> {ext}/")
                archivos_movidos += 1

        # 2. Comprimir clasificados si hay elementos
        if any(self.clasificados.iterdir()):
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_zip = self.respaldos / f"backup_{fecha}"
            shutil.make_archive(str(nombre_zip), 'zip', str(self.clasificados))
            logging.info(f"[!] Respaldo creado exitosamente: {nombre_zip}.zip")
        else:
            logging.info("[-] No hay archivos para respaldar.")

    # Alias por compatibilidad
    def organizar_y_respaldar(self):
        return self.process_files()

if __name__ == "__main__":
    archiver = AutomatedFileArchiver()
    archiver.process_files()
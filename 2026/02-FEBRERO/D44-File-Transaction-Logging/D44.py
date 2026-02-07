"""
Proyecto: 365 Python Challenge
Día 44: File Transaction Logging
Objetivo: Registrar cada movimiento de archivo en un log de auditoría persistente.
"""

import shutil
from pathlib import Path
from datetime import datetime

class AuditOrganizer:
    def __init__(self):
        # Definición de rutas base
        self.base_path = Path(__file__).parent.absolute()
        self.source_dir = self.base_path / "Workspace_Prueba"
        self.log_file = self.base_path / "file_transactions.log"
        
        # Aseguramos que la carpeta raíz del proceso exista
        self.source_dir.mkdir(parents=True, exist_ok=True)

    def write_log(self, message: str):
        """
        Escribe una entrada en el log de auditoría.
        Usa el modo 'a' (append) para no borrar registros anteriores.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message}\n")
        except Exception as e:
            print(f"❌ Error crítico escribiendo en el log: {e}")

    def process_and_log(self):
        """Escanea archivos y registra cada movimiento físicamente."""
        print(f"🚀 Iniciando sesión de auditoría en: {self.source_dir}")
        self.write_log("--- NUEVA SESIÓN DE AUTOMATIZACIÓN INICIADA ---")

        # Buscamos todos los archivos en la raíz del workspace
        files_to_process = [f for f in self.source_dir.iterdir() if f.is_file()]
        
        if not files_to_process:
            msg = "INFO: No se encontraron archivos para procesar."
            self.write_log(msg)
            print(f"ℹ️ {msg}")
            return

        # Definir y crear carpeta de destino
        dest_folder = self.source_dir / "Logs_Procesados"
        dest_folder.mkdir(exist_ok=True)

        for item in files_to_process:
            dest_path = dest_folder / item.name
            
            try:
                # Realizamos el movimiento físico
                shutil.move(str(item), str(dest_path))
                
                # Registro de éxito con ruta relativa para limpieza visual
                rel_dest = dest_path.relative_to(self.base_path)
                log_msg = f"SUCCESS: '{item.name}' movido a '{rel_dest}'"
                self.write_log(log_msg)
                print(f"✅ {log_msg}")
                
            except Exception as e:
                # Registro de error en el rastro de auditoría
                error_msg = f"ERROR: Fallo al mover '{item.name}'. Motivo: {e}"
                self.write_log(error_msg)
                print(f"❌ {error_msg}")

        self.write_log("--- SESIÓN FINALIZADA CORRECTAMENTE ---\n")

if __name__ == "__main__":
    # --- FIX DE SEGURIDAD: Inicialización del Entorno ---
    # 1. Definimos la carpeta de trabajo
    work_dir = Path(__file__).parent.absolute() / "Workspace_Prueba"
    
    # 2. Creamos la carpeta ANTES de intentar tocar cualquier archivo dentro
    work_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. Creamos un archivo de prueba para procesar
    test_file = work_dir / "documento_importante.pdf"
    test_file.touch() # Ahora sí funcionará porque el 'padre' existe
    print(f"📝 Archivo de prueba creado: {test_file.name}")

    # 4. Ejecutamos el sistema de auditoría
    bot = AuditOrganizer()
    bot.process_and_log()
    
    print(f"\n📄 Proceso terminado. Registro guardado en: {bot.log_file.name}")
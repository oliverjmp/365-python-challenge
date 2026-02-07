"""
Proyecto: 365 Python Challenge
Día 42: Bulk Rename & Timestamping
Objetivo: Renombrar archivos agregando fecha y organizarlos.
"""

import shutil
from pathlib import Path
from datetime import datetime

class TimestampRenamer:
    def __init__(self):
        # Usamos el workspace del día anterior para dar continuidad
        self.source_dir = Path(__file__).parent.absolute() / "Workspace_Prueba"
        self.timestamp = datetime.now().strftime("%Y-%m-%d")
        
        # Mapa de categorías (mismo del D41)
        self.categories = {
            "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
            "Imagenes": [".jpg", ".jpeg", ".png"],
            "Otros": []
        }

    def process_files(self):
        if not self.source_dir.exists():
            print("❌ El directorio de prueba no existe. Ejecuta el D41 primero.")
            return

        print(f"🚀 Iniciando Renombrado y Organización: {self.source_dir}")

        # Iterar sobre archivos (solo archivos, no carpetas de categorías)
        for item in self.source_dir.iterdir():
            if item.is_file():
                # 1. Obtener categoría
                category = self.get_category(item.suffix.lower())
                
                # 2. Crear nombre con Timestamp: 2026-02-10_Original.ext
                new_name = f"{self.timestamp}_{item.name}"
                
                # 3. Definir destino
                dest_folder = self.source_dir / category
                dest_folder.mkdir(exist_ok=True)
                dest_path = dest_folder / new_name

                # 4. Renombrar y Mover
                try:
                    shutil.move(str(item), str(dest_path))
                    print(f"✅ Procesado: {item.name} -> {category}/{new_name}")
                except Exception as e:
                    print(f"❌ Error con {item.name}: {e}")

    def get_category(self, extension):
        for cat, exts in self.categories.items():
            if extension in exts:
                return cat
        return "Otros"

if __name__ == "__main__":
    # Para probarlo, vamos a crear un par de archivos nuevos antes
    base = Path(__file__).parent.absolute() / "Workspace_Prueba"
    base.mkdir(exist_ok=True)
    (base / "reporte_ventas.xlsx").touch()
    (base / "perfil_usuario.png").touch()

    renamer = TimestampRenamer()
    print("\n" + "="*50)
    print("🏷️ D42: BULK RENAME & TIMESTAMPING ACTIVADO")
    print("="*50)
    
    renamer.process_files()
    print("\n✨ ¡Proceso de versionamiento completado!")
"""
Proyecto: 365 Python Challenge
Día 41: Smart File Organizer
Objetivo: Organizar automáticamente archivos por extensión en carpetas.
"""

import os
import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self):
        # Definimos la ruta a organizar (por defecto, donde esté el script)
        self.target_dir = Path(__file__).parent.absolute() / "Workspace_Prueba"
        
        # Crear la carpeta de prueba si no existe para no desordenar tu PC real aún
        if not self.target_dir.exists():
            self.target_dir.mkdir()
            self.create_dummy_files()

        # Mapa de extensiones por categoría
        self.extensions = {
            "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
            "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
            "Ejecutables": [".exe", ".msi", ".bat", ".sh"],
            "Comprimidos": [".zip", ".rar", ".7z", ".tar"],
            "Otros": []
        }

    def create_dummy_files(self):
        """Crea archivos vacíos para probar la organización."""
        filenames = ["test.pdf", "foto.jpg", "notas.txt", "programa.exe", "datos.xlsx", "vacaciones.png"]
        for f in filenames:
            (self.target_dir / f).touch()
        print(f"✅ Entorno de prueba creado en: {self.target_dir}")

    def organize(self):
        print(f"🚀 Iniciando organización en: {self.target_dir}")
        
        # Iterar sobre los archivos en el directorio
        for file_path in self.target_dir.iterdir():
            # Ignorar carpetas
            if file_path.is_dir():
                continue
            
            # Obtener la extensión
            ext = file_path.suffix.lower()
            moved = False
            
            # Buscar a qué categoría pertenece
            for category, ext_list in self.extensions.items():
                if ext in ext_list:
                    self.move_file(file_path, category)
                    moved = True
                    break
            
            # Si no está en ninguna categoría, va a "Otros"
            if not moved:
                self.move_file(file_path, "Otros")

    def move_file(self, file_path, category):
        # Crear la carpeta de la categoría si no existe
        dest_dir = self.target_dir / category
        dest_dir.mkdir(exist_ok=True)
        
        # Mover el archivo
        try:
            shutil.move(str(file_path), str(dest_dir / file_path.name))
            print(f"📦 [MOVIDO] {file_path.name} -> {category}/")
        except Exception as e:
            print(f"❌ Error moviendo {file_path.name}: {e}")

if __name__ == "__main__":
    organizer = FileOrganizer()
    print("\n" + "="*50)
    print("📂 D41: SMART FILE ORGANIZER ACTIVADO")
    print("="*50)
    
    confirm = input(f"¿Deseas organizar los archivos en '{organizer.target_dir}'? (s/n): ")
    if confirm.lower() == 's':
        organizer.organize()
        print("\n✨ ¡Limpieza completada!")
    else:
        print("❌ Operación cancelada.")
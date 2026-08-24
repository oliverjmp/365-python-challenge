import os
from typing import List

def get_project_docs_status(docs_dir: str = "docs") -> List[str]:
    """Valida la existencia de la carpeta de documentación y lista los archivos Markdown disponibles."""
    if not os.path.exists(docs_dir):
        return []
    
    files = [f for f in os.listdir(docs_dir) if f.endswith(".md")]
    return files

def generate_doc_summary(project_name: str) -> str:
    """Genera una cabecera resumida para la automatización documental."""
    return f"=== Documentación Oficial para: {project_name} ==="
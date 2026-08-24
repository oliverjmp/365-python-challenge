import os
from typing import List

def verify_semiannual_modules(base_path: str = ".") -> List[str]:
    """Verifica y lista los componentes clave consolidados en el bloque semestral."""
    if not os.path.exists(base_path):
        return []
    
    # Simula la validación de directorios o entregables del semestre
    expected_artifacts = ["requirements.txt", "README.md", "src"]
    found = [item for item in expected_artifacts if os.path.exists(os.path.join(base_path, item))]
    return found

def generate_consolidation_report(block_name: str) -> str:
    """Genera un reporte textual de cierre para el bloque semestral."""
    return f"=== Cierre Exitoso del Bloque: {block_name} ==="
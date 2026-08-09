import json
import os

class ArchitectureAuditor:
    """Auditor de integridad estructural para módulos del trimestre."""

    def __init__(self, json_path: str):
        self.json_path = json_path

    def load_manifest(self) -> dict:
        """Carga el archivo JSON con el manifiesto de módulos."""
        if not os.path.exists(self.json_path):
            return {"modules": []}
        with open(self.json_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def audit_modules(self) -> dict:
        """Verifica la existencia de los archivos clave especificados en el manifiesto."""
        manifest = self.load_manifest()
        results = {"total": 0, "passed": 0, "failed": 0, "details": []}

        for mod in manifest.get("modules", []):
            results["total"] += 1
            path = mod.get("path")
            exists = os.path.exists(path) if path else False

            if exists:
                results["passed"] += 1
            else:
                results["failed"] += 1

            results["details"].append({
                "name": mod.get("name"),
                "path": path,
                "status": "OK" if exists else "MISSING"
            })

        return results
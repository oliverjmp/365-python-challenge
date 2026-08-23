from __future__ import annotations
import os
import json
from typing import Dict, Any, List

class ArchitectureAuditor:
    """Motor de auditoría integral para validar el estado, rendimiento y métricas de los componentes del semestre."""

    def __init__(self, audit_registry_path: str) -> None:
        if not audit_registry_path or not audit_registry_path.endswith(".json"):
            raise ValueError("La ruta del registro de auditoría debe ser un archivo JSON válido.")
        self.audit_registry_path = audit_registry_path

    def load_registry_data(self) -> Dict[str, Any]:
        """Carga y parsea el archivo JSON de registro de componentes del semestre."""
        if not os.path.exists(self.audit_registry_path):
            raise FileNotFoundError(f"No se encontró el archivo de registro en: {self.audit_registry_path}")

        try:
            with open(self.audit_registry_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    raise ValueError("El formato del registro JSON debe ser un diccionario raíz.")
                return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Error de sintaxis en el archivo JSON de registro: {str(e)}")
        except Exception as e:
            if isinstance(e, (FileNotFoundError, ValueError)):
                raise e
            raise RuntimeError(f"Error crítico al leer el registro de arquitectura: {str(e)}")

    def audit_component_performance(self, components: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Evalúa las métricas de rendimiento y cobertura de los componentes auditados."""
        if not components:
            raise ValueError("La lista de componentes a auditar no puede estar vacía.")

        total_components = len(components)
        fully_covered = 0
        total_coverage_percentage = 0.0
        flagged_components = []

        for comp in components:
            name = comp.get("name", "Desconocido")
            coverage = comp.get("coverage_percentage", 0.0)
            status = comp.get("status", "pending")

            if not isinstance(coverage, (int, float)) or not (0.0 <= coverage <= 100.0):
                raise ValueError(f"El componente '{name}' tiene un porcentaje de cobertura inválido: {coverage}")

            total_coverage_percentage += coverage

            if coverage == 100.0 and status == "active":
                fully_covered += 1
            else:
                flagged_components.append(name)

        average_coverage = total_coverage_percentage / total_components

        audit_summary = {
            "total_components": total_components,
            "fully_covered_count": fully_covered,
            "average_coverage": round(average_coverage, 2),
            "flagged_components": flagged_components,
            "audit_status": "PASSED" if average_coverage >= 95.0 else "REVIEW_REQUIRED"
        }

        return audit_summary

    def generate_report(self, components: List[Dict[str, Any]], output_report_path: str) -> str:
        """Genera un informe consolidado de auditoría en formato JSON."""
        if not output_report_path or not output_report_path.endswith(".json"):
            raise ValueError("La ruta del informe de salida debe ser un archivo JSON válido.")

        try:
            summary = self.audit_component_performance(components)
            report_payload = {
                "audit_metadata": {
                    "target_registry": self.audit_registry_path,
                    "semestre": "Junio - 2026",
                    "framework": "Python Core Architecture Audit"
                },
                "summary": summary
            }

            with open(output_report_path, 'w', encoding='utf-8') as f:
                json.dump(report_payload, f, indent=4, ensure_ascii=False)

            return output_report_path

        except Exception as e:
            if isinstance(e, ValueError):
                raise e
            raise RuntimeError(f"Error crítico al generar el informe de auditoría: {str(e)}")
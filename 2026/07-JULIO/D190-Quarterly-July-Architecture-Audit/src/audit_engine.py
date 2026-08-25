import json
import os
from typing import Dict, List, Any
from pydantic import BaseModel, Field, ValidationError

class ComponentAuditSchema(BaseModel):
    """Esquema de validación estricta para cada componente auditado en la arquitectura."""
    component_id: str = Field(..., min_length=3, description="Identificador único del módulo")
    name: str = Field(..., description="Nombre descriptivo del subsistema")
    status: str = Field(..., pattern=r"^(CONFORME|ADVERTENCIA|CRITICO)$", description="Estado operativo")
    performance_score: float = Field(..., ge=0.0, le=100.0, description="Puntuación de rendimiento (0-100)")

class ArchitectureAuditReport(BaseModel):
    """Esquema global del informe de auditoría trimestral de julio."""
    quarter: str = Field(..., description="Trimestre evaluado")
    phase: str = Field(..., description="Fase de desarrollo actual")
    components: List[ComponentAuditSchema] = Field(..., description="Lista de componentes auditados")

class QuarterlyArchitectureAuditor:
    """Motor encargado de consolidar, auditar y validar esquemas de arquitectura de sistemas."""
    
    def __init__(self, storage_path: str = "data_lake/architecture_state.json"):
        self.storage_path = storage_path

    def load_raw_data(self) -> Dict[str, Any]:
        """Carga el estado bruto de la arquitectura desde el repositorio JSON."""
        if not os.path.exists(self.storage_path):
            raise FileNotFoundError(f"No se encontró el archivo de estado en: {self.storage_path}")
        
        with open(self.storage_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def audit_architecture(self) -> Dict[str, Any]:
        """Ejecuta la auditoría integral validando el archivo JSON contra el esquema Pydantic."""
        raw_data = self.load_raw_data()
        
        try:
            validated_report = ArchitectureAuditReport(**raw_data)
        except ValidationError as e:
            raise ValueError(f"Fallo crítico en la validación de esquemas de arquitectura: {e}")
        
        total_components = len(validated_report.components)
        conformes = sum(1 for c in validated_report.components if c.status == "CONFORME")
        avg_score = sum(c.performance_score for c in validated_report.components) / total_components if total_components > 0 else 0.0
        
        audit_summary = {
            "quarter": validated_report.quarter,
            "phase": validated_report.phase,
            "total_components": total_components,
            "components_conformes": conformes,
            "compliance_rate": (conformes / total_components) * 100 if total_components > 0 else 0.0,
            "average_performance_score": round(avg_score, 2),
            "status": "APROBADO_INTEGRAL" if conformes == total_components else "REQUIERE_REVISION"
        }
        
        return audit_summary
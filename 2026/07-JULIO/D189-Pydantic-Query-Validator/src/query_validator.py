import re
from typing import Any, List, Optional
from pydantic import BaseModel, Field, field_validator

class SQLSanitizer:
    """Utilidad de sanitización avanzada para detectar y bloquear patrones maliciosos de inyección SQL."""
    
    FORBIDDEN_PATTERNS = [
        r"(%27)|(')",                    # Comillas simples sueltas
        r"(%23)|(#)",                    # Comentarios de SQL
        r"(--)",                         # Comentarios en línea de SQL
        r"(\bOR\b.*=)",                  # Tautologías clásicas (OR 1=1)
        r"(\bUNION\b.*\bSELECT\b)",      # Ataques UNION SELECT
        r"(\bDROP\b.*\bTABLE\b)",        # DROP TABLE
        r"(\bEXEC\b|\bEXECUTE\b)",       # Ejecución de comandos
        r"(;\s*(?:DROP|ALTER|CREATE|UPDATE|DELETE|INSERT)\b)" # Múltiples sentencias destructivas
    ]

    @classmethod
    def clean(cls, value: str) -> str:
        if not isinstance(value, str):
            return value
        
        for pattern in cls.FORBIDDEN_PATTERNS:
            if re.search(pattern, value, re.IGNORECASE):
                raise ValueError("Intento de inyección SQL detectado o patrón no permitido en la consulta.")
        
        return value


class AnalyticsQuerySchema(BaseModel):
    """Esquema de validación estricta y sanitización para parámetros de peticiones en APIs analíticas."""
    
    metric: str = Field(..., min_length=2, max_length=50, description="Métrica analítica solicitada")
    start_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Fecha de inicio (YYYY-MM-DD)")
    end_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Fecha de fin (YYYY-MM-DD)")
    filters: Optional[List[str]] = Field(default=None, description="Filtros opcionales de segmentación")
    limit: int = Field(default=100, ge=1, le=1000, description="Límite máximo de registros")

    @field_validator("metric", "filters", mode="before")
    @classmethod
    def sanitize_inputs(cls, v: Any) -> Any:
        """Método especializado: Intercepta y sanitiza los campos de texto antes de cualquier validación estructural."""
        if isinstance(v, str):
            return SQLSanitizer.clean(v)
        elif isinstance(v, list):
            return [SQLSanitizer.clean(item) if isinstance(item, str) else item for item in v]
        return v
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator, model_validator

class InferencePayload(BaseModel):
    """Esquema de validación estricta para payloads de inferencia de Machine Learning."""
    model_version: str = Field(..., description="Versión del modelo objetivo (ej: v1.0.0)")
    features: List[float] = Field(..., description="Vector de características numéricas para la predicción")
    threshold: Optional[float] = Field(0.5, ge=0.0, le=1.0, description="Umbral opcional de confianza")

    @field_validator("features")
    @classmethod
    def validate_features_not_empty(cls, v: List[float]) -> List[float]:
        if not v:
            raise ValueError("El vector de características 'features' no puede estar vacío.")
        if len(v) > 10:
            raise ValueError("El vector excede el límite máximo permitido de 10 características.")
        return v

    @field_validator("model_version")
    @classmethod
    def validate_version_format(cls, v: str) -> str:
        if not v.startswith("v"):
            raise ValueError("La versión del modelo debe comenzar con el prefijo 'v' (ej: v1.0.0).")
        return v

    @model_validator(mode="after")
    def validate_business_logic(self) -> "InferencePayload":
        # Regla de negocio de ejemplo: si la versión es v2.0+, se exigen al menos 3 features
        if self.model_version.startswith("v2") and len(self.features) < 3:
            raise ValueError("Los modelos de la familia v2.0 o superior requieren un mínimo de 3 características.")
        return self
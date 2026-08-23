from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class RecordSchema(BaseModel):
    id: int = Field(..., gt=0, description="Identificador único positivo")
    name: str = Field(..., min_length=2, description="Nombre del registro")
    score: float = Field(..., ge=0.0, le=100.0, description="Puntuación entre 0 y 100")
    active: Optional[bool] = True
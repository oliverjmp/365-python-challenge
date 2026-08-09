import logging
from typing import Any, Dict, List
import pandas as pd
from pydantic import BaseModel, Field, ValidationError

# Configuración de logs estructurados
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("ETLTransformer")


class RecordSchema(BaseModel):
    """Esquema de validación para los registros de entrada."""
    id: int = Field(..., description="Identificador único")
    value: float = Field(..., description="Valor numérico de la métrica")
    category: str = Field(..., description="Categoría del registro")


class ETLTransformer:
    """Transformador de datos robusto con validación Pydantic y manejo de nulos."""

    def __init__(self, multiplier: float = 1.1):
        self.multiplier = multiplier

    def clean_and_transform(self, raw_data: List[Dict[str, Any]]) -> pd.DataFrame:
        """Valida, limpia y transforma una lista de diccionarios en un DataFrame."""
        logger.info(f"Iniciando transformación de {len(raw_data)} registros brutos.")
        valid_records = []

        for row in raw_data:
            try:
                validated = RecordSchema(**row)
                valid_records.append(
                    {
                        "id": validated.id,
                        "value": validated.value * self.multiplier,
                        "category": validated.category.strip().upper(),
                    }
                )
            except ValidationError as e:
                logger.warning(
                    f"Registro descartado por error de validación: {e} | Datos: {row}"
                )
            except Exception as e:
                logger.error(f"Error inesperado procesando fila: {e}")

        if not valid_records:
            logger.warning("No se encontraron registros válidos tras la limpieza.")
            return pd.DataFrame(columns=["id", "value", "category"])

        df = pd.DataFrame(valid_records)
        logger.info(f"Transformación exitosa. Registros finales: {len(df)}")
        return df
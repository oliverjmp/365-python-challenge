from datetime import date
from pydantic import BaseModel, Field


class FinancialTrendRecord(BaseModel):
    """Modelo Pydantic v2 para validar el resultado del análisis financiero avanzado."""

    transaction_date: date = Field(..., description="Fecha de la transacción financiera")
    category: str = Field(..., description="Categoría de la cuenta o transacción")
    daily_amount: float = Field(..., description="Monto registrado en la fecha")
    moving_average_7d: float = Field(..., description="Media móvil de 7 días")
    previous_day_amount: float = Field(..., description="Monto del día anterior (LAG)")
    trend_deviation_pct: float = Field(
        ..., description="Desviación porcentual respecto a la media móvil"
    )

    model_config = {"frozen": True}
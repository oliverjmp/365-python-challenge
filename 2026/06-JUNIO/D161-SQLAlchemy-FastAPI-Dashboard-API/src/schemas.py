from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class AnalyticsCreate(BaseModel):
    metric_name: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)
    value: float

class AnalyticsResponse(AnalyticsCreate):
    id: int
    recorded_at: datetime

    model_config = ConfigDict(from_attributes=True)
from __future__ import annotations
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from src.database import Base

class AnalyticsRecord(Base):
    """Modelo SQLAlchemy para almacenar métricas analíticas agregadas."""
    __tablename__ = "analytics_records"

    id = Column(Integer, primary_key=True, index=True)
    metric_name = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    value = Column(Float, nullable=False)
    recorded_at = Column(DateTime, default=datetime.utcnow)
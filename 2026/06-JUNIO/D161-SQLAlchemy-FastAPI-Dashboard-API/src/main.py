from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import engine, Base, get_db
from src.models import AnalyticsRecord
from src.schemas import AnalyticsCreate, AnalyticsResponse

# Crear tablas en base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Dashboard Analytics API",
    description="Microservicio backend optimizado para servir datos analíticos agregados.",
    version="1.0.0"
)

@app.post("/analytics/", response_model=AnalyticsResponse, status_code=status.HTTP_201_CREATED)
def create_analytics_record(payload: AnalyticsCreate, db: Session = Depends(get_db)):
    """Registra una nueva métrica analítica en la base de datos."""
    try:
        db_record = AnalyticsRecord(
            metric_name=payload.metric_name,
            category=payload.category,
            value=payload.value
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno al guardar la métrica: {str(e)}")

@app.get("/analytics/", response_model=List[AnalyticsResponse])
def get_analytics_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene el listado paginado de registros analíticos."""
    records = db.query(AnalyticsRecord).offset(skip).limit(limit).all()
    return records

@app.get("/analytics/summary/", status_code=status.HTTP_200_OK)
def get_analytics_summary(db: Session = Depends(get_db)):
    """Devuelve un resumen agregado de las métricas para tableros web."""
    records = db.query(AnalyticsRecord).all()
    total_records = len(records)
    
    if total_records == 0:
        return {"total_records": 0, "average_value": 0.0, "categories": []}

    total_sum = sum(r.value for r in records)
    avg_value = total_sum / total_records
    categories = list(set(r.category for r in records))

    return {
        "total_records": total_records,
        "average_value": round(avg_value, 2),
        "categories": categories
    }
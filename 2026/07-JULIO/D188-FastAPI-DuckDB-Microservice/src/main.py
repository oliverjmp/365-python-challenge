from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse  # <-- Añadir esta importación
from pydantic import BaseModel
from typing import List
from database import inicializar_base_datos_prueba
from service import AnaliticaVentasService

@asynccontextmanager
async def lifespan(app: FastAPI):
    inicializar_base_datos_prueba()
    yield

app = FastAPI(
    title="D188 - FastAPI DuckDB Read-Only Microservice",
    version="1.0.0",
    lifespan=lifespan
)

class VentaRespuesta(BaseModel):
    id_transaccion: int
    departamento: str
    pais: str
    monto: float
    estado: str

class ResumenDepartamento(BaseModel):
    departamento: str
    total_monto: float
    transacciones_count: int

# --- NUEVO: Redirección automática de la raíz al Swagger UI ---
@app.get("/", include_in_schema=False)
def raiz_redirect():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["Sistema"])
def health_check():
    return {"status": "healthy", "engine": "FastAPI + DuckDB Read-Only + Service Layer"}

@app.get("/api/ventas", response_model=List[VentaRespuesta], tags=["Analítica"])
def listar_ventas(limit: int = 10):
    try:
        return AnaliticaVentasService.obtener_todas_las_ventas(limit)
    except Exception as e:
        import traceback
        traceback.print_exc()  # <-- Esto imprimirá el error rojo completo en la terminal
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/resumen/departamento", response_model=List[ResumenDepartamento], tags=["Analítica"])
def resumen_por_departamento():
    try:
        return AnaliticaVentasService.obtener_resumen_por_departamento()
    except Exception as e:
        import traceback
        traceback.print_exc()  # <-- Esto imprimirá el error rojo completo en la terminal
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI(title="Microservicio con Global Exception Handler")

class BusinessException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "status": "error",
            "message": f"El recurso '{exc.name}' no fue encontrado o la regla de negocio no es válida.",
        },
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status": "error",
            "message": "Ocurrió un error interno en el servidor.",
        },
    )

@app.get("/analytics/resource/{name}")
def get_resource(name: str):
    if name == "unknown":
        raise BusinessException(name=name)
    return {"status": "success", "resource": name}

@app.get("/analytics/error")
def trigger_server_error():
    raise ValueError("Error crítico de sistema")
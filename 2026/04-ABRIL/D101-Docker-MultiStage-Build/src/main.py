from fastapi import FastAPI

app = FastAPI(title="D101 Microservice", version="1.0.0")

@app.get("/")
def read_root():
    """Endpoint principal de verificación de estado del microservicio."""
    return {"status": "healthy", "message": "D101 Docker Multi-Stage Build running successfully!"}

@app.get("/health")
def health_check():
    """Endpoint de control de salud para Docker (Healthcheck)."""
    return {"status": "ok"}
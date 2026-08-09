from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Inicializamos el limitador basado en la IP remota del cliente
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Microservicio con Rate Limiter Middleware")

# Registramos el manejador de excepciones para cuando se superen los límites
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/analytics/data")
@limiter.limit("5/minute")  # Limitado a 5 peticiones por minuto por IP
def get_analytics_data(request: Request):
    """Endpoint protegido con limitación de tráfico."""
    return {"status": "success", "data": [10, 20, 30, 40, 50]}
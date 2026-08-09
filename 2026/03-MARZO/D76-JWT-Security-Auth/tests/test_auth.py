from fastapi.testclient import TestClient
from src.auth import app
from datetime import datetime, timedelta
import jwt
from src.auth import SECRET_KEY, ALGORITHM


client = TestClient(app)

def test_login_success():
    """Valida la obtención exitosa del token JWT con credenciales correctas."""
    response = client.post("/token", data={"username": "admin", "password": "secret"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    """Valida el rechazo al intentar iniciar sesión con credenciales erróneas."""
    response = client.post("/token", data={"username": "admin", "password": "wrong"})
    assert response.status_code == 401

def test_secure_endpoint_success():
    """Valida el acceso a un endpoint protegido enviando un token válido."""
    # Primero obtenemos el token
    login_res = client.post("/token", data={"username": "admin", "password": "secret"})
    token = login_res.json()["access_token"]
    
    # Consultamos el endpoint protegido
    response = client.get(
        "/analytics/secure-data",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_secure_endpoint_unauthorized():
    """Valida que se niegue el acceso si no se provee un token."""
    response = client.get("/analytics/secure-data")
    assert response.status_code == 401

def test_secure_endpoint_invalid_token():
    """Valida que se deniegue el acceso si se envía un token inválido o corrupto."""
    response = client.get(
        "/analytics/secure-data",
        headers={"Authorization": "Bearer token_invalido_de_prueba"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "No se pudieron validar las credenciales"


def test_secure_endpoint_missing_sub():
    """Valida que se deniegue el acceso si el token no contiene el campo 'sub' (username)."""
    # Creamos un token válido sin la clave 'sub'
    invalid_payload = {"exp": datetime.utcnow() + timedelta(minutes=15)}
    token = jwt.encode(invalid_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    response = client.get(
        "/analytics/secure-data",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "No se pudieron validar las credenciales"
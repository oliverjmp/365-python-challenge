import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from src.database import get_db
from fastapi import HTTPException

from src.database import Base, get_db
from src.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_create_analytics_record():
    """Valida la creación exitosa de un registro analítico vía POST."""
    response = client.post(
        "/analytics/",
        json={"metric_name": "Conversión", "category": "Digital", "value": 4.5}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["metric_name"] == "Conversión"
    assert data["category"] == "Digital"
    assert data["value"] == 4.5
    assert "id" in data

def test_get_analytics_records():
    """Valida la recuperación del listado de registros analíticos."""
    client.post("/analytics/", json={"metric_name": "Ingresos", "category": "Retail", "value": 1500.0})
    
    response = client.get("/analytics/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["metric_name"] == "Ingresos"

def test_get_analytics_summary_empty():
    """Valida el resumen agregado cuando no existen registros."""
    response = client.get("/analytics/summary/")
    assert response.status_code == 200
    data = response.json()
    assert data["total_records"] == 0
    assert data["average_value"] == 0.0
    assert data["categories"] == []

def test_get_analytics_summary_with_data():
    """Valida el cálculo correcto del resumen agregado con múltiples registros."""
    client.post("/analytics/", json={"metric_name": "M1", "category": "A", "value": 10.0})
    client.post("/analytics/", json={"metric_name": "M2", "category": "B", "value": 20.0})

    response = client.get("/analytics/summary/")
    assert response.status_code == 200
    data = response.json()
    assert data["total_records"] == 2
    assert data["average_value"] == 15.0
    assert sorted(data["categories"]) == ["A", "B"]

def test_get_db_generator():
    """Valida la ejecución correcta del generador de base de datos get_db."""
    db_gen = get_db()
    session = next(db_gen)
    assert session is not None
    # Forzar el cierre del bloque finally
    try:
        db_gen.close()
    except StopIteration:
        pass

def test_create_analytics_server_error(monkeypatch):
    """Valida que un fallo inesperado en la base de datos lance un HTTPException 500."""
    def mock_commit_error(*args, **kwargs):
        raise RuntimeError("Fallo de base de datos simulado")

    monkeypatch.setattr("sqlalchemy.orm.Session.commit", mock_commit_error)

    response = client.post(
        "/analytics/",
        json={"metric_name": "Test", "category": "Error", "value": 0.0}
    )
    assert response.status_code == 500
    assert "Error interno al guardar la métrica" in response.json()["detail"]
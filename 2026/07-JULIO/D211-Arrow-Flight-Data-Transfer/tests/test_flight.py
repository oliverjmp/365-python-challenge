import pytest
import pandas as pd
import pyarrow as pa
import pyarrow.flight as fl
from src.flight_server import SimpleFlightServer

@pytest.fixture
def flight_service():
    server = SimpleFlightServer("grpc://localhost:8999")
    df_test = pd.DataFrame({"id": [1, 2, 3], "valor": [10.5, 20.0, 35.2]})
    server.populate_table("dataset_prueba", df_test)
    
    yield server
    server.shutdown()

def test_flight_server_population(flight_service):
    assert "dataset_prueba" in flight_service.flights
    table = flight_service.flights["dataset_prueba"]
    assert table.num_rows == 3
    assert table.num_columns == 2

def test_flight_do_get_extraction(flight_service):
    ticket = fl.Ticket(b"dataset_prueba")
    stream = flight_service.do_get(None, ticket)
    
    # Validar que do_get retorna un RecordBatchStream válido de Apache Flight
    assert isinstance(stream, fl.RecordBatchStream)
    
    # Verificar que los datos en memoria corresponden al DataFrame original
    df_result = flight_service.flights["dataset_prueba"].to_pandas()
    assert len(df_result) == 3
    assert list(df_result["id"]) == [1, 2, 3]

def test_flight_invalid_ticket(flight_service):
    ticket = fl.Ticket(b"dataset_inexistente")
    with pytest.raises(KeyError):
        flight_service.do_get(None, ticket)

def test_flight_list_flights(flight_service):
    criteria = None
    flights_gen = list(flight_service.list_flights(None, criteria))
    assert len(flights_gen) == 1
    assert flights_gen[0].total_records == 3
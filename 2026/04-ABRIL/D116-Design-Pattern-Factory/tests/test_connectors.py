import pytest
from src.connectors import ConnectorFactory, DatabaseConnector, PostgreSQLConnector, MySQLConnector, MongoDBConnector

def test_postgresql_connector():
    connector = ConnectorFactory.create_connector("postgresql")
    assert isinstance(connector, PostgreSQLConnector)
    assert "PostgreSQL" in connector.connect()

def test_mysql_connector():
    connector = ConnectorFactory.create_connector("mysql")
    assert isinstance(connector, MySQLConnector)
    assert "MySQL" in connector.connect()

def test_mongodb_connector():
    connector = ConnectorFactory.create_connector("mongodb")
    assert isinstance(connector, MongoDBConnector)
    assert "MongoDB" in connector.connect()

def test_invalid_connector_raises_error():
    with pytest.raises(ValueError, match="Conector no soportado"):
        ConnectorFactory.create_connector("oracle")

def test_register_custom_connector():
    class CustomConnector(DatabaseConnector):
        def connect(self) -> str:
            return "Custom Connected"

    ConnectorFactory.register_connector("custom", CustomConnector)
    connector = ConnectorFactory.create_connector("custom")
    assert isinstance(connector, CustomConnector)
    assert connector.connect() == "Custom Connected"


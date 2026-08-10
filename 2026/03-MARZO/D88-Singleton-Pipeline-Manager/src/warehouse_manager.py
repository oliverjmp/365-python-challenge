class WarehouseConnectionManager:
    _instance = None

    def __new__(cls, connection_string: str = "default_dw_connection"):
        if cls._instance is None:
            cls._instance = super(WarehouseConnectionManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, connection_string: str = "default_dw_connection"):
        # Evitamos reinicializar los atributos si la instancia ya fue creada
        if self._initialized:
            return
        self.connection_string = connection_string
        self.is_connected = True
        self._initialized = True

    def execute_query(self, query: str) -> str:
        """Simula la ejecución de una consulta en el Data Warehouse."""
        if not self.is_connected:
            raise ConnectionError("No hay conexión activa con el Data Warehouse.")
        return f"Ejecutando '{query}' usando la conexión: {self.connection_string}"
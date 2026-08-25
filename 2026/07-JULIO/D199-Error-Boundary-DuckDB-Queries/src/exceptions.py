class DataLakeError(Exception):
    """Excepción base para todos los errores del pipeline de datos."""
    pass

class SQLSyntaxError(DataLakeError):
    """Se lanza cuando ocurre un error de sintaxis en la consulta SQL."""
    def __init__(self, message: str, query: str = ""):
        super().__init__(f"[SINTAXIS INVÁLIDA] {message} | Query: {query}")
        self.query = query

class QueryExecutionError(DataLakeError):
    """Se lanza cuando ocurre un fallo durante la ejecución lógica de la consulta en DuckDB."""
    def __init__(self, message: str, query: str = ""):
        super().__init__(f"[ERROR DE EJECUCIÓN] {message} | Query: {query}")
        self.query = query
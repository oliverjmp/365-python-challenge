import duckdb
import pandas as pd
from src.exceptions import SQLSyntaxError, QueryExecutionError

class DuckDBQueryRunner:
    """Ejecutor de consultas seguro con un patrón Error Boundary."""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path

    def ejecutar_query(self, query: str) -> pd.DataFrame:
        """Ejecuta una consulta SQL asegurando la captura y traducción de errores nativos."""
        try:
            conn = duckdb.connect(self.db_path)
            resultado = conn.execute(query).fetchdf()
            conn.close()
            return resultado
        except duckdb.ParserException as e:
            raise SQLSyntaxError(str(e), query=query)
        except (duckdb.CatalogException, duckdb.BinderException, duckdb.ConversionException, Exception) as e:
            # Si ya es una de nuestras excepciones personalizadas, la re-lanzamos
            if isinstance(e, (SQLSyntaxError, QueryExecutionError)):
                raise e
            raise QueryExecutionError(str(e), query=query)
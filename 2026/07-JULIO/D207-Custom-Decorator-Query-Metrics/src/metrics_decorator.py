import functools
import time
import logging
import duckdb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("QueryMetricsLogger")

def medir_rendimiento_sql(func):
    """Decorador avanzado para medir latencia y telemetría de ejecución de consultas SQL."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        exito = True
        
        try:
            resultado = func(*args, **kwargs)
            return resultado
        except Exception as e:
            exito = False
            logger.error(f"[ERROR TELEMETRIA] Error en '{func.__name__}': {str(e)}")
            raise
        finally:
            fin = time.perf_counter()
            latencia_ms = (fin - inicio) * 1000.0
            logger.info(f"[TELEMETRIA] Función '{func.__name__}' ejecutada en {latencia_ms:.4f} ms | Estado Exitoso: {exito}")
            
    return wrapper

class MetricsAnalyzer:
    """Analizador de métricas y consultas respaldado por DuckDB."""

    def __init__(self, conn: duckdb.DuckDBPyConnection):
        self.conn = conn

    @medir_rendimiento_sql
    def ejecutar_consulta_analitica(self) -> list:
        """Ejecuta una consulta agregada sobre las métricas de rendimiento."""
        query = """
            SELECT 
                operacion,
                COUNT(*) as total_operaciones,
                SUM(filas_afectadas) as total_filas
            FROM metrics_data
            GROUP BY operacion
            ORDER BY total_filas DESC;
        """
        df = self.conn.execute(query).fetchdf()
        return df.to_dict(orient="records")

    @medir_rendimiento_sql
    def filtrar_por_operacion(self, operacion: str) -> list:
        """Filtra los registros de métricas por tipo de operación SQL."""
        query = """
            SELECT id, operacion, tabla, filas_afectadas, estado
            FROM metrics_data
            WHERE LOWER(operacion) = LOWER(?);
        """
        df = self.conn.execute(query, [operacion]).fetchdf()
        return df.to_dict(orient="records")

    @medir_rendimiento_sql
    def ejecutar_consulta_fallida(self) -> list:
        """Método diseñado para forzar un error controlado y cubrir las excepciones del decorador."""
        raise RuntimeError("Error forzado de infraestructura analítica")
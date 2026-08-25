import timeit
import pandas as pd
import duckdb

class BenchmarkRunner:
    """Motor de rendimiento para comparar consultas analíticas entre Pandas y DuckDB."""

    def __init__(self, num_filas: int = 100_000):
        self.num_filas = num_filas
        self.df = pd.DataFrame({
            "id": range(num_filas),
            "categoria": pd.Series(["A" if i % 2 == 0 else "B" for i in range(num_filas)], dtype="string"),
            "valor": [float(i * 1.5) for i in range(num_filas)]
        })
        self.conn = duckdb.connect(database=":memory:")
        # Convertimos a Arrow o usamos el DataFrame directamente asegurando tipos compatibles
        self.conn.register("datos_df", self.df)

    def benchmark_pandas(self) -> float:
        """Mide el tiempo de ejecución de una agregación agrupada utilizando Pandas."""
        def operacion_pandas():
            return self.df.groupby("categoria")["valor"].sum()
        
        tiempo = timeit.timeit(operacion_pandas, number=10)
        return tiempo

    def benchmark_duckdb(self) -> float:
        """Mide el tiempo de ejecución de la misma agregación utilizando DuckDB."""
        def operacion_duckdb():
            self.conn.execute("SELECT categoria, SUM(valor) FROM datos_df GROUP BY categoria").fetchall()
        
        tiempo = timeit.timeit(operacion_duckdb, number=10)
        return tiempo

    def ejecutar_comparativa(self) -> dict:
        """Ejecuta ambos benchmarks y retorna los resultados comparativos."""
        t_pandas = self.benchmark_pandas()
        t_duckdb = self.benchmark_duckdb()
        
        return {
            "filas": self.num_filas,
            "pandas_segundos": t_pandas,
            "duckdb_segundos": t_duckdb,
            "mejora_x": round(t_pandas / t_duckdb, 2) if t_duckdb > 0 else 0
        }
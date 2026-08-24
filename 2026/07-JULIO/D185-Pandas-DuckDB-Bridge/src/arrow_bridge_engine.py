import os
import time
import duckdb
import pyarrow as pa
import pandas as pd

class PandasDuckDBBridgeEngine:
    """
    Motor especializado en el intercambio optimizado de DataFrames mediante
    Zero-Copy utilizando Apache Arrow y DuckDB.
    """

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = duckdb.connect(db_path)

    def generar_dataset_vectorial(self, num_registros: int = 100000) -> pa.Table:
        """
        Genera un dataset masivo en Pandas y lo convierte directamente a una tabla
        de Apache Arrow para asegurar el intercambio sin copias innecesarias en memoria.
        """
        print(f"[Bridge ETL] Generando dataset vectorial de {num_registros:,} registros...")
        
        data = {
            "transaccion_id": range(1, num_registros + 1),
            "departamento": ["Ingeniería", "Finanzas", "Marketing", "Operaciones"] * (num_registros // 4),
            "pais": ["España", "México", "Colombia", "Argentina"] * (num_registros // 4),
            "monto": [round(float((i % 5000) + 15.50), 2) for i in range(num_registros)],
            "estado": ["COMPLETADO" if i % 7 != 0 else "PENDIENTE" for i in range(num_registros)]
        }
        
        df = pd.DataFrame(data)
        
        # Conversión a Apache Arrow Table (Zero-Copy Interoperability)
        inicio = time.time()
        arrow_table = pa.Table.from_pandas(df)
        duracion = time.time() - inicio
        
        print(f" > Conversión a Apache Arrow completada en: {duracion * 1000:.2f} ms")
        return arrow_table

    def ejecutar_analitica_bridge(self, arrow_table: pa.Table) -> dict:
        """
        Ejecuta consultas SQL directamente sobre la tabla de Apache Arrow registrada
        en DuckDB sin deserializar a objetos nativos de Python (Cero Copia).
        """
        # Registrar la tabla Arrow virtualmente en DuckDB sin mover datos a RAM adicional
        self.conn.register("tabla_vectorial", arrow_table)

        query = """
            SELECT 
                departamento,
                pais,
                COUNT(transaccion_id) AS total_transacciones,
                ROUND(SUM(monto), 2) AS monto_total,
                ROUND(AVG(monto), 2) AS monto_promedio
            FROM tabla_vectorial
            WHERE estado = 'COMPLETADO'
            GROUP BY departamento, pais
            ORDER BY monto_total DESC;
        """

        inicio = time.time()
        cursor = self.conn.execute(query)
        datos = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        latencia = (time.time() - inicio) * 1000

        # Exportar resultados de vuelta a Pandas/Arrow de forma optimizada
        df_resultado = self.conn.execute(query).df()

        return {
            "latencia_ms": round(latencia, 2),
            "dataframe_resultados": df_resultado
        }

    def cerrar_conexion(self):
        self.conn.close()
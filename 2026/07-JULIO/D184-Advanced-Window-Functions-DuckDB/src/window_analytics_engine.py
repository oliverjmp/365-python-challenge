import os
import time
import duckdb
import pandas as pd

class AdvancedWindowAnalyticsEngine:
    """
    Motor analítico especializado en SQL avanzado y funciones de ventana (Window Functions)
    sobre almacenamiento columnar mediante DuckDB.
    """

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = duckdb.connect(db_path)

    def generar_dataset_financiero(self, parquet_path: str) -> dict:
        """
        Genera un dataset histórico corporativo de ingresos mensuales por línea de negocio
        y lo almacena con compresión columnar ZSTD.
        """
        os.makedirs(os.path.dirname(parquet_path) or ".", exist_ok=True)

        anios = [2024, 2025, 2026]
        meses = range(1, 13)
        lineas = ["Cloud Infrastructure", "Cybersecurity Suite", "AI Enterprise API"]

        registros = []
        id_counter = 1
        for anio in anios:
            for mes in meses:
                for linea in lineas:
                    base_revenue = 150000.0 if linea == "Cloud Infrastructure" else 90000.0
                    factor_crecimiento = (anio - 2023) * 1.15
                    factor_mes = 1.0 + (mes * 0.02)
                    ingresos = round(base_revenue * factor_crecimiento * factor_mes, 2)

                    registros.append({
                        "registro_id": id_counter,
                        "anio": anio,
                        "mes": mes,
                        "linea_negocio": linea,
                        "ingresos_mensuales": ingresos
                    })
                    id_counter += 1

        df = pd.DataFrame(registros)
        df.to_parquet(parquet_path, compression="ZSTD", index=False)
        
        tamano_mb = os.path.getsize(parquet_path) / (1024 * 1024)
        return {
            "total_filas": len(df),
            "tamano_mb": round(tamano_mb, 4)
        }

    def calcular_metricas_financieras(self, parquet_path: str) -> dict:
        """
        Aplica funciones de ventana avanzadas de SQL (LAG, SUM OVER Partition) para evaluar
        el rendimiento financiero, acumulados anuales y variaciones porcentuales (MoM).
        """
        if not os.path.exists(parquet_path):
            raise FileNotFoundError(f"El recurso financiero no existe en: {parquet_path}")

        query = f"""
            WITH base_calculada AS (
                SELECT 
                    linea_negocio,
                    anio,
                    mes,
                    ingresos_mensuales,
                    SUM(ingresos_mensuales) OVER (
                        PARTITION BY linea_negocio, anio 
                        ORDER BY mes 
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                    ) AS ingresos_acumulados_anio,
                    LAG(ingresos_mensuales, 1) OVER (
                        PARTITION BY linea_negocio 
                        ORDER BY anio, mes
                    ) as ingresos_mes_anterior
                FROM read_parquet('{parquet_path}')
            )
            SELECT 
                linea_negocio,
                anio,
                mes,
                ingresos_mensuales,
                ingresos_acumulados_anio,
                COALESCE(ingresos_mes_anterior, ingresos_mensuales) AS ingresos_mes_anterior,
                ROUND(((ingresos_mensuales - ingresos_mes_anterior) / NULLIF(ingresos_mes_anterior, 0)) * 100, 2) AS variacion_mom_pct
            FROM base_calculada
            ORDER BY linea_negocio, anio, mes;
        """

        inicio = time.time()
        cursor = self.conn.execute(query)
        datos = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        latencia = (time.time() - inicio) * 1000

        df_resultado = pd.DataFrame(datos, columns=columnas)
        return {
            "latencia_ms": round(latencia, 2),
            "dataframe_resultados": df_resultado
        }

    def cerrar_conexion(self):
        self.conn.close()
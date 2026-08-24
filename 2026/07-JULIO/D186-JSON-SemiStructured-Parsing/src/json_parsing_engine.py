import os
import time
import json
import duckdb
import pandas as pd

class JSONSemiStructuredEngine:
    """
    Motor especializado en la ingesta, aplanamiento y consulta analítica de datos
    semi-estructurados (JSON anidado) utilizando DuckDB sobre almacenamiento columnar.
    """

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = duckdb.connect(db_path)

    def generar_dataset_json(self, parquet_path: str) -> dict:
        """
        Genera un dataset corporativo con cargas útiles JSON anidadas y lo almacena en Parquet.
        """
        os.makedirs(os.path.dirname(parquet_path) or ".", exist_ok=True)
        
        num_registros = 50000
        eventos = ["USER_LOGIN", "CHECKOUT_CART", "API_REQUEST", "ERROR_LOG"]
        dispositivos = ["iOS", "Android", "Web-Chrome", "Web-Firefox"]
        
        registros = []
        for i in range(1, num_registros + 1):
            payload_anidado = {
                "evento": eventos[i % len(eventos)],
                "dispositivo": dispositivos[i % len(dispositivos)],
                "sesion": {
                    "id_sesion": f"sess_{i * 13}",
                    "duracion_ms": (i * 37) % 5000 + 200
                },
                "detalles": {
                    "codigo_respuesta": 200 if i % 10 != 0 else 500,
                    "latencia_red_ms": round((i % 150) + 12.5, 2)
                }
            }
            
            registros.append({
                "transaccion_id": 100000 + i,
                "timestamp_utc": f"2026-07-{(i % 28) + 1:02d}T12:00:00Z",
                "payload_json": json.dumps(payload_anidado)
            })

        df = pd.DataFrame(registros)
        df.to_parquet(parquet_path, compression="ZSTD", index=False)
        
        tamano_mb = os.path.getsize(parquet_path) / (1024 * 1024)
        return {
            "total_filas": num_registros,
            "tamano_mb": round(tamano_mb, 4)
        }

    def consultar_datos_json(self, parquet_path: str) -> dict:
        """
        Extrae y consulta campos internos del JSON directamente utilizando operadores de DuckDB (->>).
        """
        if not os.path.exists(parquet_path):
            raise FileNotFoundError(f"El recurso JSON no existe en: {parquet_path}")

        query = f"""
            SELECT 
                payload_json->>'evento' AS tipo_evento,
                payload_json->>'dispositivo' AS plataforma,
                CAST(payload_json->'detalles'->>'codigo_respuesta' AS INTEGER) AS codigo_resp,
                COUNT(*) AS total_ocurrencias,
                ROUND(AVG(CAST(payload_json->'detalles'->>'latencia_red_ms' AS DOUBLE)), 2) AS latencia_promedio_ms
            FROM read_parquet('{parquet_path}')
            GROUP BY 1, 2, 3
            ORDER BY total_ocurrencias DESC;
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
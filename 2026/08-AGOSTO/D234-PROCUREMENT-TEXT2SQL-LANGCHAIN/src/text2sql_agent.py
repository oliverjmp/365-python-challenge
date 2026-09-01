"""Agente Text-to-SQL nativo para Procurement OpEx utilizando el SDK oficial google-genai."""

import os
import re
import logging
from typing import Tuple, Any, Optional
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.database_engine import ProcurementDatabaseManager

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class ProcurementText2SQLAgent:
    """Traductor de Lenguaje Natural a SQL ANSI mediante el SDK oficial Google GenAI y DuckDB."""

    def __init__(
        self, 
        db_manager: ProcurementDatabaseManager, 
        api_key: Optional[str] = None, 
        model_name: str = "gemini-3.6-flash"  # <-- Actualizado al modelo vigente
    ):
        self.db = db_manager
        
        raw_key = api_key or os.getenv("GEMINI_API_KEY", "")
        clean_key = str(raw_key).strip().strip("'").strip('"').replace("\n", "").replace("\r", "")

        if not clean_key or clean_key.startswith("tu_api_key"):
            raise ValueError("GEMINI_API_KEY no encontrada o no válida en el entorno.")

        self.model_name = str(model_name).replace("models/", "").strip()
        self.client = genai.Client(api_key=clean_key)

    def _build_prompt(self, question: str) -> str:
        """Construye el prompt estructurado inyectando el DDL de DuckDB."""
        schema_info = self.db.get_schema_info()
        return f"""
Eres un Staff Data Engineer y experto en SQL ANSI especializado en analítica de Procurement y OpEx. Tu función es traducir preguntas de negocio en español a consultas SQL ejecutables y optimizadas para DuckDB.

ESQUEMA DDL DE LA BASE DE DATOS:
{schema_info}

REGLAS DE GENERACIÓN SQL:
1. Retorna ÚNICAMENTE la sentencia SQL válida envuelta dentro de un bloque markdown ```sql ... ```.
2. NO incluyas explicaciones, texto introductorio ni notas al final.
3. Para montos totales acumulados, utiliza la columna `total_amount`.
4. Utiliza sintaxis estándar compatible con DuckDB (GROUP BY, HAVING, ORDER BY, LIMIT, JOINs explícitos).
5. Mantén la búsqueda de valores categóricos insensible a mayúsculas/minúsculas si aplica.

PREGUNTA DE NEGOCIO: {question}

RESPUESTA (Consulta SQL estricta):
"""

    @staticmethod
    def _extract_sql_from_response(raw_response: str) -> str:
        """Sanea la respuesta del LLM extrayendo la consulta SQL dentro de bloques Markdown."""
        match = re.search(r"```sql\s*(.*?)\s*```", raw_response, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return raw_response.replace("```", "").strip()

    def generate_sql(self, question: str) -> str:
        """Genera la consulta SQL ejecutando la llamada directa al SDK oficial de Gemini."""
        prompt = self._build_prompt(question)
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.0
                )
            )
            return self._extract_sql_from_response(response.text)
        except Exception as err:
            logging.error("Error en la invocación del SDK GenAI: %s", err)
            raise RuntimeError(f"Error al generar SQL con el modelo '{self.model_name}': {err}")

    def query_and_analyze(self, question: str) -> Tuple[str, Any]:
        """Orquesta la traducción a SQL y ejecuta la consulta sobre DuckDB."""
        sql_query = self.generate_sql(question)
        logging.info("SQL Generado: %s", sql_query)
        result_df = self.db.execute_query(sql_query)
        return sql_query, result_df
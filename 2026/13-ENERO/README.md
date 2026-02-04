🧪 Día 13 — Sistema de Validación Automática de Datos (Data Quality Checks)

📌 Descripción general

En este día desarrollé un módulo de validación automática de calidad de datos, cuyo propósito es asegurar que cualquier dataset cumpla con estándares mínimos antes de ser utilizado en análisis, reportes o procesos automatizados.
El sistema detecta problemas comunes y genera un log detallado para facilitar la trazabilidad.

🎯 Objetivos del día

Validar datasets antes de procesarlos.

Detectar:

columnas faltantes

tipos incorrectos

valores nulos

duplicados

valores fuera de rango

Registrar resultados en logs.

Devolver un resultado booleano que indique si el dataset es apto o no.

🛠️ Tecnologías utilizadas

Python

Pandas

Logging

JSON para reglas configurables

🧩 Funcionalidades principales

✔ Validación de columnas obligatorias
Comprueba que el dataset incluya todas las columnas definidas en rules.json.

✔ Validación de tipos
Convierte y valida tipos como:

int

float

datetime

✔ Detección de nulos y duplicados
Registra advertencias si encuentra valores faltantes o filas repetidas.

✔ Validación de rangos
Verifica que los valores estén dentro de límites definidos.

✔ Logging estructurado
Genera un archivo:

logs/data_quality.log

con todos los resultados de la validación.

📂 Estructura del módulo

Código

13-ENERO/

│── data_quality.py

│── rules.json

│── data.csv

│── logs/

│     └── data_quality.log

│── README.md

🚀 Ejecución

Desde la carpeta:

Código
cd 2026/13-ENERO

python data_quality.py

Salida esperada:

Código

¿Dataset válido?: True

📄 Ejemplo de reglas (rules.json)


json

{

    "required_columns": ["id", "fecha", "valor"],

    "column_types": {

        "id": "int",

        "fecha": "datetime",

        "valor": "float"

    },

    "range_rules": {

        "valor": {

            "min": 0,

            "max": 10000

        }

    }

}

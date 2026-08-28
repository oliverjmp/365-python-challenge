# D224 - Multiprocessing CPU-Bound (Superando el GIL)

Implementación de un motor de procesamiento paralelo intensivo basado en `multiprocessing` y `ProcessPoolExecutor` diseñado para ejecutar cargas de trabajo numéricas pesadas sin las restricciones del GIL de Python.

---

## 🏛️ Explicación Profunda de la Arquitectura

### El Problema: El Bloqueo del GIL (Global Interpreter Lock)
El GIL en CPython previene que múltiples hilos nativos ejecuten código de bytecode de Python al mismo tiempo. Esto imposibilita el rendimiento multinúcleo en tareas de alta carga matemática o analítica cuando se usan hilos.

### La Solución: Arquitectura Multi-Proceso
Crear procesos independientes (`multiprocessing`) otorga a cada uno su propio intérprete de Python y su propio espacio de memoria. Esto permite saturar el 100% de la potencia de procesamiento del hardware moderno.

---

## 💼 Casos de Uso Reales en Producción
1. **Machine Learning y Data Science:** Procesamiento previo y transformación pesada de datasets masivos (*Feature Engineering*).
2. **Criptografía y Análisis Numérico:** Resolución de cálculos factoriales, criptografía de clave pública o simulaciones científicas complejas.
3. **Renderizado y Procesamiento de Imágenes:** Manipulación de matrices de píxeles a alta velocidad.

---

## 🚀 Comandos de Ejecución y Validación

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar CLI de validación:**
  `python main.py`

- **Lanzar aplicación web interactiva (Streamlit):**
  `streamlit run app.py`

- **Levantar documentación local (MkDocs Enterprise):**
  `mkdocs serve`
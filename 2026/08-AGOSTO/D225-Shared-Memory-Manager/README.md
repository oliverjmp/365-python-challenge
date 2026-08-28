# D225 - Shared Memory Manager (Procesamiento Zero-Copy)

Implementación avanzada de intercambio de matrices de gran escala entre procesos utilizando bloques de memoria compartida del sistema operativo (`multiprocessing.shared_memory`) para maximizar el rendimiento analítico.

---

## 🏛️ Explicación Profunda de la Arquitectura

### El Problema: El Costo de la Serialización IPC
Cuando se procesan grandes conjuntos de datos (como matrices de Machine Learning o Big Data) utilizando múltiples procesos, pasar arreglos a través de colas o pipes estándar obliga a Python a serializar los datos byte a byte, consumiendo valioso tiempo de CPU y memoria RAM.

### La Solución: Bloques de Memoria del Sistema Operativo
`shared_memory` permite reservar un segmento de memoria RAM gestionado directamente por el kernel del SO. Los procesos hijos reciben únicamente una referencia ligera (nombre de cadena de texto) y montan una vista estructurada de NumPy directamente sobre esas direcciones físicas de memoria.

---

## 💼 Casos de Uso Reales en Producción
1. **Modelos de Deep Learning Distribuidos:** Intercambio rápido de tensores de pesos entre workers de entrenamiento paralelo.
2. **Procesamiento de Imágenes en Tiempo Real:** Manipulación de streams de video de alta resolución distribuidos entre núcleos de CPU.
3. **Sistemas de Trading de Alta Frecuencia (HFT):** Lectura ultra rápida de libros de órdenes compartidos en memoria volátil.

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
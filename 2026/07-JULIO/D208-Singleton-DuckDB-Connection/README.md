# D208 - Singleton DuckDB Connection

Patrón de diseño creacional para garantizar una única instancia segura del motor analítico *in-process* **DuckDB**, optimizando la concurrencia mediante mecanismos *thread-safe*.

## 🏛️ Estructura del Proyecto

D208-Singleton-DuckDB-Connection/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (fail_under = 100)
├── docs/
│   ├── index.md           # Página principal de documentación técnica del reto
│   └── architecture.md    # Arquitectura detallada del patrón Singleton y seguridad de hilos
├── src/
│   ├── __init__.py
│   └── singleton_db.py    # Implementación Thread-Safe del patrón Singleton con DuckDB
├── tests/
│   ├── __init__.py
│   └── test_singleton.py  # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── main.py                # Script CLI de demostración y pruebas de concurrencia por hilos
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Índigo)
├── requirements.txt       # Dependencias y librerías del entorno
└── README.md              # Documentación principal en la raíz del proyecto

## 💼 Casos Prácticos de Uso

1. **Gestión Eficiente de Recursos In-Process:**
   - Evita la apertura masiva y redundante de conexiones a bases de datos en memoria local, reduciendo la huella de memoria y optimizando el acceso concurrente en pipelines.
2. **Arquitecturas Multi-Thread (Hilos Múltiples):**
   - Garantiza mediante bloqueos de exclusión mutua (`threading.Lock`) que hilos paralelos accedan de forma segura al mismo descriptor de DuckDB sin colisiones de estado.
3. **Gobierno de Estado y Testing:**
   - Facilita el aislamiento transaccional y la limpieza de conexiones mediante métodos de control de ciclo de vida en entornos de pruebas automatizadas.

## ⚙️ Componentes Técnicos
- **Motor Singleton (`src/singleton_db.py`):** Clase metaclase estructurada con sobrecarga de `__new__` y sincronización por hilos.
- **Demostración CLI (`main.py`):** Script de ejecución interactiva para validar la igualdad de punteros en memoria bajo concurrencia paralela.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo un esquema de color índigo corporativo.

## 🚀 Ejecución y Comandos de Pruebas

- **Instalación de dependencias:**
  `pip install -r requirements.txt`

- **Ejecución de pruebas unitarias (con cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecución del Script CLI de Concurrencia:**
  `python main.py`

- **Lanzamiento del Portal de Documentación:**
  `mkdocs serve`
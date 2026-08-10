# Módulo D85: Thread Pool Downloader (`concurrent.futures`)

## Descripción General
Este módulo implementa un **descargador concurrente multihilo** optimizado en Python. Utiliza `concurrent.futures.ThreadPoolExecutor` para procesar peticiones web de forma paralela, maximizando el rendimiento en la obtención masiva de datos o recursos.

---

## Características Principales
* **Concurrencia Controlada**: Ajuste dinámico del número de hilos simultáneos mediante `max_workers`.
* **Manejo Robusto de Errores**: Captura de excepciones de red individuales sin interrumpir el lote completo de descargas.
* **Pruebas Mockeadas**: Verificación rápida y aislada del comportamiento concurrente con `unittest.mock`.

---

## Estructura del Proyecto
```text
D85-Thread-Pool-Downloader/
├── src/
│   ├── __init__.py
│   └── downloader.py # Lógica del ThreadPoolExecutor y gestión de peticiones
├── tests/
│   ├── __init__.py
│   └── test_downloader.py # Pruebas unitarias con mocks de red
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo
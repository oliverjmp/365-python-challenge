# D219 - Refactoring Analytics Core (Design Pattern: Facade)

Refactorización estructural del núcleo analítico utilizando el patrón de diseño **Fachada (*Facade*)** para desacoplar las operaciones de ingesta columnar, control de memoria (*Memory Pools*) y procesamiento analítico de alto rendimiento con **Apache Arrow**.

---

## 🏛️ Explicación Profunda de la Arquitectura y Diseño

### El Problema: Acoplamiento Crítico y Complejidad de Subsistemas
En los pipelines de analítica modernos, los motores de procesamiento suelen interactuar de forma directa con múltiples subsistemas de bajo nivel:
1. **Gestores de Memoria (*Memory Pools*):** Auditoría y asignación de búferes en RAM.
2. **Motores de Ingesta Columnar:** Conversión de estructuras nativas de Python/Pandas a tablas contiguas en C++ (`pa.Table`).
3. **Motores de Transformación:** Ejecución de agregaciones y extracción de métricas.

Si los scripts de cliente o las APIs interactúan directamente con cada uno de este tipo de subsistemas, el código se vuelve altamente acoplado, frágil y difícil de mantener.

### La Solución: El Patrón Fachada (`AnalyticsCoreFacade`)
El patrón **Fachada** introduce una capa de abstracción intermedia que centraliza el flujo de trabajo en un punto de entrada único (`Single Entry Point`).

---

## 💼 Casos de Uso Reales en Entornos de Producción
1. **Unificación de Pipelines en ETL/ELT:** Permite a los orquestadores ejecutar transformaciones complejas en una sola línea de código.
2. **Desacoplamiento para Pruebas (Mocking):** Facilita aislar los componentes internos pesados durante los test unitarios.
3. **Blindaje de APIs Analíticas:** Previene fugas de memoria o corrupciones de estado ante solicitudes concurrentes mal estructuradas.

---

## 🚀 Comandos de Ejecución
- **Instalar dependencias:** `pip install -r requirements.txt`
- **Ejecutar pruebas con 100% de cobertura:** `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`
- **Ejecutar validación CLI:** `python main.py`
- **Levantar documentación:** `mkdocs serve`
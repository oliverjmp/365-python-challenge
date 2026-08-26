# Portal Técnico: D208 - Singleton DuckDB Connection

## 🏢 Resumen Ejecutivo y Gobierno de Concurrencia
El hito **D208** implementa el patrón de diseño creacional **Singleton** aplicado de forma segura a hilos (*Thread-Safe Singleton*) para la gestión de conexiones al motor analítico en memoria **DuckDB**. 

En arquitecturas de ingeniería de datos orientadas a microservicios y procesamiento local de alto rendimiento, abrir múltiples instancias de bases de datos *in-process* concurrentes sobre el mismo archivo o espacio de memoria genera contención de recursos, bloqueos de escritura y sobrecarga operacional. Este módulo centraliza y blinda el ciclo de vida de la conexión.

---

## 🎯 Objetivos y Principios Arquitectónicos
* **Instancia Única Garantizada:** Control estricto mediante el método espacial `__new__` para asegurar que solo exista un descriptor de conexión activo por proceso.
* **Seguridad contra Concurrencia (`threading.Lock`):** Implementación de mecanismos de exclusión mutua para prevenir condiciones de carrera (*race conditions*) cuando múltiples hilos solicitan la conexión simultáneamente.
* **Aislamiento para Pruebas Unitarias:** Exposición controlada del método `reset_instance` para permitir la destrucción limpia del estado entre ejecuciones de pruebas con Pytest.
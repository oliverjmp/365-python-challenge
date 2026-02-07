### 🤖 Proyecto Día 44: File Transaction Logging & Traceability 📜🔍

En este hito, dotamos a nuestro automatizador de una **Memoria de Auditoría**. El sistema genera ahora un archivo de registro persistente (`activity_log.txt`) que documenta cada transacción: origen, destino, marca de tiempo y estado de la operación. Esto es fundamental para cumplir con normativas de cumplimiento y resolución de errores en sistemas de producción.

#### **Hitos Técnicos Alcanzados:**
1.  **Logging Transaccional:** Implementación de una función de escritura asíncrona (Append Mode) que registra cada movimiento físico en el disco.
2.  **Trazabilidad de Rutas:** Registro de rutas absolutas para localizar archivos incluso si la estructura de carpetas cambia.
3.  **Sello de Auditoría:** Inclusión de metadatos (timestamps y tamaños) en el log para análisis forense de datos.
4.  **Arquitectura de "Caja Negra":** El log se mantiene independiente del flujo principal, garantizando que el historial se guarde incluso si el proceso se interrumpe.

#### **Tecnologías Utilizadas:**
* **File I/O (Context Managers):** Uso de `with open()` para garantizar cierres de archivo seguros.
* **Pathlib:** Para la resolución de rutas complejas y nombres de archivo.
* **Datetime:** Para el sellado cronológico de cada entrada del log.
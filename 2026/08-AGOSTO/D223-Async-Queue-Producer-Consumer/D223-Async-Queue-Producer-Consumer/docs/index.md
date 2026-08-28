# D223 - Async Queue Producer-Consumer

## 🏢 Resumen Ejecutivo y Alcance del Hito
El hito **D223** establece la implementación del **Patrón Productor-Consumidor** mediante el uso de colas seguras en memoria (**`asyncio.Queue`**). Este diseño arquitectónico desacopla la velocidad de generación de eventos (*Productores*) de la capacidad de procesamiento de carga de trabajo (*Consumidores*), introduciendo contrapresión (*Backpressure*) automática a través de límites de capacidad acotados (*maxsize*).

---

## 📐 Principios Clave de Ingeniería
1. **Desacoplamiento Temporal:** Los productores no necesitan esperar a que un consumidor termine un elemento específico para continuar generando nuevos registros.
2. **Control de Contrapresión (Backpressure):** Si la cola alcanza su capacidad máxima (`maxsize`), el productor se suspende de forma transparente hasta que un consumidor libera espacio.
3. **Concurrencia Escalonada:** Múltiples corrutinas consumidoras procesan en paralelo los elementos extraídos de la misma cola compartida de forma totalmente segura.
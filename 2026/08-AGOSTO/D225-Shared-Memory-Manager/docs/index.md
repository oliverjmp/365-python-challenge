# D225 - Shared Memory Manager

## 🏢 Resumen Ejecutivo y Alcance del Hito
El hito **D225** introduce arquitecturas de alto rendimiento para el intercambio de grandes volúmenes de datos numéricos entre procesos independientes mediante **`multiprocessing.shared_memory`**. Tradicionalmente, enviar información entre procesos requiere serialización (*pickle*) y duplicación de datos a través de pipes o sockets. Este núcleo implementa un enfoque de **Cero-Copia (Zero-Copy)** donde múltiples procesos leen y escriben directamente sobre el mismo bloque de memoria física del sistema operativo.

---

## 📐 Principios Clave de Ingeniería
1. **Eliminación del Overhead de Serialización:** Se evita por completo la codificación y decodificación de objetos complejos en formato binario para el transporte interprocesos.
2. **Vistas de Memoria con NumPy:** Acoplamiento directo de arreglos multidimensionales sobre los búferes de memoria compartida del sistema.
3. **Control Estricto de Ciclo de Vida:** Gestión segura de la asignación (`create=True`), vinculación por identificadores de nombre (`name`) y liberación explícita (`unlink`).
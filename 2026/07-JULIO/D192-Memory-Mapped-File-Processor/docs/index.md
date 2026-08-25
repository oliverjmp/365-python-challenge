# Memory Mapped File Processor (D192)

Procesador de ficheros binarios masivos de alto rendimiento mediante el mapeo directo en la memoria virtual del sistema operativo utilizando el módulo nativo **`mmap`** de Python, persistencia en el Data Lake y visualización avanzada en consola mediante **`rich`**.

## 🏛️ Características Técnicas
- **Mapeo en Memoria Virtual (`mmap`):** Acceso directo y lectura de archivos binarios pesados en disco sin saturar la memoria RAM de la aplicación.
- **Persistencia en Data Lake:** Gestión y almacenamiento de ficheros binarios estructurados en la ruta `data_lake/binary_records.bin`.
- **Escaneo con Métricas:** Búsqueda optimizada de patrones binarios calculando latencias exactas en milisegundos.

---

## 📊 Métricas de Rendimiento del Procesador

| Operación Binaria | Tamaño del Bloque | Modo de Acceso | Estado Técnico |
|:------------------|:------------------|:---------------|:---------------|
| **Generación de Stream Binario** | Estructura fija (Bytes) | Escritura Secuencial | ✅ **COMPLETADO** |
| **Mapeo Virtual del Archivo** | 100% del Fichero | `mmap.ACCESS_READ` | ✅ **COMPLETADO** |
| **Búsqueda de Patrones con Rich** | Escaneo en búfer CLI | Interfaz Estilizada | ✅ **COMPLETADO** |

> **Conclusión:** El mapeo directo reduce drásticamente el consumo de recursos al evitar la carga completa de archivos pesados en la memoria RAM, complementado con una interfaz de consola de nivel senior.
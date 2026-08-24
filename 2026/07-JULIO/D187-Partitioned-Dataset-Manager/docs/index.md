# Partitioned Dataset Manager (D187)

Escritura y lectura de datasets masivos particionados por criterios de fecha y región geográfica mediante **PyArrow Datasets**, optimizando el rendimiento de lectura mediante técnicas de *Partition Pruning*.

## 🏛️ Fundamentos de Arquitectura de Particionado
1. **Estructura de Directorios en Árbol:** Organización física de ficheros Parquet dividida por claves de negocio (`region=X/fecha=Y/file.parquet`), evitando el escaneo completo de tablas (*Full Table Scans*).
2. **Partition Pruning (Descarte de Particiones):** PyArrow analiza los filtros de la consulta antes de acceder al almacenamiento, abriendo únicamente los subdirectorios estrictamente necesarios.
3. **Alto Rendimiento de E/S:** Compresión columnar nativa que reduce drásticamente el uso de memoria en disco y RAM.

---

## 📈 Resultados del Administrador de Particiones

| Métrica de Rendimiento | Valor Registrado |
|:-----------------------|:-----------------|
| **Registros Totales Procesados** | 120,000 |
| **Tiempo de Escritura Particionada** | ~145.20 ms |
| **Latencia de Lectura con Pruning** | ~12.30 ms |
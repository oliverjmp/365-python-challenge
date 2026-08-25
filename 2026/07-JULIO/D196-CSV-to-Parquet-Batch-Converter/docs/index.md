# CSV to Parquet Batch Converter (D196)

Pipeline automatizado de conversión por lotes para ficheros CSV de gran tamaño, utilizando **Generadores de Python** para control de memoria RAM y escritura eficiente en formato columnar **PyArrow Parquet**.

## 🏛️ Características Técnicas
- **Procesamiento por Chunks (Generadores):** Lectura fragmentada de ficheros gigantes para evitar desbordamientos de memoria RAM (*Memory Overflow*).
- **Compresión Columnar:** Transformación directa a ficheros `.parquet` optimizados dentro del **Data Lake**.
- **Trazabilidad en Consola:** Monitoreo del progreso de conversión mediante barras de estado dinámicas con **`rich`**.

---

## 📊 Rendimiento del Pipeline

| Métrica de Conversión | Estado Técnico |
|:----------------------|:---------------|
| **Control de Memoria RAM** | ✅ Optimizado mediante Generators |
| **Escritura en Data Lake** | ✅ Formato Parquet Columnar |
| **Pruebas de Calidad** | ✅ Cobertura > 95% |
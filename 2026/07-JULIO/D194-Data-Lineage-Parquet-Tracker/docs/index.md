# Data Lineage Parquet Tracker (D194)

Sistema de rastreo automatizado de metadatos y linaje de datos para transformaciones con ficheros **Parquet**, respaldado por persistencia en el **Data Lake** y visualización ejecutiva en **Streamlit**.

## 🏛️ Características Técnicas
- **Rastreo de Metadatos:** Captura automática de esquemas, filas y dependencias entre datasets de entrada y salida.
- **Linaje de Datos (*Data Lineage*):** Mapeo de transformaciones upstream y downstream sobre ficheros Parquet.
- **Gobierno del Data Lake:** Auditoría centralizada de artefactos en la ruta `data_lake/`.

---

## 📊 Arquitectura de Linaje

| Capa de Datos | Fichero Parquet | Dependencia / Origen | Estado de Auditoría |
|:--------------|:----------------|:---------------------|:--------------------|
| **Raw Layer** | `raw_data.parquet` | Ingesta Directa (API/CSV) | ✅ **REGISTRADO** |
| **Processed Layer** | `processed_data.parquet` | Derivado de `raw_data.parquet` | ✅ **RASTREADO** |

> **Conclusión:** Permite a los ingenieros de datos auditar el ciclo de vida completo de la información sin perder trazabilidad en las transformaciones analíticas.
# Arquitectura de Contratos de Datos - D237

## 📐 Flujo de Validación

1. **Ingesta de Datos (Pandas DataFrame):** Recepción de lotes crudos desde orígenes externos.
2. **Contexto Efímero (Great Expectations):** Conversión a formato `gx.Dataset` en memoria sin necesidad de inicializar directorios persistentes pesados.
3. **Suite de Expectativas:** Aplicación matemática y categórica de rangos permitidos (ej. montos > 0).
4. **Veredicto:** Aprobación (Pase a producción) o Rechazo (Generación de alertas).
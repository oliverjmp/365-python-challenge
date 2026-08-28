# Arquitectura de Memoria Compartida Interprocesos - D225

## 📊 Diagrama de Componentes y Bloque Cero-Copia

```mermaid
graph TD
    Parent[Proceso Padre / Orquestador] -->|Asignación Inicial y create=True| SharedMem[(Segmento de Memoria Compartida OS)]
    
    Parent -->|Envío exclusivo de metadatos: Nombre, Forma y Tipo| Child[Proceso Hijo / Worker]

    subgraph Acceso Directo Zero-Copy
        Child -->|Conexión por nombre y mapeo de vista NumPy| SharedMem
        SharedMem -->|Modificación In-place sin copias| Child
    end

    Child -->|Retorno de estado y lectura directa final| Parent
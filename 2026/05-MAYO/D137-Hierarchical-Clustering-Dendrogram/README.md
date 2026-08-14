# D137 - Hierarchical Clustering & Dendrogram Analysis

Este hito implementa un **motor analítico para el análisis de conglomerados jerárquicos y la construcción de dendrogramas** utilizando `SciPy`, permitiendo agrupar datos de forma jerárquica ascendente (aglomerativa).

## Características Principales
- **Matriz de Enlace (Linkage Matrix):** Soporta múltiples métricas de distancia (`euclidean`, `manhattan`, etc.) y métodos de enlace (`ward`, `complete`, `average`, `single`).
- **Extracción de Conglomerados Planos:** Conversión del árbol jerárquico en particiones discretas mediante umbrales de distancia o número máximo de clusters (`fcluster`).
- **Estructuración Analítica de Dendrogramas:** Cálculo de coordenadas vectoriales para la representación gráfica e interpretación estructural sin dependencias de despliegue gráfico obligatorio.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
El clustering jerárquico es ideal cuando no se conoce de antemano el número exacto de conglomerados y se requiere entender la taxonomía o jerarquía natural de las observaciones.

### Ejemplos de Uso:
1. **Segmentación Taxonómica y Biología Computacional:**
   * *Caso:* Agrupar perfiles genéticos o especies según similitudes evolutivas.
   * *Uso:* Visualizar mediante un dendrograma las distancias de separación gradual entre especies.
2. **Segmentación de Clientes por Comportamiento de Compra:**
   * *Caso:* Agrupar clientes con base en su ticket promedio y frecuencia.
   * *Uso:* Determinar el punto de corte óptimo en el dendrograma para definir campañas de marketing dirigidas a subgrupos específicos.

## 📂 Estructura del Proyecto
```text
D137-Hierarchical-Clustering-Dendrogram/
│
├── src/
│   ├── __init__.py
│   └── cluster_analyzer.py
├── tests/
│   └── test_cluster_analyzer.py
├── run_clustering.py
├── requirements.txt
└── README.md
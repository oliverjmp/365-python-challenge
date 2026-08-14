# D136 - Unsupervised KMeans Clustering

Este hito implementa un **motor de agrupamiento no supervisado mediante K-Means** utilizando `Scikit-learn`, diseñado específicamente para la **segmentación inteligente de bases de datos de clientes**.

## Características Principales
- **Agrupamiento No Supervisado:** Agrupa observaciones en $K$ clústeres basándose en la proximidad geométrica de sus características (minimización de la inercia).
- **Validación Robusta de Entradas:** Controla de forma estricta DataFrames vacíos, arreglos nulos e hiperparámetros no válidos.
- **Asignación Escalable:** Permite ajustar el modelo con datos históricos (`fit_predict`) y clasificar nuevos perfiles de clientes en tiempo real (`predict`).

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En analítica de negocios y marketing, la segmentación de clientes permite personalizar estrategias comerciales sin requerir etiquetas previas.

### Ejemplos de Uso:
1. **Segmentación de Clientes por Comportamiento de Compra (RFM o Similares):**
   * *Caso:* Agrupar compradores por sus ingresos y frecuencia de gasto para campañas de fidelización dirigidas.
2. **Detección de Anomalías / Perfiles Atípicos:**
   * *Caso:* Identificar clústeres aislados de transacciones financieras con comportamientos fuera de lo común.

## 📂 Estructura del Proyecto
```text
D136-Unsupervised-KMeans-Clustering/
│
├── src/
│   ├── __init__.py
│   └── kmeans_clusterer.py
├── tests/
│   └── test_kmeans.py
├── run_kmeans.py
├── requirements.txt
└── README.md
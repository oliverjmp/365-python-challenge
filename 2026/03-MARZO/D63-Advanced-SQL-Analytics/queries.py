# Consulta SQL analítica avanzada utilizando CTEs y Window Functions
ADVANCED_FINANCIAL_TRENDS_QUERY = """
WITH DailyAggregates AS (
    -- Paso 1: Agregación base por fecha y categoría
    SELECT 
        transaction_date,
        category,
        SUM(amount) AS daily_amount
    FROM financial_transactions
    GROUP BY transaction_date, category
),
AnalyticalMetrics AS (
    -- Paso 2: Aplicación de Window Functions para tendencias y desviaciones
    SELECT 
        transaction_date,
        category,
        daily_amount,
        -- Media móvil de 7 días sobre los registros ordenados por fecha
        AVG(daily_amount) OVER (
            PARTITION BY category 
            ORDER BY transaction_date 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS moving_average_7d,
        -- Valor del día anterior utilizando LAG
        LAG(daily_amount, 1, 0.0) OVER (
            PARTITION BY category 
            ORDER BY transaction_date
        ) AS previous_day_amount
    FROM DailyAggregates
)
-- Paso 3: Selección final con cálculo de desviación porcentual de tendencia
SELECT 
    transaction_date,
    category,
    daily_amount,
    ROUND(moving_average_7d, 2) AS moving_average_7d,
    previous_day_amount,
    ROUND(
        CASE 
            WHEN moving_average_7d = 0 THEN 0.0 
            ELSE ((daily_amount - moving_average_7d) / moving_average_7d) * 100 
        END, 2
    ) AS trend_deviation_pct
FROM AnalyticalMetrics
ORDER BY transaction_date ASC;
"""
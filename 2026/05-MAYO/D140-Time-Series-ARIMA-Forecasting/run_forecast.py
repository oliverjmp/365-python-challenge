import logging
import pandas as pd
from src.arima_forecaster import ARIMAForecaster

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Pronóstico de Series Temporales con ARIMA (D140) ===")

    # Simulación de métricas financieras u operativas mensuales (ej. Ingresos en miles)
    financial_data = [
        1200, 1250, 1280, 1310, 1350, 1400, 
        1420, 1480, 1530, 1580, 1620, 1690
    ]

    logging.info(f"Datos históricos de entrada ({len(financial_data)} meses): {financial_data}")

    # Inicializar y ajustar el modelo ARIMA (p=1, d=1, q=1)
    logging.info("Ajustando modelo ARIMA(1, 1, 1)...")
    forecaster = ARIMAForecaster(order=(1, 1, 1))
    forecaster.fit(financial_data)
    logging.info("Modelo ajustado exitosamente.")

    # Generar pronóstico para los próximos 4 meses
    steps_ahead = 4
    logging.info(f"Generando pronóstico para los próximos {steps_ahead} meses...")
    forecasts = forecaster.forecast(steps=steps_ahead)

    for i, pred in enumerate(forecasts, start=1):
        logging.info(f" -> Mes T+{i}: Pronóstico de Ingresos = {pred:.2f}")

    # Mostrar extracto del resumen estadístico
    print("\n--- Resumen Estadístico del Modelo ARIMA ---")
    print(forecaster.get_summary()[:500] + "\n[...]")
    print("--------------------------------------------")

    logging.info("=== Hito D140 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()
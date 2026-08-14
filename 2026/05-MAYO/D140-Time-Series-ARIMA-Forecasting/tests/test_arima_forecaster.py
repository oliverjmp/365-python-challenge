import pytest
import numpy as np
import pandas as pd
from src.arima_forecaster import ARIMAForecaster

def test_empty_data_fit_raises_error():
    """Valida que pasar datos vacíos al ajuste lance un ValueError."""
    forecaster = ARIMAForecaster()
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        forecaster.fit([])

def test_nan_data_fit_raises_error():
    """Valida que una serie con valores NaN lance un ValueError."""
    forecaster = ARIMAForecaster()
    with pytest.raises(ValueError, match="contiene valores nulos"):
        forecaster.fit([10.0, np.nan, 12.0, 13.0])

def test_forecast_without_fit_raises_error():
    """Valida que intentar pronosticar sin ajustar lance un RuntimeError."""
    forecaster = ARIMAForecaster()
    with pytest.raises(RuntimeError, match="debe ser ajustado"):
        forecaster.forecast(steps=3)

def test_get_summary_without_fit_raises_error():
    """Valida que solicitar el resumen sin ajustar lance un RuntimeError."""
    forecaster = ARIMAForecaster()
    with pytest.raises(RuntimeError, match="debe estar ajustado"):
        forecaster.get_summary()

def test_invalid_steps_raises_error():
    """Valida que un número de pasos menor o igual a cero lance un ValueError."""
    forecaster = ARIMAForecaster()
    forecaster.fit([10, 12, 14, 16, 18, 20])
    with pytest.raises(ValueError, match="debe ser mayor a cero"):
        forecaster.forecast(steps=0)

def test_arima_forecaster_success():
    """Valida el flujo completo exitoso: ajuste, pronóstico y obtención de resumen."""
    # Serie temporal con tendencia lineal clara
    time_series = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

    forecaster = ARIMAForecaster(order=(1, 1, 0))
    forecaster.fit(time_series)

    # Pronosticar los siguientes 3 periodos
    predictions = forecaster.forecast(steps=3)
    
    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == 3
    assert not np.isnan(predictions).any()

    # Validar resumen estadístico
    summary = forecaster.get_summary()
    assert "ARIMAX" in summary or "ARIMA" in summary

def test_arima_fit_exception_raises_runtime_error(monkeypatch):
    """Valida que un fallo interno durante el ajuste lance un RuntimeError (línea 24)."""
    forecaster = ARIMAForecaster(order=(1, 1, 1))
    
    # Forzar que el método fit interno de ARIMA lance una excepción genérica
    from statsmodels.tsa.arima.model import ARIMA
    monkeypatch.setattr(ARIMA, "fit", lambda self: (_ for _ in()).throw(Exception("Fallo forzado")))
    
    with pytest.raises(RuntimeError, match="Error al ajustar el modelo ARIMA"):
        forecaster.fit([10, 12, 14, 16, 18])
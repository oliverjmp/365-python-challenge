import pytest
import pandas as pd
import numpy as np
from src.linear_regression_engine import MultipleLinearRegressionEngine

def test_empty_data_raises_error():
    """Valida que se lance un error si los datos de entrenamiento están vacíos (Cubre líneas de validación X/y vacío)."""
    engine = MultipleLinearRegressionEngine()
    
    # X vacío, y con datos
    with pytest.raises(ValueError, match="están vacíos"):
        engine.fit(pd.DataFrame(), pd.Series([1.0]))
        
    # X con datos, y vacío
    with pytest.raises(ValueError, match="están vacíos"):
        engine.fit(pd.DataFrame({"a": [1.0]}), pd.Series(dtype=float))

def test_mismatched_lengths_raises_error():
    """Valida que falle si X y y tienen longitudes diferentes."""
    engine = MultipleLinearRegressionEngine()
    X = pd.DataFrame({"feat1": [1.0, 2.0]})
    y = pd.Series([10.0]) # Longitud 1 vs 2 en X
    with pytest.raises(ValueError, match="no coincide"):
        engine.fit(X, y)

def test_predict_without_fit_raises_error():
    """Valida que se lance un error al predecir sin haber ajustado el modelo."""
    engine = MultipleLinearRegressionEngine()
    X = pd.DataFrame({"feat1": [1.0, 2.0]})
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.predict(X)

def test_evaluate_without_fit_raises_error():
    """Valida que evaluar sin ajustar lance un error."""
    engine = MultipleLinearRegressionEngine()
    X = pd.DataFrame({"feat1": [1.0, 2.0]})
    y = pd.Series([1.0, 2.0])
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.evaluate(X, y)

def test_coefficients_unfitted_raises_error():
    """Valida que consultar coeficientes o intercepto sin ajustar lance un error."""
    engine = MultipleLinearRegressionEngine()
    with pytest.raises(ValueError, match="no ha sido ajustado todavía"):
        _ = engine.coefficients
    with pytest.raises(ValueError, match="no ha sido ajustado todavía"):
        _ = engine.intercept

def test_predict_empty_dataframe_raises_error():
    """Valida que predecir con un DataFrame vacío arroje error si ya está ajustado."""
    X = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    y = pd.Series([5, 11, 17])
    engine = MultipleLinearRegressionEngine()
    engine.fit(X, y)
    
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.predict(pd.DataFrame())

def test_model_training_and_evaluation_workflow():
    """Flujo completo de entrenamiento, predicción, evaluación, residuos y propiedades."""
    np.random.seed(42)
    X = pd.DataFrame({
        "horas_estudio": [1, 2, 3, 4, 5, 6, 7, 8],
        "asistencia": [80, 85, 90, 92, 95, 96, 98, 100]
    })
    y = pd.Series([2 * row["horas_estudio"] + 0.5 * row["asistencia"] + np.random.normal(0, 0.1) for _, row in X.iterrows()])

    engine = MultipleLinearRegressionEngine()
    engine.fit(X, y)

    assert engine.is_fitted is True
    assert len(engine.feature_names_) == 2
    assert isinstance(engine.intercept, float)
    assert len(engine.coefficients) == 2

    metrics = engine.evaluate(X, y)
    assert "mse" in metrics
    assert "rmse" in metrics
    assert "r2" in metrics
    assert metrics["r2"] > 0.90

    # Probar análisis de residuos (pasando tanto Pandas Series como array numpy plano)
    residuals_df = engine.analyze_residuals(X, y.values)
    assert "y_true" in residuals_df.columns
    assert "y_pred" in residuals_df.columns
    assert "residual" in residuals_df.columns
    assert len(residuals_df) == len(X)
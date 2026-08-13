import pytest
import pandas as pd
import numpy as np
from src.scaler_engine import FeatureScalerEngine

def test_invalid_method_raises_error():
    """Valida que se lance un error si se pasa un método desconocido."""
    with pytest.raises(ValueError, match="Método de escalado no soportado"):
        FeatureScalerEngine(method="unknown_method")

def test_empty_dataframe_raises_error():
    """Valida que se lance un error si el DataFrame está vacío en fit_transform."""
    engine = FeatureScalerEngine(method="robust")
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.fit_transform(df_empty)

def test_transform_without_fit_raises_error():
    """Valida que falle si se intenta transformar sin ajustar antes."""
    engine = FeatureScalerEngine(method="robust")
    df = pd.DataFrame({"col1": [1.0, 2.0], "col2": [3.0, 4.0]})
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.transform(df)

def test_transform_empty_dataframe_raises_error():
    """Valida que se lance un error si se intenta transformar un DataFrame vacío con el motor ajustado."""
    data = {"col1": [1.0, 2.0, 3.0], "col2": [4.0, 5.0, 6.0]}
    df = pd.DataFrame(data)
    engine = FeatureScalerEngine(method="robust")
    engine.fit_transform(df)
    
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.transform(df_empty)

def test_robust_scaler_success():
    """Valida el funcionamiento correcto de RobustScaler con outliers."""
    data = {
        "feature_a": [1.0, 2.0, 3.0, 100.0],  # 100.0 es un outlier claro
        "feature_b": [10.0, 20.0, 30.0, 40.0]
    }
    df = pd.DataFrame(data)
    
    engine = FeatureScalerEngine(method="robust")
    result = engine.fit_transform(df)
    
    assert len(result) == 4
    assert not result.isnull().any().any()
    
    # Transformar nuevos datos
    new_data = pd.DataFrame({"feature_a": [2.5], "feature_b": [25.0]})
    transformed_new = engine.transform(new_data)
    assert len(transformed_new) == 1

def test_power_transformer_success():
    """Valida el funcionamiento correcto de PowerTransformer (Yeo-Johnson) para datos sesgados."""
    data = {
        "feature_skewed": [1.0, 1.5, 2.0, 10.0, 50.0]  # Distribución fuertemente sesgada a la derecha
    }
    df = pd.DataFrame(data)
    
    engine = FeatureScalerEngine(method="power")
    result = engine.fit_transform(df)
    
    assert len(result) == 5
    assert not result.isnull().any().any()
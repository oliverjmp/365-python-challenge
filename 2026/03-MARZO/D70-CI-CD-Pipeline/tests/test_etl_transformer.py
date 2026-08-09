import pytest
import pandas as pd
from src.etl_transformer import ETLTransformer


@pytest.fixture
def transformer():
    """Inicializa el transformador con un multiplicador estándar."""
    return ETLTransformer(multiplier=2.0)


@pytest.fixture
def sample_data():
    """Dataset para probar casos de éxito y de error."""
    return [
        {"id": 1, "value": 10.0, "category": "alpha"},
        {"id": 2, "value": 20.0, "category": "  beta  "},
        {"id": 3, "value": "no_numero", "category": "gamma"},
        {"missing_id": 4, "value": 5.0, "category": "delta"}
    ]


def test_transformacion_valida(transformer, sample_data):
    """Verifica que los datos válidos se transformen correctamente."""
    df = transformer.clean_and_transform(sample_data)
    assert len(df) == 2
    assert df.loc[0, "value"] == 20.0
    assert df.loc[1, "category"] == "BETA"


def test_df_vacio_si_no_hay_datos(transformer):
    """Verifica que devuelve un DataFrame vacío si no hay datos válidos."""
    df = transformer.clean_and_transform([{"wrong": "data"}])
    assert df.empty
    assert list(df.columns) == ["id", "value", "category"]
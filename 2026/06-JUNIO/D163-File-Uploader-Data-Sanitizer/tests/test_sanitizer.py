import pandas as pd
from src.sanitizer import sanitize_and_validate_dataframe

def test_sanitizer_valid_and_invalid():
    data = {
        "id": [1, -5, 3],
        "name": ["Ana", "B", "Carlos"],
        "score": [85.5, 50.0, 150.0], # -5 (id inválido) y 150.0 (score fuera de rango) darán error
        "active": [True, True, False]
    }
    df = pd.DataFrame(data)
    valid_df, errors = sanitize_and_validate_dataframe(df)

    assert len(valid_df) == 1 # Solo el registro 3 es perfectamente válido (id=3, name="Carlos", score=150.0 falla por le=100.0)
    assert len(errors) > 0

def test_sanitizer_unexpected_exception(monkeypatch):
    # Forzamos un comportamiento donde row.to_dict() o la validación dispare una excepción genérica
    class MockRow:
        def to_dict(self):
            raise RuntimeError("Error crítico inesperado")

    class MockDataFrame:
        def iterrows(self):
            return iter([(0, MockRow())])

    import src.sanitizer as sanitizer_mod
    valid_df, errors = sanitizer_mod.sanitize_and_validate_dataframe(MockDataFrame())
    
    assert len(valid_df) == 0
    assert len(errors) == 1
    assert errors[0]["field"] == "general"
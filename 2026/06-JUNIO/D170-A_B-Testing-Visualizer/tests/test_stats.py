from src.stats_analyzer import calculate_ab_test

def test_calculate_ab_test_significant():
    res = calculate_ab_test(1000, 100, 1000, 180)
    assert res["rate_a"] == 0.10
    assert res["rate_b"] == 0.18
    assert res["significant"] is True

def test_calculate_ab_test_zero_visitors():
    res = calculate_ab_test(0, 0, 0, 0)
    assert res["p_value"] == 1.0
    assert res["significant"] is False

def test_calculate_ab_test_zero_pooled():
    # Caso donde no hay ninguna conversión en absoluto (p_pooled == 0)
    res = calculate_ab_test(1000, 0, 1000, 0)
    assert res["p_value"] == 1.0
    assert res["significant"] is False

def test_calculate_ab_test_identical_rates():
    # Caso donde las tasas son exactamente iguales y sin varianza extrema
    res = calculate_ab_test(1000, 100, 1000, 100)
    assert res["p_value"] == 1.0
    assert res["significant"] is False

def test_calculate_ab_test_zero_se():
    # Tasas idénticas con conversiones > 0 para forzar se == 0 en el cálculo exacto de proporciones idénticas
    res = calculate_ab_test(1000, 100, 1000, 100)
    assert res["p_value"] == 1.0
    assert res["significant"] is False
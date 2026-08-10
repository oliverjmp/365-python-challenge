import pytest
from src.code_refactor_tool import CodeRefactorAnalyzer

def test_detect_long_functions():
    """Valida que el analizador detecte funciones que superan el límite máximo de líneas."""
    source_code = """
def short_func():
    return True

def long_func():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    return a + b + c + d + e + f + g + h + i + j + k
"""
    analyzer = CodeRefactorAnalyzer(max_lines=5)
    long_funcs = analyzer.analyze_source_code(source_code)
    
    assert "short_func" not in long_funcs
    assert "long_func" in long_funcs

def test_no_long_functions():
    """Valida que no se detecten anomalías si el código cumple con los estándares."""
    source_code = """
def clean_func():
    return 42
"""
    analyzer = CodeRefactorAnalyzer(max_lines=10)
    long_funcs = analyzer.analyze_source_code(source_code)
    
    assert long_funcs == []
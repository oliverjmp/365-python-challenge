"""
Suite de pruebas unitarias para el motor de rotación de proxies.
Utiliza Pytest para validar el comportamiento del pool y la resiliencia del cliente.
"""

import pytest
from scraper import ProxyConfig, ProxyRotatorPool


def test_proxy_pool_round_robin():
    """Valida la rotación secuencial (round-robin) de los proxies del pool."""
    proxies = ["http://proxy1:8080", "http://proxy2:8080"]
    pool = ProxyRotatorPool(proxies)

    first = pool.get_next_proxy()
    second = pool.get_next_proxy()
    third = pool.get_next_proxy()

    assert first == {"http": "http://proxy1:8080", "https": "http://proxy1:8080"}
    assert second == {"http": "http://proxy2:8080", "https": "http://proxy2:8080"}
    assert third == first  # Debe reiniciar el ciclo


def test_proxy_removal():
    """Valida la eliminación dinámica de un proxy defectuoso."""
    proxies = ["http://proxy1:8080", "http://proxy2:8080"]
    pool = ProxyRotatorPool(proxies)

    pool.remove_proxy({"http": "http://proxy1:8080", "https": "http://proxy1:8080"})

    assert len(pool._proxies) == 1
    assert "http://proxy1:8080" not in pool._proxies
    assert "http://proxy2:8080" in pool._proxies


def test_empty_proxy_pool():
    """Valida el comportamiento del pool cuando no se configuran proxies."""
    pool = ProxyRotatorPool([])
    result = pool.get_next_proxy()
    assert result is None
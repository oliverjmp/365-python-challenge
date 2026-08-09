import fakeredis
import pytest
from src.cache_manager import RedisCacheManager

@pytest.fixture
def fake_cache():
    """Fixture que provee un cliente Redis simulado en memoria."""
    server = fakeredis.FakeRedis(decode_responses=True)
    return RedisCacheManager(client=server)

def test_set_and_get_cache(fake_cache):
    """Valida el almacenamiento y recuperación de datos en la caché."""
    fake_cache.set_value("user:123", "Oliver")
    val = fake_cache.get_value("user:123")
    assert val == "Oliver"

def test_delete_cache(fake_cache):
    """Valida la eliminación de claves en la caché."""
    fake_cache.set_value("temp:key", "data")
    assert fake_cache.get_value("temp:key") == "data"
    
    fake_cache.delete_value("temp:key")
    assert fake_cache.get_value("temp:key") is None
    
def test_default_redis_client():
    """Valida la inicialización por defecto del cliente Redis."""
    manager = RedisCacheManager(host="localhost", port=6379, db=0)
    assert manager.client is not None
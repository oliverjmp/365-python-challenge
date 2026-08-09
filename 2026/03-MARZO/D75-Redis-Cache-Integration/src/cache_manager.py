import redis

class RedisCacheManager:
    """Gestor de caché basado en Redis para almacenamiento temporal."""

    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0, client=None):
        if client:
            self.client = client
        else:
            self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def set_value(self, key: str, value: str, expire_seconds: int = None) -> bool:
        """Almacena un valor en la caché con tiempo de expiración opcional."""
        return self.client.set(key, value, ex=expire_seconds)

    def get_value(self, key: str) -> str:
        """Recupera un valor de la caché usando su clave."""
        return self.client.get(key)

    def delete_value(self, key: str) -> int:
        """Elimina una clave de la caché."""
        return self.client.delete(key)
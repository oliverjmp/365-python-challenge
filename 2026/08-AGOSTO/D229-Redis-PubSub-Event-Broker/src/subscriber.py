import redis
import json
from typing import Callable, Any

class EventSubscriber:
    def __init__(self, host: str = "localhost", port: int = 6379, client=None):
        self.client = client if client else redis.Redis(host=host, port=port, decode_responses=True)
        self.pubsub = self.client.pubsub()

    def subscribe_to_channels(self, channels: list[str]):
        """Suscribe el cliente a una lista de canales."""
        self.pubsub.subscribe(*channels)

    def listen_events(self, callback: Callable[[dict], Any], timeout: float = 1.0):
        """Escucha eventos de forma segura utilizando un timeout para pruebas unitarias."""
        message = self.pubsub.get_message(ignore_subscribe_messages=True, timeout=timeout)
        if message and message["type"] == "message":
            try:
                data = json.loads(message["data"])
                callback(data)
                return data
            except json.JSONDecodeError:
                pass
        return None
import redis
import json

class EventPublisher:
    def __init__(self, host: str = "localhost", port: int = 6379, client=None):
        self.client = client if client else redis.Redis(host=host, port=port, decode_responses=True)

    def publish_event(self, channel: str, event_type: str, payload: dict) -> int:
        """Publica un evento estructurado en formato JSON a un canal de Redis."""
        message = {
            "event_type": event_type,
            "payload": payload
        }
        return self.client.publish(channel, json.dumps(message))
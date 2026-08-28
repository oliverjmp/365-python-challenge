import pytest
from unittest.mock import MagicMock
from src.publisher import EventPublisher
from src.subscriber import EventSubscriber

def test_publisher_send_event():
    mock_redis = MagicMock()
    mock_redis.publish.return_value = 1
    
    publisher = EventPublisher(client=mock_redis)
    subscribers_count = publisher.publish_event("orders", "ORDER_CREATED", {"order_id": 99})
    
    assert subscribers_count == 1
    mock_redis.publish.assert_called_once()

def test_subscriber_listen_events():
    mock_redis = MagicMock()
    mock_pubsub = MagicMock()
    
    mock_pubsub.get_message.return_value = {
        "type": "message",
        "data": '{"event_type": "USER_SIGNUP", "payload": {"username": "oliver"}}'
    }
    mock_redis.pubsub.return_value = mock_pubsub

    received_data = []
    def dummy_callback(event):
        received_data.append(event)

    subscriber = EventSubscriber(client=mock_redis)
    subscriber.subscribe_to_channels(["notifications"])
    
    event = subscriber.listen_events(dummy_callback)
    
    assert event["event_type"] == "USER_SIGNUP"
    assert event["payload"]["username"] == "oliver"
    assert len(received_data) == 1

def test_subscriber_listen_empty_message():
    mock_redis = MagicMock()
    mock_pubsub = MagicMock()
    mock_pubsub.get_message.return_value = None
    mock_redis.pubsub.return_value = mock_pubsub

    subscriber = EventSubscriber(client=mock_redis)
    event = subscriber.listen_events(lambda x: x)
    
    assert event is None

def test_subscriber_listen_invalid_json():
    mock_redis = MagicMock()
    mock_pubsub = MagicMock()
    mock_pubsub.get_message.return_value = {
        "type": "message",
        "data": "invalid-json-string"
    }
    mock_redis.pubsub.return_value = mock_pubsub

    subscriber = EventSubscriber(client=mock_redis)
    event = subscriber.listen_events(lambda x: x)
    
    assert event is None
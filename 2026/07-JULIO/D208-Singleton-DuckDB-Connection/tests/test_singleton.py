import pytest
import threading
from src.singleton_db import DuckDBConnectionSingleton

@pytest.fixture(autouse=True)
def reset_singleton():
    DuckDBConnectionSingleton.reset_instance()
    yield
    DuckDBConnectionSingleton.reset_instance()

def test_singleton_instance_equality():
    db1 = DuckDBConnectionSingleton()
    db2 = DuckDBConnectionSingleton()
    
    assert db1 is db2
    assert db1.connection is db2.connection

def test_singleton_thread_safety():
    instances = []

    def thread_target():
        inst = DuckDBConnectionSingleton()
        instances.append(inst)

    threads = [threading.Thread(target=thread_target) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    first_instance = instances[0]
    for inst in instances:
        assert inst is first_instance
        assert inst.connection is first_instance.connection

def test_singleton_reset_behavior():
    db1 = DuckDBConnectionSingleton()
    DuckDBConnectionSingleton.reset_instance()
    db2 = DuckDBConnectionSingleton()
    
    assert db1 is not db2
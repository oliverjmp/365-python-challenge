import pytest
from src.process_manager import OSProcessManager

def test_list_running_processes(monkeypatch):
    """Valida que se listen los procesos correctamente utilizando un mock de psutil."""
    class MockProcess:
        def __init__(self, info):
            self.info = info

    def mock_process_iter(attrs):
        return [
            MockProcess({"pid": 101, "name": "python.exe", "cpu_percent": 5.0, "memory_percent": 2.1}),
            MockProcess({"pid": 102, "name": "notepad.exe", "cpu_percent": 0.1, "memory_percent": 0.5})
        ]

    monkeypatch.setattr("psutil.process_iter", mock_process_iter)

    manager = OSProcessManager()
    procs = manager.list_running_processes()
    
    assert len(procs) == 2
    assert procs[0]["name"] == "python.exe"
    assert procs[1]["pid"] == 102

def test_check_and_terminate_heavy_processes(monkeypatch):
    """Valida la detección y terminación de procesos que superan los umbrales."""
    class MockPsutilProcess:
        def __init__(self, pid):
            self.pid = pid
        def terminate(self):
            pass

    class MockProcessInfo:
        def __init__(self, info):
            self.info = info

    def mock_process_iter(attrs):
        return [
            MockProcessInfo({"pid": 201, "name": "heavy_task.exe", "cpu_percent": 95.0, "memory_percent": 85.0}),
            MockProcessInfo({"pid": 202, "name": "System", "cpu_percent": 99.0, "memory_percent": 90.0})
        ]

    monkeypatch.setattr("psutil.process_iter", mock_process_iter)
    monkeypatch.setattr("psutil.Process", lambda pid: MockPsutilProcess(pid))

    manager = OSProcessManager(cpu_threshold=80.0, mem_threshold=80.0)
    terminated = manager.check_and_terminate_heavy_processes()

    assert len(terminated) == 1
    assert terminated[0]["name"] == "heavy_task.exe"
    assert terminated[0]["pid"] == 201

def test_process_manager_exceptions(monkeypatch):
    """Valida el manejo seguro de excepciones (NoSuchProcess) durante el monitoreo."""
    import psutil

    def mock_process_iter_exception(attrs):
        class FaultyProcess:
            @property
            def info(self):
                raise psutil.NoSuchProcess(pid=999)
        return [FaultyProcess()]

    monkeypatch.setattr("psutil.process_iter", mock_process_iter_exception)

    manager = OSProcessManager()
    procs = manager.list_running_processes()
    assert procs == []

    terminated = manager.check_and_terminate_heavy_processes()
    assert terminated == []
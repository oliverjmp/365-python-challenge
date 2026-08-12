import os
import pickle
import pytest
from src.session_persistence import SessionPersistence

def test_initialization():
    """Valida los valores iniciales de la clase."""
    manager = SessionPersistence(cookie_file="test_cookies.pkl", headless=True)
    assert manager.headless is True
    assert manager.driver is None
    assert manager.cookie_file == "test_cookies.pkl"

def test_save_cookies_success(monkeypatch):
    """Valida el proceso exitoso de guardado de cookies simulando Selenium."""
    manager = SessionPersistence(cookie_file="test_cookies.pkl", headless=True)
    
    class MockBrowser:
        def get(self, url):
            pass
        def get_cookies(self):
            return [{"name": "session_id", "value": "12345"}]
        def quit(self):
            pass

    monkeypatch.setattr("src.session_persistence.ChromeDriverManager.install", lambda *args, **kwargs: "path")
    monkeypatch.setattr("src.session_persistence.webdriver.Chrome", lambda *args, **kwargs: MockBrowser())

    success = manager.save_cookies("http://valid.url.test.local")
    assert success is True
    assert os.path.exists("test_cookies.pkl")
    
    if os.path.exists("test_cookies.pkl"):
        os.remove("test_cookies.pkl")

def test_load_session_with_cookies(monkeypatch):
    """Valida la carga y restauración de cookies mediante pickle."""
    manager = SessionPersistence(cookie_file="test_cookies.pkl", headless=True)
    
    mock_cookies = [{"name": "session_id", "value": "abcde"}]
    with open("test_cookies.pkl", "wb") as f:
        pickle.dump(mock_cookies, f)

    class MockBrowserSession:
        def get(self, url):
            pass
        def add_cookie(self, cookie):
            pass
        def refresh(self):
            pass
        def quit(self):
            pass

    monkeypatch.setattr("src.session_persistence.ChromeDriverManager.install", lambda *args, **kwargs: "path")
    monkeypatch.setattr("src.session_persistence.webdriver.Chrome", lambda *args, **kwargs: MockBrowserSession())

    success = manager.load_session_with_cookies("http://valid.url.test.local")
    assert success is True

    if os.path.exists("test_cookies.pkl"):
        os.remove("test_cookies.pkl")

def test_load_session_file_not_found(monkeypatch):
    """Valida el comportamiento cuando el archivo de cookies no existe."""
    manager = SessionPersistence(cookie_file="nonexistent_cookies.pkl", headless=True)
    
    class MockBrowserEmpty:
        def get(self, url):
            pass
        def quit(self):
            pass

    monkeypatch.setattr("src.session_persistence.ChromeDriverManager.install", lambda *args, **kwargs: "path")
    monkeypatch.setattr("src.session_persistence.webdriver.Chrome", lambda *args, **kwargs: MockBrowserEmpty())

    success = manager.load_session_with_cookies("http://valid.url.test.local")
    assert success is False
import pytest
from src.auth_automation import HeadlessAuthAutomation

def test_automation_initialization():
    """Valida la inicialización de la clase."""
    bot = HeadlessAuthAutomation(headless=True)
    assert bot.headless is True
    assert bot.driver is None

def test_initialize_driver_directly(monkeypatch):
    """Valida la creación directa del driver mediante mock."""
    bot = HeadlessAuthAutomation(headless=True)
    
    class MockBrowser:
        def quit(self):
            pass

    monkeypatch.setattr("src.auth_automation.ChromeDriverManager.install", lambda *args, **kwargs: "path")
    monkeypatch.setattr("src.auth_automation.webdriver.Chrome", lambda *args, **kwargs: MockBrowser())

    driver = bot.initialize_driver()
    assert driver is not None
    bot.close()

def test_login_flow_success_path(monkeypatch):
    """Valida el flujo exitoso cubriendo la línea de navegación get()."""
    bot = HeadlessAuthAutomation(headless=True)
    
    class MockBrowserSuccess:
        def get(self, url):
            pass
        def quit(self):
            pass

    monkeypatch.setattr("src.auth_automation.ChromeDriverManager.install", lambda *args, **kwargs: "path")
    monkeypatch.setattr("src.auth_automation.webdriver.Chrome", lambda *args, **kwargs: MockBrowserSuccess())

    success = bot.simulate_login_flow("http://valid.url.test.local", "user", "pass", "123456")
    assert success is True

def test_login_flow_exception_handling(monkeypatch):
    """Valida el manejo de excepciones en el flujo."""
    bot = HeadlessAuthAutomation(headless=True)
    
    class MockBrowserException:
        def get(self, url):
            raise Exception("Error de red")
        def quit(self):
            pass

    monkeypatch.setattr("src.auth_automation.ChromeDriverManager.install", lambda *args, **kwargs: "path")
    monkeypatch.setattr("src.auth_automation.webdriver.Chrome", lambda *args, **kwargs: MockBrowserException())

    success = bot.simulate_login_flow("http://invalid.url.test.local", "user", "pass", "123456")
    assert success is False

def test_driver_explicit_close():
    """Valida el cierre explícito del driver."""
    bot = HeadlessAuthAutomation(headless=True)
    bot.close()
    
    class MockBrowser:
        def quit(self):
            pass
            
    bot.driver = MockBrowser()
    bot.close()
    assert bot.driver is None
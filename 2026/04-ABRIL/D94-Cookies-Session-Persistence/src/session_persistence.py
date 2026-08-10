import pickle
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SessionPersistence:
    def __init__(self, cookie_file: str = "cookies.pkl", headless: bool = True):
        self.cookie_file = cookie_file
        self.headless = headless
        self.driver = None

    def initialize_driver(self) -> webdriver.Chrome:
        """Inicializa el WebDriver de Chrome en modo Headless o normal."""
        options = Options()
        if self.headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return self.driver

    def save_cookies(self, url: str) -> bool:
        """Navega a una URL, espera la interacción y guarda las cookies actuales en disco."""
        try:
            if not self.driver:
                self.initialize_driver()
            
            self.driver.get(url)
            # Obtenemos las cookies activas de la sesión del navegador
            cookies = self.driver.get_cookies()
            
            with open(self.cookie_file, "wb") as file:
                pickle.dump(cookies, file)
            return True
        except Exception:
            return False
        finally:
            self.close()

    def load_session_with_cookies(self, url: str) -> bool:
        """Carga las cookies guardadas previamente e inicia sesión de forma persistente."""
        try:
            if not self.driver:
                self.initialize_driver()
            
            # Primero cargamos el dominio base para que el navegador acepte las cookies
            self.driver.get(url)
            
            if os.path.exists(self.cookie_file):
                with open(self.cookie_file, "rb") as file:
                    cookies = pickle.load(file)
                    for cookie in cookies:
                        # Añadimos cada cookie almacenada al navegador
                        self.driver.add_cookie(cookie)
                
                # Refrescamos la página para aplicar la sesión restaurada
                self.driver.refresh()
                return True
            return False
        except Exception:
            return False
        finally:
            self.close()

    def close(self) -> None:
        """Cierra el navegador de forma segura."""
        if self.driver:
            self.driver.quit()
            self.driver = None
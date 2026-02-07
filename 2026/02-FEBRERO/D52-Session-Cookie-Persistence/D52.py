"""
Proyecto: 365 Python Challenge
Día 52: Session & Cookie Persistence
Objetivo: Simular un login y mantener la sesión activa para navegar por páginas protegidas.
"""

import requests
from bs4 import BeautifulSoup

class SessionBot:
    def __init__(self):
        # El objeto Session mantiene las cookies automáticamente
        self.session = requests.Session()
        self.base_url = "https://httpbin.org" # Servicio para pruebas de peticiones
        
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OliverAuthBot/1.0"
        })

    def simulate_login(self, user, password):
        print(f"🔐 Intentando login para el usuario: {user}...")
        
        # Datos que enviaríamos en un formulario de login real
        login_data = {
            "user": user,
            "password": password
        }

        # Usamos POST para enviar credenciales (más seguro que GET)
        # httpbin.org/post nos devolverá lo que enviamos para confirmar
        try:
            response = self.session.post(f"{self.base_url}/post", data=login_data)
            response.raise_for_status()
            
            print("✅ Login exitoso (Simulado). Sesión iniciada.")
            print(f"🍪 Cookies actuales en el tarro: {self.session.cookies.get_dict()}")
            
        except Exception as e:
            print(f"❌ Error en la autenticación: {e}")

    def access_private_area(self):
        print("\n🕵️ Intentando acceder a zona privada con la sesión actual...")
        
        # Pedimos al servidor que nos devuelva las cookies que él ve en nosotros
        try:
            response = self.session.get(f"{self.base_url}/cookies")
            print(f"📡 Respuesta del servidor: {response.json()}")
            
            if response.status_code == 200:
                print("🔓 Acceso concedido: El servidor reconoce nuestra identidad.")
            else:
                print("🔒 Acceso denegado: Sesión inválida.")
                
        except Exception as e:
            print(f"❌ Error de acceso: {e}")

if __name__ == "__main__":
    bot = SessionBot()
    
    # 1. Realizamos el login
    bot.simulate_login("OliverEngineer", "Python365_Secret")
    
    # 2. Navegamos manteniendo la sesión (sin tener que volver a loguearnos)
    bot.access_private_area()

    print("\n" + "═"*50)
    print("✨ Hito D52: Gestión de Sesiones Completada")
    print("═"*50)
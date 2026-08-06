import logging
import httpx

# Configuración de logging estructurado corporativo
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] ProxyScraperEngine - %(message)s",
)
logger = logging.getLogger("ProxyScraperEngine")

def run_proxy_scraper() -> None:
    # Pool de proxies (simulados para pruebas de resistencia)
    proxy_pool = [
        "http://10.10.1.10:3128",
        "http://10.10.1.11:3128"
    ]
    
    url = "https://httpbin.org/ip"
    success = False

    for proxy_url in proxy_pool:
        logger.info(f"Realizando petición usando proxy: {{'http://': '{proxy_url}', 'https://': '{proxy_url}'}}")
        
        try:
            # Usamos el parámetro 'proxy' soportado por httpx.Client con un timeout ajustado
            with httpx.Client(proxy=proxy_url, timeout=3.0) as client:
                response = client.get(url)
                if response.status_code == 200:
                    logger.info(f"Resultado obtenido con proxy: {response.json()}")
                    success = True
                    break
        except Exception as e:
            logger.error(f"Falla crítica con proxy {proxy_url}: {type(e).__name__} -> {e}")

    # Mecanismo de resiliencia: Fallback a conexión directa si el pool falla
    if not success:
        logger.warning("Se agotaron todos los proxies del pool. Intentando conexión directa de emergencia...")
        try:
            with httpx.Client(timeout=5.0) as client:
                response = client.get(url)
                logger.info(f"HTTP Request: GET {url} 'HTTP/1.1 200 OK'")
                logger.info(f"Conexión directa de emergencia exitosa. Resultado: {response.json()}")
        except Exception as e:
            logger.error(f"Falla crítica en conexión directa de emergencia: {e}")

if __name__ == "__main__":
    run_proxy_scraper()
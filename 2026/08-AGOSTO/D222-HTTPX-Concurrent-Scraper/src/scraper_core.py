import asyncio
import httpx

class HTTPXConcurrentScraper:
    """Núcleo de ingesta web concurrente masiva optimizada con HTTPX y Keep-Alive."""

    async def fetch_url(self, client: httpx.AsyncClient, url: str) -> dict:
        """Realiza una petición asíncrona individual utilizando el cliente Keep-Alive."""
        try:
            start_time = asyncio.get_event_loop().time()
            response = await client.get(url, timeout=5.0)
            duration = asyncio.get_event_loop().time() - start_time
            return {
                "url": url,
                "status_code": response.status_code,
                "duration": round(duration, 4),
                "success": response.is_success
            }
        except Exception as e:
            return {
                "url": url,
                "status_code": 0,
                "duration": 0.0,
                "success": False,
                "error": str(e)
            }

    async def scrape_batch(self, urls: list[str]) -> dict:
        """Ejecuta un lote masivo de peticiones concurrentes reutilizando conexiones Keep-Alive."""
        if not urls:
            raise ValueError("La lista de URLs a ingestar no puede estar vacía.")

        limits = httpx.Limits(max_keepalive_connections=20, max_connections=50)
        async with httpx.AsyncClient(limits=limits, http2=False) as client:
            tasks = [self.fetch_url(client, url) for url in urls]
            results = await asyncio.gather(*tasks)

        successful = sum(1 for r in results if r["success"])
        return {
            "total_urls": len(urls),
            "successful_requests": successful,
            "failed_requests": len(urls) - successful,
            "results": results
        }
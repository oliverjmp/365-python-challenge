import asyncio
from src.scraper_core import HTTPXConcurrentScraper

async def main():
    print("=== D222: Ingesta Web Concurrente con HTTPX y Keep-Alive ===")
    scraper = HTTPXConcurrentScraper()
    
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/status/200",
        "https://httpbin.org/uuid",
        "https://httpbin.org/json"
    ]
    
    print(f"[i] Procesando de forma concurrente {len(urls)} endpoints...")
    summary = await scraper.scrape_batch(urls)
    
    print(f"[✔] Total procesadas: {summary['total_urls']}")
    print(f"[✔] Exitosas: {summary['successful_requests']}")
    print(f"[✔] Fallidas: {summary['failed_requests']}")

if __name__ == "__main__":
    asyncio.run(main())
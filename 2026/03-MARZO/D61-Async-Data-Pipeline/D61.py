import asyncio
import httpx
import time
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Async-Pipeline-Artifact")

ENDPOINTS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/json",
    "https://httpbin.org/uuid",
    "https://httpbin.org/user-agent",
    "https://httpbin.org/headers",
    "https://httpbin.org/ip"
]

MAX_CONCURRENT_REQUESTS = 3
sem = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

async def fetch_source_controlled(client: httpx.AsyncClient, url: str) -> Dict[str, Any]:
    async with sem:
        start_time = time.perf_counter()
        try:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()
            elapsed = time.perf_counter() - start_time
            logger.info(f"Éxito | URL: {url} | Latencia: {elapsed:.3f}s")
            return {
                "url": url,
                "status": response.status_code,
                "latency_seconds": round(elapsed, 4),
                "data": response.json()
            }
        except httpx.HTTPError as e:
            logger.error(f"Fallo de red en {url}: {str(e)}")
            return {
                "url": url,
                "status": "error",
                "error_message": str(e)
            }

async def run_pipeline(urls: List[str]) -> List[Dict[str, Any]]:
    async with httpx.AsyncClient() as client:
        tasks = [fetch_source_controlled(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

def main():
    total_start = time.perf_counter()
    results = asyncio.run(run_pipeline(ENDPOINTS))
    total_elapsed = time.perf_counter() - total_start
    
    pipeline_report = {
        "execution_time_seconds": round(total_elapsed, 4),
        "total_sources_queried": len(ENDPOINTS),
        "max_concurrency_limit": MAX_CONCURRENT_REQUESTS,
        "payloads": results
    }
    
    # --- SOLUCIÓN ARQUITECTÓNICA ---
    # Obtenemos la ruta absoluta del directorio donde vive este script (D61.py)
    current_dir = Path(__file__).resolve().parent
    output_path = current_dir / "pipeline_metrics.json"
    
    output_path.write_text(json.dumps(pipeline_report, indent=4), encoding="utf-8")
    logger.info(f"[SUCCESS] Artefacto de métricas exportado correctamente en: {output_path}")

if __name__ == "__main__":
    main()
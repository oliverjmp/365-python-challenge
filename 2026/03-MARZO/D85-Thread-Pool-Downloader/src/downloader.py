import concurrent.futures
import requests
from typing import List, Dict, Any

class ThreadPoolDownloader:
    def __init__(self, max_workers: int = 5):
        self.max_workers = max_workers

    def fetch_resource(self, url: str) -> Dict[str, Any]:
        """Realiza la petición HTTP para descargar un recurso individual."""
        try:
            response = requests.get(url, timeout=5)
            return {
                "url": url,
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "content_length": len(response.content)
            }
        except Exception as e:
            return {
                "url": url,
                "status_code": None,
                "success": False,
                "error": str(e)
            }

    def download_all(self, urls: List[str]) -> List[Dict[str, Any]]:
        """Descarga múltiples URLs de forma concurrente usando ThreadPoolExecutor."""
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {executor.submit(self.fetch_resource, url): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                results.append(future.result())
        return results
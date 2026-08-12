import asyncio
import httpx
from typing import List, Dict, Any
from pathlib import Path

class AsyncFileUploader:
    def __init__(self, target_url: str, timeout: float = 30.0):
        """Inicializa el uploader asíncrono con la URL de destino y un timeout por defecto."""
        self.target_url = target_url
        self.timeout = timeout

    async def upload_single_file(self, client: httpx.AsyncClient, file_path: Path) -> Dict[str, Any]:
        """Sube un único archivo de forma asíncrona al servidor remoto."""
        if not file_path.exists():
            return {"file": file_path.name, "status": "failed", "error": "File not found"}

        try:
            with open(file_path, "rb") as f:
                files = {"file": (file_path.name, f)}
                response = await client.post(self.target_url, files=files, timeout=self.timeout)
                
                if response.status_code == 200:
                    return {"file": file_path.name, "status": "success", "status_code": response.status_code}
                else:
                    return {"file": file_path.name, "status": "failed", "status_code": response.status_code}
        except Exception as e:
            return {"file": file_path.name, "status": "failed", "error": str(e)}

    async def upload_batch(self, file_paths: List[Path]) -> List[Dict[str, Any]]:
        """Sube un lote de ficheros de forma concurrente utilizando asyncio.gather."""
        async with httpx.AsyncClient() as client:
            tasks = [self.upload_single_file(client, fp) for fp in file_paths]
            results = await asyncio.gather(*tasks)
            return list(results)
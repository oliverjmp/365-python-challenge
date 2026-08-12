import asyncio
import logging
from pathlib import Path
from src.uploader import AsyncFileUploader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def main():
    logging.info("=== Iniciando Servicio Asíncrono de Transferencia de Ficheros (Hito D108) ===")
    
    # Crear algunos archivos temporales de prueba locales
    temp_dir = Path("temp_files")
    temp_dir.mkdir(exist_ok=True)
    
    file_paths = []
    for i in range(1, 4):
        fp = temp_dir / f"document_{i}.dat"
        fp.write_bytes(b"0" * 1024 * 100) # 100 KB simulados por fichero
        file_paths.append(fp)

    # URL simulada de subida (en entorno real apuntaría al servidor remoto)
    target_url = "https://httpbin.org/post"
    
    uploader = AsyncFileUploader(target_url=target_url)
    
    logging.info(f"Iniciando subida concurrente de {len(file_paths)} ficheros hacia {target_url}...")
    results = await uploader.upload_batch(file_paths)
    
    for res in results:
        logging.info(f"Resultado de transferencia: {res}")

    # Limpieza de ficheros temporales
    for fp in file_paths:
        if fp.exists():
            fp.unlink()
    if temp_dir.exists():
        temp_dir.rmdir()

    logging.info("=== Hito D108 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    asyncio.run(main())
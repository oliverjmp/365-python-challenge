# D101 - Docker Multi-Stage Build

Este proyecto aborda la **contenedorización optimizada de microservicios mediante compilación multi-etapa** en Docker utilizando Python y FastAPI.

## Características Principales
- **Multi-Stage Build:** Separa el entorno de construcción/compilación de dependencias del entorno final de ejecución, logrando una imagen ligera y segura para producción.
- **Microservicio Escalable:** API basada en FastAPI con endpoints de estado y control de salud (`/health`).
- **Pruebas Unitarias Rigurosas:** Cobertura de código validada al 100% con `pytest` y `TestClient`.

## Requisitos del Entorno
- Python 3.11 o superior.
- Docker Desktop instalado (opcional para pruebas de contenedores).

## Instrucciones de Instalación y Ejecución

1. **Instalar dependencias locales:**
   ```powershell
   python -m pip install -r requirements.txt
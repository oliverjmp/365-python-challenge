# Arquitectura del Sistema de Integración Continua (CI/CD) - D220

## 📊 Diagrama de Secuencia y Componentes del Pipeline

```mermaid
graph TD
    subgraph Entorno de Desarrollo Local
        Dev[Desarrollador / Git Commit] -->|Git Push / Pull Request| GitHub[Repositorio Remoto GitHub]
    end

    subgraph Orquestación Cloud (GitHub Actions Runners)
        GitHub -->|Disparador de Evento (Trigger)| Workflow[.github/workflows/ci.yml]
        
        subgraph Matriz de Ejecución Paralela
            Workflow --> JobPy10[Job: Python 3.10]
            Workflow --> JobPy11[Job: Python 3.11]
            Workflow --> JobPy12[Job: Python 3.12]
        end

        JobPy10 --> Steps[Pasos del Pipeline: Checkout -> Setup -> Install -> Test with Coverage]
        JobPy11 --> Steps
        JobPy12 --> Steps
    end

    subgraph Validación de Calidad
        Steps --> Pytest[Ejecución de pytest --cov-fail-under=100]
        Pytest -->|Éxito 100%| Success[Aprobación del Build]
        Pytest -->|Fallo o < 100%| Failure[Bloqueo del Merge / Alerta al Dev]
    end
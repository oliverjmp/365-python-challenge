import time
import typer
from rich.console import Console
from rich.table import Table
from rich.progress import track

app = typer.Typer(help="Panel de Control CLI - Reto D103")
console = Console()

@app.command("status")
def status():
    """Muestra el estado general del sistema en una tabla estilizada."""
    console.print("\n[bold cyan]=== Panel de Control: Estado del Sistema ===[/bold cyan]\n")
    
    table = Table(title="Servicios Activos (D103)")
    table.add_column("Servicio", style="magenta", no_wrap=True)
    table.add_column("Estado", style="green")
    table.add_column("Latencia", style="yellow")

    table.add_row("Base de Datos PostgreSQL", "ONLINE", "12 ms")
    table.add_row("API Gateway (FastAPI)", "ONLINE", "24 ms")
    table.add_row("Worker de Procesamiento", "IDLE", "5 ms")

    console.print(table)
    console.print()

@app.command("deploy")
def deploy(environment: str = typer.Option("staging", "--environment", "-e", help="Entorno de despliegue")):
    """Simula un proceso de despliegue con barra de progreso en consola."""
    console.print(f"\n[bold yellow]Iniciando despliegue hacia el entorno: [{environment.upper()}]...[/bold yellow]\n")

    steps = [
        "Verificando dependencias...",
        "Compilando contenedores Docker...",
        "Ejecutando pruebas unitarias...",
        "Aplicando migraciones de base de datos...",
        "Reiniciando servicios..."
    ]

    for step in track(steps, description="[green]Desplegando..."):
        time.sleep(0.01)

    console.print(f"\n[bold green]¡Despliegue a '{environment}' completado con éxito![/bold green]\n")

if __name__ == "__main__":  # pragma: no cover
    app()
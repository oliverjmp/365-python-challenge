from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint
from src.fts_engine import DuckDBFTSEngine

console = Console()

def main():
    console.print(Panel.fit(
        "[bold cyan]D193 - MOTOR DE BÚSQUEDA DE TEXTO COMPLETO (DUCKDB FTS)[/bold cyan]\n"
        "[italic]Indexación y consulta ultrarrápida de logs masivos en el Data Lake[/italic]",
        border_style="blue"
    ))
    
    engine = DuckDBFTSEngine()
    termino_busqueda = "error"
    
    console.print(f"\n[yellow]🔍 Buscando término clave:[/yellow] [bold magenta]'{termino_busqueda}'[/bold magenta] en el Data Lake...")
    
    with console.status("[bold green]Consultando índice FTS..."):
        resultado = engine.buscar_logs(termino_busqueda)
        
    console.print(f"[bold green]✔[/bold green] Búsqueda ejecutada en [cyan]{resultado['duracion_ms']} ms[/cyan]. Se encontraron [cyan]{len(resultado['filas'])}[/cyan] registros.\n")
    
    table = Table(title=f"Resultados FTS para: '{termino_busqueda}'")
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nivel", justify="center", style="yellow")
    table.add_column("Mensaje de Log", style="green")
    table.add_column("Timestamp", justify="center", style="magenta")
    table.add_column("Score FTS", justify="right", style="blue")
    
    for row in resultado["filas"]:
        log_id, nivel, mensaje, timestamp, score = row
        table.add_row(
            str(log_id),
            nivel,
            mensaje,
            str(timestamp),
            str(round(score, 4))
        )
        
    console.print(table)
    rprint("\n[bold blue]==================================================================[/bold blue]")
    rprint("[bold green]      ¡BÚSQUEDA FTS CON RICH FINALIZADA CON ÉXITO!                [/bold green]")
    rprint("[bold blue]==================================================================[/bold blue]")

if __name__ == "__main__":
    main()
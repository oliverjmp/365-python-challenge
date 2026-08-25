from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint
from src.mmap_engine import MemoryMappedFileProcessor

console = Console()

def main():
    console.print(Panel.fit(
        "[bold cyan]D192 - PROCESADOR DE ARCHIVOS MASIVOS CON MMAP[/bold cyan]\n"
        "[italic]Mapeo directo en memoria virtual del OS + Data Lake[/italic]",
        border_style="blue"
    ))
    
    processor = MemoryMappedFileProcessor()
    patron_busqueda = b"DATA"
    
    with console.status("[bold green]Escaneando búfer virtual en disco..."):
        resultado = processor.buscar_patron_con_metricas(patron_busqueda)
    
    console.print(f"\n[bold green]✔[/bold green] Escaneo completado en [cyan]{resultado['duracion_ms']} ms[/cyan] sobre un fichero de [cyan]{resultado['tamano_archivo_bytes']} bytes[/cyan].\n")
    
    # Crear tabla estilizada con rich
    table = Table(title="Resultados del Escaneo Binario (Offsets mmap)")
    table.add_column("Índice", justify="center", style="cyan", no_wrap=True)
    table.add_column("Offset (Bytes)", justify="right", style="magenta")
    table.add_column("Patrón", justify="center", style="yellow")
    table.add_column("Bloque Extraído (30 Bytes)", style="green")
    
    for idx, pos in enumerate(resultado["coincidencias"]):
        bloque = processor.leer_bloque(pos, 30)
        table.add_row(
            str(idx + 1),
            str(pos),
            resultado["patron"],
            str(bloque)
        )
        
    console.print(table)
    rprint("\n[bold blue]==================================================================[/bold blue]")
    rprint("[bold green]      ¡PROCESAMIENTO MMAP CON RICH FINALIZADO CON ÉXITO!          [/bold green]")
    rprint("[bold blue]==================================================================[/bold blue]")

if __name__ == "__main__":
    main()
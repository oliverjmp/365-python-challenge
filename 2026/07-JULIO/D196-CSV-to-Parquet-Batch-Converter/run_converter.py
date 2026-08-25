from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from src.batch_converter import CSVParquetBatchConverter

console = Console()

def main():
    console.print(Panel.fit(
        "[bold cyan]D196 - PIPELINE DE CONVERSIÓN CSV A PARQUET POR LOTES[/bold cyan]\n"
        "[italic]Optimización de memoria RAM mediante Generadores de Python y PyArrow[/italic]",
        border_style="blue"
    ))
    
    converter = CSVParquetBatchConverter()
    csv_file = "dataset_gigante.csv"
    parquet_file = "dataset_optimizado.parquet"
    
    console.print(f"\n[yellow]⚙️ Iniciando procesamiento por lotes del fichero:[/yellow] [magenta]{csv_file}[/magenta]")
    
    with console.status("[bold green]Convirtiendo bloques al Data Lake..."):
        total_filas = converter.convertir_a_parquet(csv_file, parquet_file, chunksize=2500)
        
    console.print(f"[bold green]✔[/bold green] ¡Conversión completada con éxito! Se procesaron [cyan]{total_filas:,} filas[/cyan] en formato columnar Parquet.")
    console.print(f"[bold blue]📁 Destino:[/bold blue] data_lake/processed/{parquet_file}\n")

if __name__ == "__main__":
    main()
import typer

app = typer.Typer(help="Centro de comandos CLI para orquestación de pipelines.")


@app.command()
def run_pipeline(name: str = "default_pipeline", dry_run: bool = False):
    """Ejecuta un pipeline de datos específico."""
    typer.echo(f"Iniciando pipeline: {name}...")
    
    if dry_run:
        typer.echo("Modo simulación (dry-run) activado. No se realizaron cambios.")
        return

    typer.echo(f"Pipeline '{name}' ejecutado exitosamente.")


if __name__ == "__main__":
    app()
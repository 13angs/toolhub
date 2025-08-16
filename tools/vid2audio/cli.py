import typer
from rich.console import Console
from pathlib import Path

from .main import convert_video_to_audio

# --- CLI Setup ---
app = typer.Typer(help="Convert video files to audio format.")
console = Console()

@app.command(
    name="convert",
    help="Extracts audio from a video file and saves it."
)
def convert_cli(
    input_file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path to the input video file."
    ),
    output_format: str = typer.Option(
        "mp3",
        "--format",
        "-f",
        help="The desired audio format (e.g., mp3, wav, aac)."
    )
):
    """
    CLI command to convert a video file to an audio file.
    This function handles user interaction, constructs file paths,
    calls the core logic from main.py, and prints results to the console.
    """
    try:
        output_filename = f"{input_file.stem}.{output_format}"
        output_path = input_file.parent / output_filename

        with console.status(f"[bold yellow]Converting {input_file.name} to {output_format}...[/bold yellow]", spinner="dots"):
            success = convert_video_to_audio(str(input_file), str(output_path))
        
        if success:
            console.print(f"✅ [bold green]Success![/bold green] Audio saved to: [cyan]{output_path}[/cyan]")

    except FileNotFoundError as e:
        console.print(f"❌ [bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"❌ [bold red]An unexpected error occurred:[/bold red] {e}")
        raise typer.Exit(code=1)
import typer
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated
from . import main

app = typer.Typer()
console = Console()

@app.command(
    name="start",
    help="Starts recording audio from the default microphone for a specified duration."
)
def start_recording(
    # ... (Options remain the same)
    output: Annotated[
        str,
        typer.Option(
            "--output",
            "-o",
            help="Path to save the output WAV file.",
            show_default=False
        )
    ] = "recording.wav",
    duration: Annotated[
        int,
        typer.Option(
            "--duration",
            "-d",
            help="Duration of the recording in seconds.",
            min=1,
            max=3600
        )
    ] = 10,
    samplerate: Annotated[
        int,
        typer.Option(
            "--samplerate",
            "-s",
            help="Sample rate for the recording in Hz."
        )
    ] = 44100
):
    """
    Records audio and saves it to a specified file.
    """
    console.print(f"[cyan]Recording started. Output will be saved to '{output}'...[/cyan]")

    saved_path = main.record_audio(
        output_path=output,
        duration=duration,
        samplerate=samplerate
    )

    if saved_path:
        console.print(f"[green]✅ Audio successfully recorded and saved to:[/] [bold]{saved_path}[/bold]")
    else:
        console.print("[bold red]❌ Error: Failed to record audio. Please check logs.[/bold red]")
        console.print("[yellow]Hint: Try running 'poetry run python toolhub.py recorder devices' to check for available microphones.[/yellow]")
        raise typer.Exit(code=1)


@app.command(
    name="devices",
    help="Lists all available audio devices found on the system."
)
def list_devices():
    """
    Lists available audio input and output devices.
    """
    devices = main.list_audio_devices()
    if not devices:
        console.print("[bold red]No audio devices found on this system.[/bold red]")
        raise typer.Exit()

    table = Table(title="Available Audio Devices")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Device Name", style="magenta")
    table.add_column("Inputs", justify="center", style="green")
    table.add_column("Outputs", justify="center", style="yellow")
    table.add_column("Default Rate (Hz)", justify="right", style="blue")

    for device in devices:
        table.add_row(
            str(device["id"]),
            device["name"],
            str(device["max_input_channels"]),
            str(device["max_output_channels"]),
            f"{device['default_samplerate']:.0f}"
        )

    console.print(table)
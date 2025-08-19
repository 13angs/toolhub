# The "Cockpit" of the yt-transcript tool
# Defines the command-line interface using Typer.

import typer
from .main import get_transcript
from typing_extensions import Annotated

app = typer.Typer()

@app.command(name="fetch", help="Fetches the transcript of a YouTube video from its URL.")
def cli_get_transcript(
    video_url: str = typer.Argument(..., help="The full URL of the YouTube video."),
    output_file: Annotated[str, typer.Option("--output", "-o", help="Path to save the transcript as a .txt file. If not provided, prints to console.")] = None
):
    """
    A command-line tool to fetch and display the transcript of a YouTube video.
    """
    try:
        typer.echo("Fetching transcript...")
        transcript_text = get_transcript(video_url)
        
        if not transcript_text:
            typer.secho("Could not retrieve transcript. The video might have transcripts disabled.", fg=typer.colors.YELLOW)
            raise typer.Exit()

        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(transcript_text)
            typer.secho(f"Successfully saved transcript to: {output_file}", fg=typer.colors.GREEN)
        else:
            typer.echo("\n--- Transcript ---")
            typer.echo(transcript_text)
            typer.echo("--- End Transcript ---")

    except Exception as e:
        typer.secho(f"An error occurred: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
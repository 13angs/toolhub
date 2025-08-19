# The "Cockpit" of the yt-transcript tool
# Defines the command-line interface using Typer.

import typer
from .main import get_transcript

app = typer.Typer()

@app.command(name="yt-transcript", help="Fetches the transcript of a YouTube video from its URL.")
def cli_get_transcript(
    video_url: str = typer.Argument(..., help="The full URL of the YouTube video.")
):
    """
    A command-line tool to fetch and display the transcript of a YouTube video.
    """
    result = get_transcript(video_url)
    typer.echo(result)
# English: CLI interface for the YouTube downloader.
# Thai: ส่วนติดต่อผู้ใช้งาน (CLI) สำหรับเครื่องมือดาวน์โหลด YouTube
import typer
from typing_extensions import Annotated
from pathlib import Path
from .main import download_media

app = typer.Typer()

@app.command(name="save", help="Download a YouTube video as MP4 or MP3.")
def download(
    url: Annotated[str, typer.Argument(help="The full YouTube video URL.")],
    output_dir: Annotated[Path, typer.Option(
        "--output", "-o",
        help="The directory to save the file in. Defaults to the current directory.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        resolve_path=True,
    )] = Path.cwd(),
    audio_only: Annotated[bool, typer.Option(
        "--audio", "-a",
        help="Download as an audio-only MP3 file.",
        rich_help_panel="Output Format"
    )] = False
):
    """
    Downloads a video or audio from a given YouTube URL.
    """
    try:
        typer.echo(f"Starting download for URL: {url}")
        if audio_only:
            typer.echo("Mode: Audio only (MP3)")
        else:
            typer.echo("Mode: Video (MP4)")

        file_path = download_media(url, str(output_dir), audio_only)
        typer.secho(f"Successfully saved file to: {file_path}", fg=typer.colors.GREEN)

    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
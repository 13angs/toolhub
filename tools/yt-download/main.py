# English: Core logic for the YouTube downloader tool, now using yt-dlp.
# Thai: Logic หลักสำหรับเครื่องมือดาวน์โหลด YouTube, เปลี่ยนมาใช้ yt-dlp
import os
import yt_dlp
from typing import Optional

def download_media(
    url: str,
    output_path: Optional[str] = None,
    audio_only: bool = False
) -> str:
    """
    Downloads a video or audio from a YouTube URL using yt-dlp.

    Args:
        url (str): The YouTube video URL.
        output_path (Optional[str]): The directory to save the file.
                                     If None, it saves in the current directory.
        audio_only (bool): If True, downloads and converts to the best audio format (mp3).
                           Otherwise, downloads the best progressive mp4 video.

    Returns:
        str: The full path of the downloaded file.

    Raises:
        yt_dlp.utils.DownloadError: If there is an issue with the download.
    """
    save_path = output_path if output_path else os.getcwd()
    final_path_template = os.path.join(save_path, '%(title)s.%(ext)s')

    # This list will be used to capture the final filename from the hook
    final_filepath_capture = []

    def hook(d):
        """yt-dlp hook to capture the final filename after processing."""
        if d['status'] == 'finished':
            # After all post-processors are done, 'filename' is the final path
            final_filepath_capture.append(d.get('filename'))

    if audio_only:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': final_path_template,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', # Standard MP3 quality
            }],
            'progress_hooks': [hook],
            'quiet': True, # Suppress console output from yt-dlp itself
            'no_warnings': True,
        }
    else:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': final_path_template,
            'merge_output_format': 'mp4',
            'progress_hooks': [hook],
            'quiet': True,
            'no_warnings': True,
        }

    try:
        print("Initializing download with yt-dlp...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # yt-dlp handles fetching info and downloading
            ydl.download([url])

        if not final_filepath_capture:
             raise yt_dlp.utils.DownloadError("Could not determine the final file path.")

        final_path = final_filepath_capture[0]
        print(f"Download complete! File saved to: {final_path}")
        return final_path

    except yt_dlp.utils.DownloadError as e:
        print(f"A download error occurred: {e}")
        raise # Re-raise the exception to be caught by the CLI
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
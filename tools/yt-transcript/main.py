# The "Engine" of the yt-transcript tool
# Contains the core logic for fetching and formatting the transcript.

import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def _extract_video_id(video_url: str) -> str | None:
    """
    Extracts the YouTube video ID from a given URL.
    Supports standard, shortened, and embed URLs.
    """
    # Standard and shortened URLs (youtube.com/watch?v=... or youtu.be/...)
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", video_url)
    if match:
        return match.group(1)
    return None

def get_transcript(video_url: str) -> str:
    """
    Fetches the transcript for a given YouTube video URL.

    Args:
        video_url: The full URL of the YouTube video.

    Returns:
        A formatted string of the transcript or an error message.
    """
    video_id = _extract_video_id(video_url)
    if not video_id:
        return "Error: Could not extract a valid YouTube video ID from the URL."

    try:
        # Fetch the transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        # Format the transcript into a single string
        formatted_transcript = " ".join([item['text'] for item in transcript_list])
        return formatted_transcript

    except TranscriptsDisabled:
        return f"Error: Transcripts are disabled for this video (ID: {video_id})."
    except NoTranscriptFound:
        return f"Error: No transcript could be found for this video (ID: {video_id})."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
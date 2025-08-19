# The engine for the yt-transcript tool
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str) -> str:
    """
    Fetches the transcript for a given YouTube video ID.

    This function attempts to retrieve the transcript for the specified
    video ID, joins all transcript text parts into a single string,
    and returns it. It includes error handling for common issues like
    missing transcripts or invalid video IDs.

    Args:
        video_id: The ID of the YouTube video.

    Returns:
        A string containing the full transcript or an error message.
    """
    try:
        # The get_transcript method is a static method on the class.
        # This is the correct way to call it.
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id)
        
        # Join all the 'text' parts of the transcript segments
        full_transcript = " ".join([item.text for item in transcript_list])
        return full_transcript
    except Exception as e:
        # Provide a more informative error message to the user
        error_message = f"Could not retrieve transcript for video ID '{video_id}'. Reason: {e}"
        return error_message
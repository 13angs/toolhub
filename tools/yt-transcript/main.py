# The engine for the yt-transcript tool
from youtube_transcript_api import YouTubeTranscriptApi
from typing import List

def get_transcript(video_id: str, languages: List[str]) -> str:
    """
    Fetches the transcript for a given YouTube video ID.

    Args:
        video_id: The ID of the YouTube video.
        languages: A list of language codes to try, in order of preference.

    Returns:
        The formatted transcript as a single string.

    Raises:
        ValueError: If the transcript cannot be found or is disabled.
    """
    try:
        # The get_transcript method is a static method on the class.
        # This is the correct way to call it.
        ytt_api = YouTubeTranscriptApi()
        transcript_data = None

        if languages:

            transcript_list = ytt_api.list(video_id)
        
            # Manually find a transcript in the desired languages
            transcript = transcript_list.find_transcript(languages)

            # fetch() returns the transcript data
            transcript_data = transcript.fetch()
        else:
            # If no languages are specified, fetch the default transcript
            transcript_data = ytt_api.fetch(video_id)
        
        # Join all the 'text' parts of the transcript segments
        full_transcript = " ".join([item.text for item in transcript_data])
        return full_transcript
    except Exception as e:
        # Provide a more informative error message to the user
        error_message = f"Could not retrieve transcript for video ID '{video_id}'. Reason: {e}"
        return error_message
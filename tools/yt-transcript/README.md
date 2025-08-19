# YouTube Transcript Tool (`yt-transcript`)

This tool fetches and displays the full text transcript of a YouTube video given its URL.

## Description

The `yt-transcript` command connects to YouTube's transcript service to retrieve the available captions for a video and formats them into a single, readable text block. This is useful for quickly getting the content of a video without having to watch it.

## Usage

To use the tool, simply provide the full YouTube video URL as an argument.

```bash
poetry run python toolhub.py yt-transcript "YOUTUBE_VIDEO_URL"
```

## Example

```bash
# Command
poetry run python toolhub.py yt-transcript "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Expected Output (will be the full transcript of the video)
# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# ...
```

## Error Handling

The tool will provide specific error messages if:
- The URL is invalid.
- Transcripts are disabled for the video.
- No transcript can be found.
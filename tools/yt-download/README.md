# YouTube Downloader (`yt-download`)

This tool downloads a video or audio from a given YouTube URL.

---

## Command: `save`

Downloads the media file.

### Arguments

-   `URL` (Required): The full URL of the YouTube video you want to download.

### Options

-   `--output, -o DIRECTORY`: Specifies the directory where the downloaded file should be saved. If not provided, it will be saved in the current working directory.
-   `--audio, -a`: If this flag is present, the tool will download the audio track as an MP3 file instead of the full video.

---

## Usage Examples

### 1. Download a video (MP4)

This will download the video in the highest available resolution to your current directory.

```bash
poetry run python toolhub.py yt-download save "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### 2. Download audio only (MP3)

Using the `--audio` flag, you can extract and download just the audio.

```bash
poetry run python toolhub.py yt-download save "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --audio
```

### 3. Download to a specific directory

Use the `--output` option to specify a target folder.

```bash
# Downloads video to the 'my_videos' folder
poetry run python toolhub.py yt-download save "YOUTUBE_URL_HERE" --output ./my_videos/

# Downloads audio to the 'my_music' folder
poetry run python toolhub.py yt-download save "YOUTUBE_URL_HERE" --output ./my_music/ --audio
```
# YouTube Transcript Tool (`yt-transcript`)

This tool fetches and displays the full text transcript of a YouTube video given its Video ID.

---

## Description

The `yt-transcript` command connects to YouTube's transcript service to retrieve the available captions for a video and formats them into a single, readable text block. This is useful for quickly getting the content of a video without having to watch it.

## How to Use

The command requires a `fetch` subcommand followed by the Video ID as an argument.

### Basic Usage

To fetch a transcript and display it directly in your terminal, use the following command structure. By default, it will search for an English (`en`) transcript.

```bash
poetry run python toolhub.py yt-transcript fetch "VIDEO_ID"
```

**Example:**
```bash
# Command
poetry run python toolhub.py yt-transcript fetch "dQw4w9WgXcQ"

# Expected Output
# Fetching transcript for video ID 'dQw4w9WgXcQ' in languages ['en']...
# 
# --- Transcript ---
# We're no strangers to love You know the rules and so do I...
# --- End Transcript ---
```

### Specifying a Language

You can request a transcript in a specific language, or provide a prioritized list of languages, using the `--language` (or `-l`) option. The tool will try the languages in the order you provide them.

```bash
poetry run python toolhub.py yt-transcript fetch "VIDEO_ID" --language de --language en
```

**Example (Trying German first, then English):**
```bash
# This video has a German transcript
poetry run python toolhub.py yt-transcript fetch "W8yG-a21f7w" -l de -l en
```

### Saving to a File

You can save the transcript directly to a `.txt` file by using the `--output` (or `-o`) option. This works with all language options.

```bash
poetry run python toolhub.py yt-transcript fetch "VIDEO_ID" --language fr --output [FILENAME].txt
```

**Example:**
```bash
poetry run python toolhub.py yt-transcript fetch "dQw4w9WgXcQ" -o rick_astley_lyrics.txt
```
This will create a file named `rick_astley_lyrics.txt` in your current directory containing the video's transcript.

## Arguments and Options

-   **`VIDEO_ID`** (Argument, Required): The unique identifier of the YouTube video (the part after `v=` in the URL).
-   **`--language, -l`** (Option, Optional): A preferred language code (e.g., `en`, `de`, `fr`). You can provide this option multiple times to create a priority list (e.g., `-l de -l en`).
-   **`--output, -o`** (Option, Optional): The file path where the transcript should be saved. If this option is not provided, the transcript will be printed to the terminal.
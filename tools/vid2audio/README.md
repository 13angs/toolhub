# vid2audio Tool

This tool extracts the audio track from a video file and saves it as a separate audio file.

---

## Commands

### `convert`

This is the primary command for performing the conversion.

- **ARGUMENTS:**
  - `INPUT_FILE`: (Required) The path to the source video file.

- **OPTIONS:**
  - `--format` / `-f`: The desired audio format (e.g., `mp3`, `wav`, `aac`). Defaults to `mp3`.

---

## Usage Examples

### 1. Basic Conversion (to MP3)

This will convert `my-cool-video.mp4` and save the audio as `my-cool-video.mp3` in the same directory.

```bash
poetry run python toolhub.py vid2audio convert /path/to/your/my-cool-video.mp4
```

### 2. Specifying an Output Format (to WAV)

This example converts a `.mov` file and saves the audio as a `.wav` file.

```bash
poetry run python toolhub.py vid2audio convert /path/to/another-video.mov --format wav
```

### 3. Getting Help

To see all available options and arguments for this tool, you can use the `--help` flag.

```bash
poetry run python toolhub.py vid2audio convert --help
```
# Tool: Audio Recorder (`recorder`)

This tool allows you to record audio from your system's default microphone and save it as a WAV file.

---

## Command: `start`

This is the primary command to begin a recording session.

### Usage

```bash
poetry run python toolhub.py recorder start [OPTIONS]
```

### Options

-   `--output` / `-o`: **(Optional)** The path and filename for the saved audio file.
    -   **Type:** `string`
    -   **Default:** `recording.wav`
-   `--duration` / `-d`: **(Optional)** The duration of the recording in seconds.
    -   **Type:** `integer`
    -   **Default:** `10`
-   `--samplerate` / `-s`: **(Optional)** The sample rate in Hz. This determines the quality of the audio.
    -   **Type:** `integer`
    -   **Default:** `44100`

---

### Examples

1.  **Basic Recording (10 seconds)**
    This command will record 10 seconds of audio and save it to the default file `recording.wav`.

    ```bash
    poetry run python toolhub.py recorder start
    ```

2.  **Record for 30 seconds to a custom file**
    This command records for 30 seconds and saves the output to `my_meeting_notes.wav`.

    ```bash
    poetry run python toolhub.py recorder start --output my_meeting_notes.wav --duration 30
    ```

### Important Notes

-   **Microphone Access:** The first time you run this tool, your operating system may ask for permission to allow the application to access your microphone. Please grant this permission.
-   **File Format:** This tool currently only supports saving in `.wav` format.

#### **`README.md` (อัปเดตไฟล์หลัก)**

ผมจะเพิ่มเครื่องมือ `recorder` เข้าไปในส่วน "Available Tools" และอัปเดตโครงสร้างโปรเจกต์
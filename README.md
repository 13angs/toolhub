# ToolHub CLI

A collection of useful command-line tools, built with Python and Typer.

---

## **Project strucure:**

```
├── tools/
│   ├── recorder/
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── main.py
│   │   └── README.md
│   └── vid2audio/
│       ├── __init__.py
│       ├── cli.py
│       ├── main.py
│       └── README.md
├── pyproject.toml
├── toolhub.py
└── README.md
```

---

## 🚀 Getting Started (Manual Setup)

This guide is for setting up the project on your local machine.

### 1. Prerequisites

Before you begin, ensure you have the following software installed on your system.

- **Python 3.10 or newer**
- **Poetry** for dependency management.
- **FFmpeg** for video/audio processing.

*(For detailed installation steps for these prerequisites, please see the original `README.md` content in the previous conversation.)*

### 2. Project Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd toolhub-cli
    ```

2.  **Install Python dependencies:**
    ```bash
    poetry install
    ```

### 3. General Usage

All commands follow this basic structure. To ensure you are using the correct Python environment, **always** prefix your commands with `poetry run`.

```bash
poetry run python toolhub.py <TOOL_NAME> <COMMAND> [ARGUMENTS] [OPTIONS]
```

---

## 🛠️ Available Tools

Below is a list of the available tools. Click on a tool's name for detailed documentation and usage examples.

- **[vid2audio](./tools/vid2audio/README.md):** A tool to extract audio from video files.
- **[recorder](./tools/recorder/README.md):** A tool to record audio from your microphone.
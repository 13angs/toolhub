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
├── .dockerignore
├── Dockerfile.alpine
├── Dockerfile.debian
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

## 🐳 Docker Usage

This project can be built into a Docker image for easy and consistent execution across different environments. We provide Dockerfiles for two popular Linux distributions.

### Choosing an Image
-   **Debian (`Dockerfile.debian`):** Recommended for general use. It offers great compatibility with a wide range of software.
-   **Alpine (`Dockerfile.alpine`):** Recommended for production or when the smallest possible image size is a priority.

### 1. Building the Image

Open your terminal at the root of the project and use one of the following commands. The `-f` flag specifies which Dockerfile to use, and the `-t` flag tags the image with a memorable name.

**To build the Debian-based image:**
```bash
docker build -f Dockerfile.debian -t toolhub:debian .
```

**To build the Alpine-based image:**
```bash
docker build -f Dockerfile.alpine -t toolhub:alpine .
```

### 2. Running Commands

Once the image is built, you can run any tool by passing commands to `docker run`. The key is to mount your current working directory into the container's `/app/data` directory to allow file access.

**General Syntax:**

```bash
# For Debian
docker run --rm -v "$(pwd):/app/data" toolhub:debian <TOOL_NAME> [COMMANDS_AND_OPTIONS]

# For Alpine
docker run --rm -v "$(pwd):/app/data" toolhub:alpine <TOOL_NAME> [COMMANDS_AND_OPTIONS]
```

**Example: Extracting audio using the `debian` image**

Assume you have a file named `my_video.mp4` in your current directory.

```bash
docker run --rm -v "$(pwd):/app/data" toolhub:debian vid2audio convert /app/data/my_video.mp4
```
This command will create an `audio.mp3` file in the same directory on your host machine.

---

## 🛠️ Available Tools

Below is a list of the available tools. Click on a tool's name for detailed documentation and usage examples.

- **[vid2audio](./tools/vid2audio/README.md):** A tool to convert audio from video files.
- **[recorder](./tools/recorder/README.md):** A tool to record audio from your microphone.
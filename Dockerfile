# --- STAGE 1: Build Stage ---
FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.2

# Set the working directory
WORKDIR /app

# Install system dependencies
# ADDED: Audio libraries needed for the 'recorder' tool (sounddevice package)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    libportaudio2 \
    portaudio19-dev \
    libasound2-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install "poetry==${POETRY_VERSION}"

# Copy only the dependency definition files
COPY pyproject.toml poetry.lock* ./

# Disable virtual environment creation by Poetry.
RUN poetry config virtualenvs.create false

# Install project dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application source code
COPY . .


# --- STAGE 2: Final Stage ---
FROM python:3.11-slim AS final

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install only the necessary system dependencies
# ADDED: Audio runtime libraries needed for the 'recorder' tool
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    libportaudio2 \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy the application code from the builder stage
COPY --from=builder /app /app

# Create a non-root user for security reasons
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

# Define the entrypoint for the container.
ENTRYPOINT ["python", "toolhub.py"]

# Set the default command to run if no command is specified.
CMD ["--help"]
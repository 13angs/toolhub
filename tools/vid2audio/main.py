import ffmpeg
import os

def convert_video_to_audio(input_path: str, output_path: str) -> bool:
    """
    Converts a video file to an audio file using ffmpeg.

    This function contains the core logic for the conversion. It is designed
    to be stateless and testable, receiving input and output paths and
    returning a status.

    Args:
        input_path (str): The full path to the source video file.
        output_path (str): The full path for the destination audio file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ffmpeg.Error: If ffmpeg encounters an error during conversion.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, acodec='libmp3lame' if output_path.endswith('.mp3') else None)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return True
    except ffmpeg.Error as e:
        # The ffmpeg.Error exception often contains detailed stderr output
        # which is useful for debugging. We re-raise it to be handled by the CLI layer.
        print(f"ffmpeg error:\n{e.stderr.decode()}")
        raise e
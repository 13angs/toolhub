import sounddevice as sd
import soundfile as sf
from typing import Optional, Dict, Any, List
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_audio_devices() -> List[Dict[str, Any]]:
    """
    Queries and returns a list of available audio devices.
    """
    try:
        devices = sd.query_devices()
        device_list = []
        if isinstance(devices, dict): # Handle case where only one device is returned
            devices = [devices]
        for i, device in enumerate(devices):
            device_info = {
                "id": i,
                "name": device.get('name', 'N/A'),
                "hostapi": device.get('hostapi', 'N/A'),
                "max_input_channels": device.get('max_input_channels', 0),
                "max_output_channels": device.get('max_output_channels', 0),
                "default_samplerate": device.get('default_samplerate', 0.0),
            }
            device_list.append(device_info)
        return device_list
    except Exception as e:
        logging.error(f"Could not retrieve audio devices: {e}")
        return []

def record_audio(
    output_path: str,
    duration: int,
    samplerate: int = 44100
) -> Optional[str]:
    """
    Records audio from the default input device and saves it to a file.
    (Functionality remains the same)
    """
    try:
        # Check if any input device exists before recording
        if sd.query_devices(kind='input') is None:
            raise sd.PortAudioError("No input device found.")

        if not output_path.lower().endswith('.wav'):
            logging.warning("Output file does not end with .wav. Appending it.")
            output_path += ".wav"

        logging.info(f"Preparing to record for {duration} seconds. Speak into your microphone...")

        # Record audio
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='float64')
        sd.wait()  # Wait until recording is finished

        # Save as a file
        sf.write(output_path, recording, samplerate)
        logging.info(f"Recording finished.")

        return output_path
    except Exception as e:
        logging.error(f"An error occurred during recording: {e}")
        return None
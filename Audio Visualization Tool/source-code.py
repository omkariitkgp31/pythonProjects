"""
Real-time audio waveform visualization using PyAudio and Matplotlib.

This script captures audio from the microphone, processes it into integers,
and displays the waveform dynamically.

To install PyAudio, run:
    pip install pyaudio
"""

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

# Constants
CHUNK = 1024 * 2         # Number of audio samples per frame
FORMAT = pyaudio.paInt16 # Audio format (16-bit)
CHANNELS = 1             # Mono input
RATE = 44100             # Sampling rate (Hz)

# Initialize PyAudio
audio_interface = pyaudio.PyAudio()

# List available input devices
print("Available audio input devices:")
host_info = audio_interface.get_host_api_info_by_index(0)
device_count = host_info.get('deviceCount')

for i in range(device_count):
    device_info = audio_interface.get_device_info_by_host_api_device_index(0, i)
    if device_info.get('maxInputChannels') > 0:
        print(f"Input Device ID {i} - {device_info.get('name')}")

# Prompt user to select a device
device_id = input("\nEnter Device ID to use as input: ")

# Open audio stream
stream = audio_interface.open(
    input_device_index=int(device_id),
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

# Setup Matplotlib plot
x = np.arange(0, 2 * CHUNK, 2)
fig, ax = plt.subplots(figsize=(15, 7))
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)
ax.set_title("Live Audio Waveform")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")
ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])
plt.show(block=False)

print("Audio stream started...")

# Frame rate measurement
frame_count = 0
start_time = time.time()

try:
    while True:
        # Read audio data from stream
        data = stream.read(CHUNK, exception_on_overflow=False)

        # Convert binary data to integers
        data_unpacked = struct.unpack(str(2 * CHUNK) + 'B', data)
        data_array = np.array(data_unpacked, dtype='b')[::2] + 128

        # Update plot data
        line.set_ydata(data_array)
        fig.canvas.draw()
        fig.canvas.flush_events()

        frame_count += 1

except TclError:
    # Calculate average frame rate
    elapsed_time = time.time() - start_time
    avg_frame_rate = frame_count / elapsed_time
    print("\nStream stopped.")
    print(f"Average frame rate: {avg_frame_rate:.0f} FPS")

finally:
    # Cleanup
    stream.stop_stream()
    stream.close()
    audio_interface.terminate()

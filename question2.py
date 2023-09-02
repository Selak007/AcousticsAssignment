import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 33  # Frequency in Hz
duration = 1    # Duration in seconds
sampling_rate = 1000  # Sampling rate in samples per second

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration))

# Function to generate a sawtooth wave
def sawtooth_wave(frequency, t):
    T = 1 / frequency
    return 2 * (t / T - np.floor(0.5 + t / T))

# Function to generate a square wave
def square_wave(frequency, t):
    T = 1 / frequency
    return 2 * (t / T - np.floor(0.5 + t / T)) > 0

# Function to generate a triangular wave
def triangular_wave(frequency, t):
    T = 1 / frequency
    return 2 * np.abs(2 * (t / T - np.floor(0.5 + t / T)) - 1) - 1

# Generate the three waves
sawtooth = sawtooth_wave(frequency, t)
square = square_wave(frequency, t)
triangular = triangular_wave(frequency, t)

# Plot the waves
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, sawtooth)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sawtooth Wave - Frequency 33 Hz')

plt.subplot(3, 1, 2)
plt.plot(t, square)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Square Wave - Frequency 33 Hz')

plt.subplot(3, 1, 3)
plt.plot(t, triangular)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Triangular Wave - Frequency 33 Hz')

plt.tight_layout()
plt.show()

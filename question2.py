import numpy as np
import matplotlib.pyplot as plt

f = 33.0  # Fundamental frequency (Hz)
A = 1.0   # Amplitude of the fundamental frequency
n_max = 50 # Maximum number of overtones
T = 1.0   # Time duration in seconds
def sawtooth_wave(t):
    wave = 0.0
    for n in range(1, n_max + 1):
        wave += (A / n) * np.sin(2 * np.pi * n * f * t)
    return wave
def square_wave(t):
    wave = 0.0
    for n in range(1, n_max + 1):
        if n % 2 == 1:  # Odd harmonics
            wave += (A / n) * np.sin(2 * np.pi * n * f * t)
    return wave
def triangular_wave(t):
    wave = 0.0
    for n in range(1, n_max + 1):
        if n % 2 == 1:  # Odd harmonics
            wave += (A / (n**2)) * np.cos(2 * np.pi * n * f * t)
    return wave
# Generate time values
t = np.linspace(0, T, int(1000 * T))  # High-resolution time values for plotting

# Generate the waveforms
sawtooth = sawtooth_wave(t)
square = square_wave(t)
triangular = triangular_wave(t)

# Plot the waveforms
plt.figure(figsize=(12, 6))

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

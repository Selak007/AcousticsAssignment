import numpy as np
import matplotlib.pyplot as plt

# Parameters for the input waves
fundamental_freq = 33  # Fundamental frequency in Hz (e.g., A4)
overtone_freqs = [fundamental_freq * 2, fundamental_freq * 3]  # Frequencies of overtones
sampling_rate = 1000  # Sampling rate in samples per second (typical for audio)
duration = 1.0  # Duration of the signal in seconds

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration))

# Generate input sine waves
fundamental_amplitude = 1.0
fundamental_phase = 0.0
fundamental_wave = fundamental_amplitude * np.sin(2 * np.pi * fundamental_freq * t + fundamental_phase)

overtone_amplitudes = [0.6, 0.3]  # Vary the amplitudes as needed
overtone_phases = [np.pi / 4, np.pi / 2]  # Vary the phases as needed
overtone_waves = []

for i, overtone_freq in enumerate(overtone_freqs):
    overtone_amplitude = overtone_amplitudes[i]
    overtone_phase = overtone_phases[i]
    overtone_wave = overtone_amplitude * np.sin(2 * np.pi * overtone_freq * t + overtone_phase)
    overtone_waves.append(overtone_wave)

# Combine all waves into the composite signal
composite_signal = fundamental_wave + sum(overtone_waves)

# Plot the individual waves and the composite signal
plt.figure(figsize=(12, 6))

# Plot the fundamental wave
plt.subplot(4, 1, 1)
plt.plot(t, fundamental_wave, label=f'Fundamental ({fundamental_freq} Hz)')
plt.ylabel('Amplitude')
plt.title('Input Sine Waves and Composite Signal')
plt.legend()

# Plot the overtone waves
for i, overtone_wave in enumerate(overtone_waves):
    plt.subplot(4, 1, i + 2)
    plt.plot(t, overtone_wave, label=f'Overtone {i + 1} ({overtone_freqs[i]} Hz)')
    plt.ylabel('Amplitude')
    plt.legend()

# Plot the composite signal
plt.subplot(4, 1, 4)
plt.plot(t, composite_signal, color='red', label='Composite Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()

# Report the input frequencies and phases
print(f'Input Frequencies: Fundamental = {fundamental_freq} Hz, Overtones = {overtone_freqs} Hz')
print(f'Input Phases: Fundamental = {fundamental_phase} radians, Overtones = {overtone_phases} radians')

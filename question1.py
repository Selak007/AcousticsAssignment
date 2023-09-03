import numpy as np
import matplotlib.pyplot as plt

# Parameters for the input waves
fun_freq = 33  # Fundamental frequency in Hz (e.g., A4)
ov_freqs = [fun_freq * 2, fun_freq * 3]  # Frequencies of ovs
waveform_rate = 1000  # Number of Waveform samples requried to create a discrete digital signal
duration = 1.0  # Duration of the signal in seconds

# Generate time values
t = np.linspace(0, duration, int(waveform_rate * duration))

# Generate input sine waves
fun_amplitude = 1.0
fun_phase = 0.0
fun_wave = fun_amplitude * np.sin(2 * np.pi * fun_freq * t + fun_phase)

ov_amplitudes = [0.5, 0.3]  # Vary the amplitudes as needed
ov_phases = [np.pi , np.pi / 2]  # Vary the phases as needed
ov_waves = []

for i, ov_freq in enumerate(ov_freqs):
    ov_amplitude = ov_amplitudes[i]
    ov_phase = ov_phases[i]
    ov_wave = ov_amplitude * np.sin(2 * np.pi * ov_freq * t + ov_phase)
    ov_waves.append(ov_wave)

# Combine all waves into the composite signal
composite_signal = fun_wave + sum(ov_waves)

# Plot the individual waves and the composite signal
plt.figure(figsize=(12, 6))

# Plot the fun wave
plt.subplot(4, 1, 1)
plt.plot(t, fun_wave, label=f'Fundamental ({fun_freq} Hz)')
plt.ylabel('Amplitude')
plt.title('Input Sine Waves and Composite Signal')
plt.legend()

# Plot the ov waves
for i, ov_wave in enumerate(ov_waves):
    plt.subplot(4, 1, i + 2)
    plt.plot(t, ov_wave, label=f'Overtone {i + 1} ({ov_freqs[i]} Hz)')
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
print(f'Input Frequencies: Fundamental = {fun_freq} Hz, Overtones = {ov_freqs} Hz')
print(f'Input Phases: Fundamental = {fun_phase} radians, Overtones = {ov_phases} radians')

# Report the input frequencies and phases
print(f'Input Frequencies: Fundamental = {fun_freq} Hz, Overtones = {ov_freqs} Hz')
print(f'Input Phases: Fundamental = {fun_phase} radians, Overtones = {ov_phases} radians')

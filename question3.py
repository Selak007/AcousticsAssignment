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
signal = fun_wave + sum(ov_waves)
# Compute the Fourier transform
fourier_transform = np.fft.fft(signal)

# Calculate the frequency axis for plotting
frequencies = np.fft.fftfreq(len(signal), 1/waveform_rate)
positive_frequencies = frequencies[:len(signal)//2]
magnitude_spectrum = np.abs(fourier_transform[:len(signal)//2])

# Plot the time-domain signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time Domain')

# Plot the frequency-domain signal
plt.subplot(2, 1, 2)
plt.plot(positive_frequencies, magnitude_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Domain')

# Adjust plot window
plt.xlim([0, waveform_rate/2])

# Show both plots
plt.tight_layout()
plt.show()

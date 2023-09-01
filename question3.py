import numpy as np
import matplotlib.pyplot as plt

# Sample data
Fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/Fs)  # Time vector
f1 = 50  # Frequency of the first sine wave (Hz)
f2 = 150  # Frequency of the second sine wave (Hz)
signal = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# Compute the Fourier transform
N = len(signal)
freq = np.fft.fftshift(np.fft.fftfreq(N, 1/Fs))  # Frequency axis
fourier_transform = np.fft.fftshift(np.fft.fft(signal))

# Plot the magnitude of the Fourier transform
plt.plot(freq, np.abs(fourier_transform))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude of Fourier Transform')
plt.grid()
plt.show()

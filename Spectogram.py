import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

Fs = 1000.0
t = np.arange(0, 2, 1/Fs)
f_c, f_m, beta = 100.0, 10.0, 5.0

# Sygnały AM i FM
x_am = (1.0 + 0.5 * np.cos(2 * np.pi * f_m * t)) * np.cos(2 * np.pi * f_c * t)
x_fm = np.cos(2 * np.pi * f_c * t + beta * np.sin(2 * np.pi * f_m * t))

L, Nfft, R = 128, 256, 32
w = np.hamming(L)

# Obliczenia spektrogramów za pomocą funkcji z biblioteki
_, t_am, S_am = spectrogram(x_am, fs=Fs, window=w, nperseg=L, noverlap=L-R, nfft=Nfft)
_, t_fm, S_fm = spectrogram(x_fm, fs=Fs, window=w, nperseg=L, noverlap=L-R, nfft=Nfft)

# Dwa subploty: AM i FM
fig, axes = plt.subplots(2, 1, figsize=(9, 6))

axes[0].imshow(20 * np.log10(S_am + 1e-6), aspect='auto', origin='lower', extent=[t_am[0], t_am[-1], 0, Fs/2])
axes[0].set_title('Spektrogram - Sygnał AM')
axes[0].set_ylabel('Częstotliwość [Hz]')

axes[1].imshow(20 * np.log10(S_fm + 1e-6), aspect='auto', origin='lower', extent=[t_fm[0], t_fm[-1], 0, Fs/2])
axes[1].set_title('Spektrogram - Sygnał FM')
axes[1].set_xlabel('Czas [s]')
axes[1].set_ylabel('Częstotliwość [Hz]')

plt.tight_layout()
plt.show()
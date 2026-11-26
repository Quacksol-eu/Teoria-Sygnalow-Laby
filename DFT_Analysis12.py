import numpy as np
import matplotlib.pyplot as plt

Fs = 100.0
F = 20.0
DC = 1.0
A = 1.0
varphi = np.pi / 5

fig, axes = plt.subplots(3, 1, figsize=(8, 12))

# 1. N = 64 bez i z paddingiem do 1024
N1 = 64
n1 = np.arange(N1)
x1 = A * np.cos(2 * np.pi * (F / Fs) * n1 + varphi) + DC

X1 = np.fft.fft(x1)
freqs1 = np.fft.fftfreq(N1, d=1/Fs)
mag1 = np.abs(X1) / N1
mag1[1:] *= 2
mask1 = freqs1 >= 0
axes[0].plot(freqs1[mask1], mag1[mask1], 'o-', label='N = 64', alpha=0.7)

X2 = np.fft.fft(x1, n=1024)
freqs2 = np.fft.fftfreq(1024, d=1/Fs)
mag2 = np.abs(X2) / N1
mag2[1:] *= 2
mask2 = freqs2 >= 0
axes[0].plot(freqs2[mask2], mag2[mask2], '-', label='N = 64 z paddingiem (1024)', color='tab:orange')

axes[0].set_title('N = 64: Bez paddingu vs Z paddingiem')
axes[0].set_xlabel('Częstotliwość [Hz]')
axes[0].set_ylabel('Amplituda')
axes[0].grid(True, linestyle=':', alpha=0.7)
axes[0].legend()
axes[0].set_xlim(0, Fs / 2)

# 2. N = 32 bez paddingu
N_32 = 32
n_32 = np.arange(N_32)
x_32 = A * np.cos(2 * np.pi * (F / Fs) * n_32 + varphi) + DC
X_32 = np.fft.fft(x_32)
freqs_32 = np.fft.fftfreq(N_32, d=1/Fs)
mag_32 = np.abs(X_32) / N_32
mag_32[1:] *= 2
mask_32 = freqs_32 >= 0

axes[1].stem(freqs_32[mask_32], mag_32[mask_32], label='N = 32')
axes[1].set_title('N = 32 (bez paddingu)')
axes[1].set_xlabel('Częstotliwość [Hz]')
axes[1].set_ylabel('Amplituda')
axes[1].grid(True, linestyle=':', alpha=0.7)
axes[1].legend()
axes[1].set_xlim(0, Fs / 2)

# 3. N = 64 bez paddingu
axes[2].stem(freqs1[mask1], mag1[mask1], label='N = 64', linefmt='g-', markerfmt='go')
axes[2].set_title('N = 64 (bez paddingu)')
axes[2].set_xlabel('Częstotliwość [Hz]')
axes[2].set_ylabel('Amplituda')
axes[2].grid(True, linestyle=':', alpha=0.7)
axes[2].legend()
axes[2].set_xlim(0, Fs / 2)

plt.tight_layout()
plt.show()
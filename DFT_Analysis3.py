import numpy as np
import matplotlib.pyplot as plt

# Parametry sygnału (7.5)
Fs = 100.0
F = 20.0
DC = 1.0
A = 1.0
varphi = np.pi / 5
N = 64
N_padded = 1024

# Generowanie sygnału
n = np.arange(N)
x = A * np.cos(2 * np.pi * (F / Fs) * n + varphi) + DC

w_rect = np.ones(N)
w_hamm = np.hamming(N)

X_rect = np.fft.fft(x * w_rect, n=N_padded)
X_hamm = np.fft.fft(x * w_hamm, n=N_padded)

freqs = np.fft.fftfreq(N_padded, d=1/Fs)
mask = freqs >= 0


def scale_spectrum(X, w):
    coherent_gain = np.sum(w)
    mag = np.abs(X) / coherent_gain
    mag[freqs > 0] *= 2  
    return mag

mag_rect = scale_spectrum(X_rect, w_rect)
mag_hamm = scale_spectrum(X_hamm, w_hamm)

# Rysowanie wykresu
plt.figure(figsize=(9, 5))
plt.plot(freqs[mask], mag_rect[mask], label='Okno prostokątne', alpha=0.8, linewidth=1.5)
plt.plot(freqs[mask], mag_hamm[mask], label='Okno Hamminga', alpha=0.8, linewidth=1.5)

plt.title('Porównanie widm: Okno prostokątne vs Hamminga (N=64, zero-padding do 1024)')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.xlim(0, Fs / 2)
plt.tight_layout()
plt.show()
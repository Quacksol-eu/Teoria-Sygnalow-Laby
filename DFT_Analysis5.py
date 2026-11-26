import numpy as np
import matplotlib.pyplot as plt

# Parametry
Fs = 100.0
F1 = 20.0
F2 = 24.0
A1 = 1.0
varphi1 = 0.0
varphi2 = 0.0
N = 256
N_padded = 1024

A2_values = [1.0, 0.5, 0.2]

fig, axes = plt.subplots(len(A2_values), 1, figsize=(8, 11))

for ax, A2 in zip(axes, A2_values):
    n = np.arange(N)
    x = A1 * np.cos(2 * np.pi * (F1 / Fs) * n + varphi1) + A2 * np.cos(2 * np.pi * (F2 / Fs) * n + varphi2)
    
    X = np.fft.fft(x, n=N_padded)
    freqs = np.fft.fftfreq(N_padded, d=1/Fs)
    
    mag = np.abs(X) / N
    mag[freqs > 0] *= 2
    
    mask = freqs >= 0
    ax.plot(freqs[mask], mag[mask], linewidth=1.5, color='tab:orange')
    ax.set_title(f'A1 = {A1}, A2 = {A2} (F1 = {F1} Hz, F2 = {F2} Hz)')
    ax.set_xlabel('Częstotliwość [Hz]')
    ax.set_ylabel('Amplituda')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xlim(0, Fs / 2)

plt.tight_layout()
plt.show()
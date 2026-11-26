import numpy as np
import matplotlib.pyplot as plt

# Parametry
Fs = 100.0
F1 = 20.0
A1 = 1.0
A2 = 1.0
varphi1 = 0.0
varphi2 = 0.0
N = 256
N_padded = 1024

# Wybrane wartości F2 z przedziału (20, 40) Hz
F2_values = [22.0, 26.0, 35.0]

fig, axes = plt.subplots(len(F2_values), 1, figsize=(8, 11))

for ax, F2 in zip(axes, F2_values):
    n = np.arange(N)
    # Sygnał złożony z dwóch kosinusów (7.6)
    x = A1 * np.cos(2 * np.pi * (F1 / Fs) * n + varphi1) + A2 * np.cos(2 * np.pi * (F2 / Fs) * n + varphi2)
    
    # DFT z zero-paddingiem do 1024
    X = np.fft.fft(x, n=N_padded)
    freqs = np.fft.fftfreq(N_padded, d=1/Fs)
    
    # Skalowanie amplitudy
    mag = np.abs(X) / N
    mag[freqs > 0] *= 2
    
    mask = freqs >= 0
    ax.plot(freqs[mask], mag[mask], linewidth=1.5, color='tab:blue')
    ax.set_title(f'F1 = {F1} Hz, F2 = {F2} Hz (N = {N}, padding = {N_padded})')
    ax.set_xlabel('Częstotliwość [Hz]')
    ax.set_ylabel('Amplituda')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xlim(0, Fs / 2)

plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Parametry
Fs = 100.0
F1 = 20.0
F2 = 22.0
A1 = 1.0
A2 = 1.0
varphi1 = 0.0
varphi2 = 0.0
N_target = 2048  

N_values = [256, 512, 1024, 2048]

fig, axes = plt.subplots(len(N_values), 1, figsize=(8, 12))

for ax, N in zip(axes, N_values):
    n = np.arange(N)
    x = A1 * np.cos(2 * np.pi * (F1 / Fs) * n + varphi1) + A2 * np.cos(2 * np.pi * (F2 / Fs) * n + varphi2)
    
    X = np.fft.fft(x, n=N_target)
    freqs = np.fft.fftfreq(N_target, d=1/Fs)
    
    mag = np.abs(X) / N
    mag[freqs > 0] *= 2
    
    mask = freqs >= 0
    ax.plot(freqs[mask], mag[mask], linewidth=1.5, color='tab:purple')
    ax.set_title(f'N = {N} (zero-padding do {N_target}) | F1 = {F1} Hz, F2 = {F2} Hz')
    ax.set_xlabel('Częstotliwość [Hz]')
    ax.set_ylabel('Amplituda')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xlim(0, Fs / 2)

plt.tight_layout()
plt.show()
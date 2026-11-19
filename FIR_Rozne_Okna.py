import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 4000.0
fc = 1000.0
M = 51

omega_c = 2 * np.pi * (fc / Fs)

n = np.arange(M)
m = n - (M - 1) / 2.0
h_ideal = np.where(m == 0, omega_c / np.pi, np.sin(omega_c * m) / (np.pi * m))

windows = {
    'Prostokątne': np.ones(M),
    'Hamminga': signal.windows.hamming(M),
    'Hanna': signal.windows.hann(M),
    'Blackmana': signal.windows.blackman(M)
}



fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for ax, (name, w_func) in zip(axes.flat, windows.items()):
    h = h_ideal * w_func
    w, h_freq = signal.freqz(h, a=1.0, worN=1024)
    f = (w / np.pi) * (Fs / 2)
    mag_db = 20 * np.log10(np.abs(h_freq) + 1e-12)
    
    ax.plot(f, mag_db, color='tab:blue', linewidth=1.5, label=name)
    ax.set_title(f'Okno: {name}')
    ax.set_xlabel('Częstotliwość [Hz]')
    ax.set_ylabel('Amplituda [dB]')
    ax.axvline(fc, color='gray', linestyle='--', alpha=0.7, label=f'fc = {fc} Hz')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.legend(loc='upper right')
    ax.set_ylim([-90, 5])

plt.tight_layout()
plt.show()
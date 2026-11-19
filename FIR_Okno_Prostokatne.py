import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 4000.0
fc = 1000.0
M_values = [11, 51, 101]

omega_c = 2 * np.pi * (fc / Fs)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for M in M_values:
    n = np.arange(M)
    m = n - (M - 1) / 2.0
    h = np.where(m == 0, omega_c / np.pi, np.sin(omega_c * m) / (np.pi * m))
    
    w, h_freq = signal.freqz(h, a=1.0, worN=1024)
    f = (w / np.pi) * (Fs / 2)
    mag_db = 20 * np.log10(np.abs(h_freq) + 1e-12)
    
    # Rysowanie na wszystkich 4 podwykresach
    for ax in axes.flat:
        ax.plot(f, mag_db, label=f'M = {M}')

# 1. Pełny zakres
axes[0, 0].set_title('Pełna charakterystyka')
axes[0, 0].set_xlim(0, Fs/2)
axes[0, 0].set_ylim(-60, 5)

# 2. Zoom: przed cutoff (pasmo przepustowe)
axes[0, 1].set_title('Zoom: przed cuttof')
axes[0, 1].set_xlim(0, fc - 100)
axes[0, 1].set_ylim(-5, 1)

# 3. Zoom: blisko cutoff
axes[1, 0].set_title('Zoom: w okolicach cuttof')
axes[1, 0].set_xlim(fc - 300, fc + 300)
axes[1, 0].set_ylim(-40, 5)

# 4. Zoom: po cutoff (pasmo zaporowe)
axes[1, 1].set_title('Zoom: po cuttof')
axes[1, 1].set_xlim(fc + 100, Fs/2)
axes[1, 1].set_ylim(-60, 0)

for ax in axes.flat:
    ax.set_xlabel('Częstotliwość [Hz]')
    ax.set_ylabel('Amplituda [dB]')
    ax.axvline(fc, color='gray', linestyle='--', alpha=0.7)
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.legend(loc='upper right')

plt.tight_layout()
plt.show()
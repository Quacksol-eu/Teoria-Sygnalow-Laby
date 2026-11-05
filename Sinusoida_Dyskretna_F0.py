import numpy as np
import matplotlib.pyplot as plt

A = 1.0
phi = 0.0
Fs = 8000.0  # Częstotliwość próbkowania (Hz)
n = np.arange(0, 40)

# Różne wartości częstotliwości F0 spełniające warunek F0 < Fs / 2 (poniżej częstotliwości Nyquista 4000 Hz)
F0_values = [
    500.0,
    1000.0,
    1500.0,
    2000.0,
    2500.0,
    3000.0,
    3500.0,
    3900.0
]

fig, axes = plt.subplots(4, 2, figsize=(14, 16))
axes = axes.flatten()

for i, F0 in enumerate(F0_values):
    x = A * np.cos(2 * np.pi * (F0 / Fs) * n + phi)
    
    axes[i].plot(n, x, 'b-o', markersize=4)
    axes[i].set_title(f'F₀ = {F0} Hz (F_s = {Fs} Hz)')
    axes[i].set_xlabel('Indeks próbki n')
    axes[i].set_ylabel('x[n]')
    axes[i].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
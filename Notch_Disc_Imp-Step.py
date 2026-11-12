import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 200.0
f0 = 50.0
omega = 2 * np.pi * f0 / Fs

r1 = 1  # promień zera
r2 = 0.1  # promień bieguna

b = np.array([1.0, -2.0 * r1 * np.cos(omega), r1**2])
a = np.array([1.0, -2.0 * r2 * np.cos(omega), r2**2])

N = len(a) - 1
M = len(b) - 1
N_samples = 70
n = np.arange(0, N_samples)

x_step = np.ones(N_samples)

x_imp = np.zeros(N_samples)
x_imp[0] = 1.0

y_step_builtin = signal.lfilter(b, a, x_step)
y_imp_builtin = signal.lfilter(b, a, x_imp)

w, h = signal.freqz(b, a, worN=1024)
f = (w / np.pi) * (Fs / 2)  # przekształcenie osi częstotliwości na Hz
magnitude_db = 20 * np.log10(np.abs(h))

fig, axes = plt.subplots(3, 1, figsize=(12, 12))
axes = axes.flatten()

axes[0].plot(n, y_step_builtin, 'r-o', markersize=3)
axes[0].set_title('Notch 50Hz - Impuls trwały (skokowy) - scipy.signal.lfilter')
axes[0].set_xlabel('Indeks próbki n')
axes[0].set_ylabel('y[n]')
axes[0].grid(True, linestyle=':', alpha=0.7)

axes[1].plot(n, y_imp_builtin, 'm-o', markersize=3)
axes[1].set_title('Notch 50Hz - Delta Kroneckera (impulsowa) - scipy.signal.lfilter')
axes[1].set_xlabel('Indeks próbki n')
axes[1].set_ylabel('y[n]')
axes[1].grid(True, linestyle=':', alpha=0.7)

axes[2].plot(f, magnitude_db, 'b-', linewidth=1.5)
axes[2].set_title('Notch 50Hz - Odpowiedź częstotliwościowa (Charakterystyka amplitudowa)')
axes[2].set_xlabel('Częstotliwość [Hz]')
axes[2].set_ylabel('Amplituda [dB]')
axes[2].grid(True, linestyle=':', alpha=0.7)
axes[2].axvline(f0, color='g', linestyle='--', label=f'Częstotliwość tłumienia f0 = {f0} Hz')
axes[2].legend()

plt.tight_layout()
plt.show()
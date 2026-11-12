import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 200.0
f0 = 50.0
omega_notch = 2 * np.pi * f0 / Fs

r1 = 1.0 
r2 = 0.9 

b = np.array([1.0, -2.0 * r1 * np.cos(omega_notch), r1**2])
a = np.array([1.0, -2.0 * r2 * np.cos(omega_notch), r2**2])

# Zakres częstotliwości znormalizowanych omega od 0 do pi
N_points = 512
w = np.linspace(0, np.pi, N_points)

H_manual = np.zeros(len(w), dtype=complex)
for idx, wi in enumerate(w):
    num = sum(b[m] * np.exp(-1j * m * wi) for m in range(len(b)))
    den = sum(a[k] * np.exp(-1j * k * wi) for k in range(len(a)))
    H_manual[idx] = num / den

w_builtin, H_builtin = signal.freqz(b, a, worN=N_points)


# Przeliczenie osi na częstotliwość w Hz
f = (w / np.pi) * (Fs / 2)

mag_manual_db = 20 * np.log10(np.abs(H_manual))
mag_builtin_db = 20 * np.log10(np.abs(H_builtin))
phase_manual = np.angle(H_manual)
phase_builtin = np.angle(H_builtin)

fig, axes = plt.subplots(2, 1, figsize=(12, 10))
axes = axes.flatten()

# Charakterystyka amplitudowa
axes[0].plot(f, mag_manual_db, 'b-', label='Implementacja własna (ze wzoru)', linewidth=2.5)
axes[0].plot(f, mag_builtin_db, 'r--', label='scipy.signal.freqz', linewidth=1.5)
axes[0].set_title('Porównanie odpowiedzi częstotliwościowej - Charakterystyka amplitudowa')
axes[0].set_xlabel('Częstotliwość [Hz]')
axes[0].set_ylabel('Amplituda [dB]')
axes[0].grid(True, linestyle=':', alpha=0.7)
axes[0].axvline(f0, color='g', linestyle=':', label=f'Tłumienie f0 = {f0} Hz')
axes[0].legend()

# Charakterystyka fazowa
axes[1].plot(f, phase_manual, 'b-', label='Implementacja własna (ze wzoru)', linewidth=2.5)
axes[1].plot(f, phase_builtin, 'r--', label='scipy.signal.freqz', linewidth=1.5)
axes[1].set_title('Porównanie odpowiedzi częstotliwościowej - Charakterystyka fazowa')
axes[1].set_xlabel('Częstotliwość [Hz]')
axes[1].set_ylabel('Faza [rad]')
axes[1].grid(True, linestyle=':', alpha=0.7)
axes[1].legend()

plt.tight_layout()
plt.show()
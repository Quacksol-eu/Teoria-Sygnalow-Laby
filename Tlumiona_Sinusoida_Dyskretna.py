import numpy as np
import matplotlib.pyplot as plt

A = 1.0
phi = 0.0
omega_0 = 0.4 * np.pi
alpha = 0.05  # Współczynnik tłumienia

N = 40
n = np.arange(0, N)

# 1. Obliczenie z definicji
x_def = A * np.exp(-alpha * n) * np.cos(omega_0 * n + phi)

# 2. Obliczenie z równania różnicowego
x_diff = np.zeros(N)
x_diff[0] = A * np.cos(phi)
x_diff[1] = A * np.exp(-alpha) * np.cos(omega_0 + phi)

r = np.exp(-alpha)
for i in range(2, N):
    x_diff[i] = 2 * r * np.cos(omega_0) * x_diff[i-1] - (r**2) * x_diff[i-2]

fig, axes = plt.subplots(2, 1, figsize=(12, 8))
axes = axes.flatten()

axes[0].plot(n, x_def, 'b-o', markersize=4, label='Z definicji')
axes[0].plot(n, x_diff, 'r--x', markersize=5, label='Z równania różnicowego')
axes[0].set_title('Porównanie sygnału tłumionego (definicja vs równanie różnicowe)')
axes[0].set_xlabel('Indeks próbki n')
axes[0].set_ylabel('x[n]')
axes[0].grid(True, linestyle=':', alpha=0.7)
axes[0].legend(loc='upper right', fontsize=8)

axes[1].plot(n, x_def - x_diff, 'g-o', markersize=4)
axes[1].set_title('Różnica między wynikami obu metod')
axes[1].set_xlabel('Indeks próbki n')
axes[1].set_ylabel('Błąd numeryczny')
axes[1].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
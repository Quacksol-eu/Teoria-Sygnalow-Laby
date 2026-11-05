import numpy as np
import matplotlib.pyplot as plt

A = 1.0
phi = 0.0
omega_0 = 0.4 * np.pi

N = 40
n = np.arange(0, N)
x = np.zeros(N)

x[0] = A * np.cos(phi)
x[1] = A * np.cos(omega_0 + phi)

for i in range(2, N):
    x[i] = 2 * np.cos(omega_0) * x[i-1] - x[i-2]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(n, x, 'b-o', markersize=4)
ax.set_title(f'Sygnał sinusoidalny z równania różnicowego (ω₀ = {omega_0/np.pi:.1f}π rad)')
ax.set_xlabel('Indeks próbki n')
ax.set_ylabel('x[n]')
ax.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
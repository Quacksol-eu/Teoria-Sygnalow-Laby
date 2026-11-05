import numpy as np
import matplotlib.pyplot as plt

A = 1.0
phi = 0.0
omega_0 = 0.4 * np.pi

n = np.arange(0, 40)

x1 = A * np.cos(omega_0 * n + phi)
omega_2 = omega_0 + 2 * np.pi
x2 = A * np.cos(omega_2 * n + phi)

other_omegas = [
    0.1 * np.pi,
    0.6 * np.pi,
    0.8 * np.pi,
    1.2 * np.pi,
    1.6 * np.pi,
    2.0 * np.pi,
    2.1 * np.pi
]

fig, axes = plt.subplots(4, 2, figsize=(14, 16))
axes = axes.flatten()

axes[0].plot(n, x1, 'b-o', markersize=4, label=f'ω₀ = {omega_0/np.pi:.1f}π rad')
axes[0].plot(n, x2, 'r--x', markersize=5, label=f'ω₀ + 2π = {omega_2/np.pi:.1f}π rad (tożsame)')
axes[0].set_title('Porównanie ω₀ oraz ω₀ + 2π')
axes[0].set_xlabel('Indeks próbki n')
axes[0].set_ylabel('x[n]')
axes[0].grid(True, linestyle=':', alpha=0.7)
axes[0].legend(loc='upper right', fontsize=8)

for i, om in enumerate(other_omegas, start=1):
    x_temp = A * np.cos(om * n + phi)
    axes[i].plot(n, x_temp, 'b-o', markersize=4)
    title_str = f'ω₀ = {om/np.pi:.2f}π rad' if om == 2.1 * np.pi else f'ω₀ = {om/np.pi:.1f}π rad'
    axes[i].set_title(title_str)
    axes[i].set_xlabel('Indeks próbki n')
    axes[i].set_ylabel('x[n]')
    axes[i].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
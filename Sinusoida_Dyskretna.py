import numpy as np
import matplotlib.pyplot as plt

A = 1.0          # Amplituda sygnału
phi = 0.0        # Faza początkowa
omega_0 = 0.4 * np.pi  # Częstotliwość bazowa

n = np.arange(0, 40)

# Sygnał bazowy
x1 = A * np.cos(omega_0 * n + phi)

# Sygnał o częstotliwości przesuniętej o okres 2*pi (identyczny ze względu na własności cosinusa)
omega_2 = omega_0 + 2 * np.pi
x2 = A * np.cos(omega_2 * n + phi)

fig, axes = plt.subplots(2, 1, figsize=(12, 8))
ax1, ax2 = axes[0], axes[1]

ax1.stem(n, x1, linefmt='b-', markerfmt='bo', basefmt='k-', label=f'ω₀ = {omega_0/np.pi:.2f}π rad')
ax1.plot(n, x2, 'r--', marker='x', label=f'ω₀ + 2π = {omega_2/np.pi:.2f}π rad (tożsame)')
ax1.set_title('Porównanie sygnałów o częstotliwościach ω₀ oraz ω₀ + 2π')
ax1.set_xlabel('Indeks próbki n')
ax1.set_ylabel('x[n]')
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend(loc='upper right')

omega_values = [0.1 * np.pi, 0.4 * np.pi, 0.8 * np.pi, 1.2 * np.pi]

for om in omega_values:
    x_temp = A * np.cos(om * n + phi)
    ax2.plot(n, x_temp, marker='o', markersize=4, label=f'ω₀ = {om/np.pi:.2f}π rad')

ax2.set_title('Sygnał sinusoidalny dla różnych wartości częstotliwości ω₀')
ax2.set_xlabel('Indeks próbki n')
ax2.set_ylabel('x[n]')
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.show()

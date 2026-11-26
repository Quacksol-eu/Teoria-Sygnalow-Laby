import numpy as np
import matplotlib.pyplot as plt

M = 10
n = np.arange(-M, M + 1)
T = 1*np.pi
omega = np.linspace(-T, T, 2000)
omega_0 = np.pi / 4

signals = [
    ("x[n] = 1", np.ones_like(n, dtype=float)),
    ("x[n] = e^(j * omega_0 * n)", np.exp(1j * omega_0 * n)),
    ("x[n] = cos(omega_0 * n)", np.cos(omega_0 * n))
]

fig, axes = plt.subplots(3, 1, figsize=(8, 10))

for ax, (name, x) in zip(axes, signals):
    X = np.zeros(len(omega), dtype=complex)
    for i, w in enumerate(omega):
        s = 0
        for idx, val in enumerate(n):
            s += x[idx] * np.exp(-1j * w * val)
        X[i] = s
        
    ax.plot(omega, np.abs(X), linewidth=1.5)
    ax.set_title(f'DTFT - {name}')
    ax.set_xlabel('Częstotliwość $\\omega$ [rad/s]')
    ax.set_ylabel('Amplituda')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xlim([-T, T])

plt.tight_layout()
plt.show()
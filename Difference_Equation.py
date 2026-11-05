import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

b = [1.0, 0.5]
a = [1.0, -0.6]

N = len(a) - 1
M = len(b) - 1

N_samples = 40
n = np.arange(0, N_samples)
x = np.zeros(N_samples)
x[0] = 1.0  

# Implementacja własna równania różnicowego N-tego rzędu
y_manual = np.zeros(N_samples)
for i in range(N_samples):
    sum_b = 0.0
    for m in range(M + 1):
        if i - m >= 0:
            sum_b += b[m] * x[i - m]
            
    sum_a = 0.0
    for k in range(1, N + 1):
        if i - k >= 0:
            sum_a += a[k] * y_manual[i - k]
            
    y_manual[i] = (sum_b - sum_a) / a[0]

# Odpowiednik z funkcji scipy.signal.lfilter
y_builtin = signal.lfilter(b, a, x)

fig, axes = plt.subplots(2, 1, figsize=(12, 8))
axes = axes.flatten()

axes[0].plot(n, y_manual, 'b-o', markersize=4)
axes[0].set_title('Implementacja własna')
axes[0].set_xlabel('Indeks próbki n')
axes[0].set_ylabel('y[n]')
axes[0].grid(True, linestyle=':', alpha=0.7)

axes[1].plot(n, y_builtin, 'r-o', markersize=4)
axes[1].set_title('Funkcja scipy.signal.lfilter')
axes[1].set_xlabel('Indeks próbki n')
axes[1].set_ylabel('y[n]')
axes[1].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
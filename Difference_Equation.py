import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

b, a = signal.ellip(4, 3, 40, 0.5)

N = len(a) - 1
M = len(b) - 1
N_samples = 80
n = np.arange(0, N_samples)

# 1. Sygnał pobudzenia: Impuls trwały (odpowiedź skokowa - same jedynki)
x_step = np.ones(N_samples)

# 2. Sygnał pobudzenia: Delta Kroneckera (odpowiedź impulsowa)
x_imp = np.zeros(N_samples)
x_imp[0] = 1.0

# Funkcja pomocnicza do obliczeń równania różnicowego
def compute_filter(b, a, x):
    N_a = len(a) - 1
    M_b = len(b) - 1
    y = np.zeros(len(x))
    for i in range(len(x)):
        sum_b = sum(b[m] * x[i - m] for m in range(M_b + 1) if i - m >= 0)
        sum_a = sum(a[k] * y[i - k] for k in range(1, N_a + 1) if i - k >= 0)
        y[i] = (sum_b - sum_a) / a[0]
    return y

# Obliczenia dla impulsu trwałego (skoku)
y_step_manual = compute_filter(b, a, x_step)
y_step_builtin = signal.lfilter(b, a, x_step)

# Obliczenia dla delty Kroneckera
y_imp_manual = compute_filter(b, a, x_imp)
y_imp_builtin = signal.lfilter(b, a, x_imp)

fig, axes = plt.subplots(4, 1, figsize=(12, 14))
axes = axes.flatten()

axes[0].plot(n, y_step_manual, 'b-o', markersize=3)
axes[0].set_title('Impuls trwały (skokowy) - Implementacja własna')
axes[0].set_xlabel('Indeks próbki n')
axes[0].set_ylabel('y[n]')
axes[0].grid(True, linestyle=':', alpha=0.7)

axes[1].plot(n, y_step_builtin, 'r-o', markersize=3)
axes[1].set_title('Impuls trwały (skokowy) - scipy.signal.lfilter')
axes[1].set_xlabel('Indeks próbki n')
axes[1].set_ylabel('y[n]')
axes[1].grid(True, linestyle=':', alpha=0.7)

axes[2].plot(n, y_imp_manual, 'g-o', markersize=3)
axes[2].set_title('Delta Kroneckera (impulsowa) - Implementacja własna')
axes[2].set_xlabel('Indeks próbki n')
axes[2].set_ylabel('y[n]')
axes[2].grid(True, linestyle=':', alpha=0.7)

axes[3].plot(n, y_imp_builtin, 'm-o', markersize=3)
axes[3].set_title('Delta Kroneckera (impulsowa) - scipy.signal.lfilter')
axes[3].set_xlabel('Indeks próbki n')
axes[3].set_ylabel('y[n]')
axes[3].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
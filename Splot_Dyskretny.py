import numpy as np
import matplotlib.pyplot as plt

# Przykładowe sygnały wejściowe
x = np.array([1.0, 2.0, 3.0, 4.0, 1.0, 1.0, 1.0, 0, 0, 1, 1])
h = np.array([1.0, 1.0, 1.0])

N_x = len(x)
N_h = len(h)
N_y = N_x + N_h - 1

# 1. Implementacja sumy splotu z definicji
y_manual = np.zeros(N_y)
for n in range(N_y):
    sum_val = 0.0
    for k in range(N_x):
        if 0 <= n - k < N_h:
            sum_val += x[k] * h[n - k]
    y_manual[n] = sum_val

# 2. Splot przy użyciu funkcji numpy.convolve (odpowiednik MATLAB-owego conv)
y_builtin = np.convolve(x, h, mode='full')

n_x = np.arange(N_x)
n_h = np.arange(N_h)
n_y = np.arange(N_y)

fig, axes = plt.subplots(3, 1, figsize=(10, 12))

axes[0].stem(n_x, x, linefmt='b-', markerfmt='bo', basefmt='k-')
axes[0].set_title('Sygnał x[n]')
axes[0].grid(True, linestyle=':', alpha=0.7)

axes[1].stem(n_h, h, linefmt='g-', markerfmt='go', basefmt='k-')
axes[1].set_title('Sygnał h[n]')
axes[1].grid(True, linestyle=':', alpha=0.7)

axes[2].plot(n_y, y_manual, 'b-o', markersize=5, label='Implementacja własna (suma splotu)')
axes[2].plot(n_y, y_builtin, 'r--x', markersize=7, label='numpy.convolve (odpowiednik conv)')
axes[2].set_title('Porównanie wyników splotu')
axes[2].set_xlabel('Indeks n')
axes[2].set_ylabel('y[n]')
axes[2].grid(True, linestyle=':', alpha=0.7)
axes[2].legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.show()
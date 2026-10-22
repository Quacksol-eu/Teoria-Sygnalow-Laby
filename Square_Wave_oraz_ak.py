import numpy as np
import matplotlib.pyplot as plt

T0 = 1
T1 = 0.1
Tmax = T0
t = np.linspace(-T0/2, T0/2, 1000)

t_mod = np.mod(t + T0/2, T0) - T0/2
x = np.where(np.abs(t_mod) < T1, 1, 0)

k = np.arange(-15, 16)
Omega0 = (2 * np.pi) / T0
ak = np.where(k == 0, (2 * T1)/ T0, np.sin(k * Omega0 * T1) / (k * np.pi))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t, x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')
plt.title(f'x(t) (T0={T0}, T1={T1})')
plt.legend(['Square Wave'])
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(k, ak, basefmt=" ")
plt.xlabel('Indeks k')
plt.ylabel('a_k')
plt.title('Współczynniki Fouriera (k od -15 do 15)')
plt.grid(True)

plt.tight_layout()
plt.show()
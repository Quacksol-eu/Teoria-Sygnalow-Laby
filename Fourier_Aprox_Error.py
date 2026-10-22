import numpy as np
import matplotlib.pyplot as plt

T0 = 1
T1 = 0.25
t = np.linspace(-T0/2, T0/2, 1000)

t_mod = np.mod(t + T0/2, T0) - T0/2
x = np.where(np.abs(t_mod) < T1, 1, 0)

N_values = np.arange(1, NDemo)
E_values = []

NDemo = 101

Omega0 = (2 * np.pi) / T0

for N in N_values:
    k = np.arange(-N, N+1)
    ak = np.where(k == 0, (2 * T1)/ T0, np.sin(k * Omega0 * T1) / (k * np.pi))
    
    x_approx = np.sum(ak * np.exp(1j * np.outer(t, k) * Omega0), axis=1).real
    
    
    integrand = np.abs(x - x_approx)**2
    E = np.trapz(integrand, t)
    E_values.append(E)


plt.figure(figsize=(18, 4))


k_demo = np.arange(-NDemo, NDemo+1)
ak_demo = np.where(k_demo == 0, (2 * T1)/ T0, np.sin(k_demo * Omega0 * T1) / (k_demo * np.pi))
x_approx_demo = np.sum(ak_demo * np.exp(1j * np.outer(t, k_demo) * Omega0), axis=1).real

plt.subplot(1, 3, 1)
plt.plot(t, x, 'b-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')
plt.title(f'Oryginalny x(t) (T0={T0}, T1={T1})')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(t, x_approx_demo, 'r-')
plt.xlabel('t (s)')
plt.ylabel('x_N(t)')
plt.title(f'Sygnał przybliżony (N=15)')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(N_values, E_values, 'g.-', linewidth=2, markersize=8)
plt.xlabel('Liczba harmonicznych N')
plt.ylabel('Błąd E(N)')
plt.title('Zależność błędu aproksymacji od N')
plt.grid(True)

plt.tight_layout()
plt.show()
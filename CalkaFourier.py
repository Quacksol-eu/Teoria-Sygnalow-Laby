import numpy as np
import matplotlib.pyplot as plt

# Wspólna oś czasu i częstotliwości
t = np.linspace(-3, 3, 1000)
Omega = np.linspace(-40, 40, 500)

T1_rect = 1.0
x1 = np.where(np.abs(t) < T1_rect, 1.0, 0.0)

T1_sin = 1.0
Omega_0 = 12.0
x2 = np.where(np.abs(t) < T1_sin, np.cos(Omega_0 * t), 0.0)

T1_am = 1.0
m = 0.5
Omega_m = 2.5
x3 = np.where(np.abs(t) < T1_am, (1.0 + m * np.cos(Omega_m * t)) * np.cos(Omega_0 * t), 0.0)

# Numeryczne obliczanie transformat Fouriera metodą trapezów
X1 = np.array([np.trapz(x1 * np.exp(-1j * om * t), t) for om in Omega])
X2 = np.array([np.trapz(x2 * np.exp(-1j * om * t), t) for om in Omega])
X3 = np.array([np.trapz(x3 * np.exp(-1j * om * t), t) for om in Omega])

# Rysowanie układu 6 wykresów (3 wiersze, 2 kolumny)
plt.figure(figsize=(14, 12))

# Rząd 1: Prostokąt
plt.subplot(3, 2, 1)
plt.plot(t, x1, 'b-', linewidth=2)
plt.ylabel('x1(t)')
plt.title('1. Impuls prostokątny')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.ylabel('|X1(jΩ)|')
plt.plot(Omega, np.abs(X1), 'r-', linewidth=2)
plt.title('Transformata Fouriera (Prostokąt)')
plt.grid(True)

# Rząd 2: Fragment sinusoidy
plt.subplot(3, 2, 3)
plt.plot(t, x2, 'b-', linewidth=2)
plt.ylabel('x2(t)')
plt.title('2. Fragment sinusoidy (|t| < 1)')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(Omega, np.abs(X2), 'r-', linewidth=2)
plt.ylabel('|X2(jΩ)|')
plt.title('Transformata Fouriera (Sinusoida)')
plt.grid(True)

# Rząd 3: Fragment sinusoidy z modulacją AM
plt.subplot(3, 2, 5)
plt.plot(t, x3, 'b-', linewidth=2)
plt.xlabel('t (s)')
plt.ylabel('x3(t)')
plt.title('3. Fragment sinusoidy AM (|t| < 1)')
plt.grid(True)

plt.subplot(3, 2, 6)
plt.plot(Omega, np.abs(X3), 'r-', linewidth=2)
plt.xlabel('Ω (rad/s)')
plt.ylabel('|X3(jΩ)|')
plt.title('Transformata Fouriera (AM)')
plt.grid(True)

plt.tight_layout()
plt.show()
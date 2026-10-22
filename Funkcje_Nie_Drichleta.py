import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-0.2, 1.1, 3000)

x1 = np.where((t > 0) & (t <= 1), 1.0 / t, 0.0)

x2 = np.where((t > 0) & (t <= 1), np.sin(2 * np.pi / t), 0.0)

x3 = np.zeros_like(t)
for n in range(15):
    t_start = 1.0 - 2.0 ** (-n)
    t_end = 1.0 - 2.0 ** (-(n + 1))
    val = 0.5 ** n
    x3 = np.where((t >= t_start) & (t < t_end), val, x3)

# Rysowanie układu 3 wykresów pod sobą
plt.figure(figsize=(10, 10))

# Wykres 1
plt.subplot(3, 1, 1)
plt.plot(t, x1, 'b-', linewidth=1.5)
plt.ylabel('x1(t)')
plt.title('1. x(t) = 1/t dla 0 < t <= 1')
plt.grid(True)
plt.ylim(-1, 15)

# Wykres 2
plt.subplot(3, 1, 2)
plt.plot(t, x2, 'r-', linewidth=1.5)
plt.ylabel('x2(t)')
plt.title('2. x(t) = sin(2*pi/t) dla 0 < t <= 1')
plt.grid(True)

# Wykres 3
plt.subplot(3, 1, 3)
plt.plot(t, x3, 'g-', linewidth=1.5)
plt.xlabel('t (s)')
plt.ylabel('x3(t)')
plt.title('3. Funkcja schodkowa (wysokość i szerokość dzielona przez 2 co krok)')
plt.grid(True)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Oś czasu obejmująca okresy [-1, 0], [0, 1] oraz [1, 2]
t = np.linspace(-1, 2, 5000)

# Okresowa zmiana zmiennej czasu (wynik w przedziale [0, 1))
t_mod = np.mod(t, 1)

# 1. Okresowa x1(t) = 1 / t_mod (zabezpieczenie przed dzieleniem przez zero w punktach całkowitych)
x1 = np.where(t_mod > 0, 1.0 / t_mod, 0.0)

# 2. Okresowa x2(t) = sin(2*pi / t_mod)
x2 = np.where(t_mod > 0, np.sin(2 * np.pi / t_mod), 0.0)

# 3. Okresowa funkcja schodkowa
x3 = np.zeros_like(t_mod)
for n in range(15):
    t_start = 1.0 - 2.0 ** (-n)
    t_end = 1.0 - 2.0 ** (-(n + 1))
    val = 0.5 ** n
    x3 = np.where((t_mod >= t_start) & (t_mod < t_end), val, x3)

# Rysowanie układu 3 wykresów pod sobą
plt.figure(figsize=(10, 10))

# Wykres 1
plt.subplot(3, 1, 1)
plt.plot(t, x1, 'b-', linewidth=1.5)
plt.ylabel('x1(t)')
plt.title('1. Okresowa x(t) = 1/t (Okres T0 = 1)')
plt.grid(True)
plt.ylim(-1, 15)
plt.xlim(-1, 2)

# Wykres 2
plt.subplot(3, 1, 2)
plt.plot(t, x2, 'r-', linewidth=1.5)
plt.ylabel('x2(t)')
plt.title('2. Okresowa x(t) = sin(2*pi/t) (Okres T0 = 1)')
plt.grid(True)
plt.xlim(-1, 2)

# Wykres 3
plt.subplot(3, 1, 3)
plt.plot(t, x3, 'g-', linewidth=1.5)
plt.xlabel('t (s)')
plt.ylabel('x3(t)')
plt.title('3. Okresowa funkcja schodkowa (Okres T0 = 1)')
plt.grid(True)
plt.xlim(-1, 2)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

Omega0 = 10
Omega1 = 1
Tmax = 10
C = 0.5
fi = (1/2 * np.pi) * 0

t = np.linspace(0, Tmax, num=200)
x = (1 + C * np.cos(Omega1*t)) * (np.cos(Omega0*t + fi))

plt.plot(t, x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')

plt.title('x(t) = (1 + C * cos(Omega1 * t)) * cos(Omega0 * t + fi)')

plt.legend(['Omega0=' + str(Omega0) + ', Omega1=' + str(Omega1) + ', fi=' + str(fi) + ', C=' + str(C) + ', Tmax=' + str(Tmax)])

plt.grid(True)
plt.show()
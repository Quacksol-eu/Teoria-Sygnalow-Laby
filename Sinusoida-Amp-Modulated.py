import numpy as np
import matplotlib.pyplot as plt

Omega0 = 0.5
Omega1 = 0.1
Tmax = 100
C = 1
fi = 1/2 * np.pi

t = np.linspace(-Tmax, Tmax, num=200)
x = (1 + C * np.cos(Omega1*t)) * (np.cos(Omega0*t + fi))

plt.plot(t, x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')

plt.title('x(t) = (1 + C * cos(Omega1 * t)) * cos(Omega0 * t + fi)')

plt.legend(['Omega0=' + str(Omega0) + ', Omega1=' + str(Omega1) + ', fi=' + str(fi) + ', C=' + str(C) + ', Tmax=' + str(Tmax)])

plt.grid(True)
plt.show()
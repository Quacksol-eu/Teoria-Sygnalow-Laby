import numpy as np
import matplotlib.pyplot as plt

Omega0 = 10
Omega1 = 1
Tmax = 20
C = 5
fi = 0

t = np.linspace(0, Tmax, num=1000)
x = np.cos(Omega0 * t + C * np.cos(Omega1*t))

plt.plot(t, x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')

plt.title('x(t) = cos(Omega0 * t + C * cos(Omega1 * t))')

#plt.legend(['Omega0=' + str(Omega0) + ', Omega1=' + str(Omega1) + ', C=' + str(C) + ', Tmax=' + str(Tmax)])

plt.grid(True)
plt.show()
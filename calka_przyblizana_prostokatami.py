import numpy as np
import matplotlib.pyplot as plt

Omega0 = 10
Tmax = 1

t = np.linspace(-Tmax, Tmax, num=50)
x = -t**2 + 0.5 * t + 2

plt.plot(t, x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')


plt.title('x(t) = -t^2 + 0.5 * t + 2')

plt.legend(['Omega0=' + str(Omega0) + ', Tmax=' + str(Tmax)])

plt.grid(True)
plt.show()
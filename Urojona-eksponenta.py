import numpy as np
import matplotlib.pyplot as plt

Omega0 = 1.0
Tmax = 10

t = np.linspace(-Tmax, Tmax, num=200)
x = np.exp(1j * Omega0 * t)

plt.plot(t, np.real(x), 'r-', t, np.imag(x), 'b--')
plt.xlabel('t (s)')
plt.ylabel('x(t)')
plt.title('x(t) = exp(j*Omega0*t)')
plt.legend(['Omega_0 = ' + str(Omega0) + ', Tmax = ' + str(Tmax)])
plt.grid(True)
plt.show()
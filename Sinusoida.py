import numpy as np
import matplotlib.pyplot as plt

Omega0 = 1.0
Tmax = 10
fi = 1/2 * np.pi

t = np.linspace(-Tmax, Tmax, num=200)
x = np.cos((Omega0 * t)+ fi) 

plt.plot(t,x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')
plt.title('x(t) = cos(Omega0 * t + fi)')
plt.legend(['Omega_0 = ' + str(Omega0) + 'fi = ' + str(fi), 'Tmax = ' + str(Tmax)])
plt.grid(True)
plt.show()
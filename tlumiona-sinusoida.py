import numpy as np
import matplotlib.pyplot as plt

Omega0 = 0.5
Tmax = 100
a = 0.01
C = 1
fi = 1/2 * np.pi

t = np.linspace(-Tmax, 3*Tmax, num=1000)
x = np.cos((Omega0 * t) + fi) * C * np.exp(a * -t)  
plt.plot(t, x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')
plt.title('x(t) = C * exp(at) * cos(Omega0 * t + fi)')


plt.legend(['Omega0=' + str(Omega0) + ', fi=' + str(fi) + ', a=' + str(a) + ', C=' + str(C) + ', Tmax=' + str(Tmax)])

plt.grid(True)
plt.show()

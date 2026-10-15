import numpy as np
import matplotlib.pyplot as plt

Tmax = 1
q = 20

t = np.linspace(-Tmax, Tmax, num=q)
x = -t**2 + 0.5 * t + 2

dt = t[1] - t[0]
I = 0

for i in range(q - 1):
    I = I + ((x[i] + x[i+1]) * dt/2)  

plt.plot(t, x, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('x(t)')

plt.title('x(t) = -t^2 + 0.5 * t + 2')
plt.legend(['Tmax=' + str(Tmax) + ', q=' + str(q) + ', I=' + str(round(I, 3))])

plt.grid(True)
plt.show()
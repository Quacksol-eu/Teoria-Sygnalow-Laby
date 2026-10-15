import numpy as np
import matplotlib.pyplot as plt

Tmax = 3.0
q = 50

t = np.linspace(-Tmax, Tmax, num=q)
tau = np.linspace(-Tmax, Tmax, num=q)
dt = tau[1] - tau[0]

y = np.zeros(q)

for i in range(q):
    I = 0.0
    for j in range(q):
        tau_val = tau[j]

        if tau_val >= -1 and tau_val <= 1:
            x_val = 0.5
        else:
            x_val = 0.0
            
        arg = t[i] - tau_val
        if arg >= -1 and arg <= 1:
            h_val = 1 + arg
        else:
            h_val = 0.0
            
        I = I + x_val * h_val * dt
        
    y[i] = I

plt.plot(t, y, 'b.-')
plt.xlabel('t (s)')
plt.ylabel('y(t)')

plt.title('Splot y(t) = (x * h)(t)')
plt.legend(['Tmax=' + str(Tmax) + ', q=' + str(q)])

plt.grid(True)
plt.show()
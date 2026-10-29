import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

f0 = 50.0
omega0 = 2 * np.pi * f0

a = -10.0       
b = omega0    
c = 10.0  

zeros = np.array([-a + 1j * b, -a - 1j * b])
poles = np.array([-c + 1j * b, -c - 1j * b])
gain = 1.0

filt_system = signal.ZerosPolesGain(zeros, poles, gain)

# --- Przygotowanie danych ---
t, y_imp = signal.impulse((zeros, poles, gain), T=np.linspace(0, 0.2, 1000))

frequencies = np.linspace(0, 2*f0, 1000)
omega = 2 * np.pi * frequencies
w, mag, phase = signal.bode(filt_system, omega)

#-------------
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 14))
#-------------

ax1.plot(np.real(zeros), np.imag(zeros), 'go', markersize=10, label='Zera (Zeros)')
ax1.plot(np.real(poles), np.imag(poles), 'rx', markersize=10, label='Bieguny (Poles)')

ax1.spines['left'].set_position('zero')
ax1.spines['bottom'].set_position('zero')
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

ax1.set_xlim(-25, 15)
ax1.set_ylim(-350, 350)

ax1.set_title('Zera i bieguny transmitancji H(s)', pad=20)
ax1.set_xlabel('Real (σ)', loc='right')
ax1.set_ylabel('Imag (jω)', loc='top', rotation=0)
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend(loc='upper right')

#-------------
ax2.plot(t, y_imp, 'b-')
ax2.set_title('Odpowiedź impulsowa filtru Notch')
ax2.set_xlabel('Czas t (s)')
ax2.set_ylabel('h(t)')
ax2.grid(True)

#-------------
ax3.plot(w / (2 * np.pi), mag, 'b-')
ax3.set_title('Charakterystyka amplitudowa (Magnitude Response)')
ax3.set_xlabel('Częstotliwość f (Hz)')
ax3.set_ylabel('Amplituda (dB)')
ax3.grid(True)

plt.tight_layout()
plt.show()
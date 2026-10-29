import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

f0 = 50.0
omega0 = 2 * np.pi * f0

a = 0.0       # Część rzeczywista zer (0.0 oznacza, że leżą idealnie na osi urojonej -> silna dziura)
b = omega0    
c = 10.0      # Część rzeczywista biegunów (im większa, tym szersza dziura)  

zeros = np.array([-a + 1j * b, -a - 1j * b])
poles = np.array([-c + 1j * b, -c - 1j * b])
gain = 1.0

B, A = signal.zpk2tf(zeros, poles, gain)

# --- Przygotowanie danych ---
Om = np.linspace(0, 2 * np.pi * (2 * f0), 1000)

# Bezpośrednie obliczenie odpowiedzi częstotliwościowej dla s = j*Om
H_lab = np.polyval(B, s) / np.polyval(A, s) # (lub po prostu użycie H_scipy)

# Odpowiednik funkcyjny ze SciPy do porównania
w_scipy, H_scipy = signal.freqs(B, A, Om)

#-------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
#-------------

ax1.plot(Om / (2 * np.pi), np.abs(H_lab), 'b-', linewidth=2, label='Bezpośrednie obliczenie')
ax1.plot(Om / (2 * np.pi), np.abs(H_scipy), 'r--', linewidth=2, label='scipy.signal.freqs')
ax1.set_title('Porównanie modułu odpowiedzi częstotliwościowej (Dziura/Notch)', pad=20)
ax1.set_xlabel('Częstotliwość f (Hz)')
ax1.set_ylabel('|H(jΩ)|')
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend(loc='upper right')

#-------------
ax2.plot(Om / (2 * np.pi), np.angle(H_lab), 'b-', linewidth=2, label='Bezpośrednie obliczenie')
ax2.plot(Om / (2 * np.pi), np.angle(H_scipy), 'r--', linewidth=2, label='scipy.signal.freqs')
ax2.set_title('Porównanie fazy odpowiedzi częstotliwościowej', pad=20)
ax2.set_xlabel('Częstotliwość f (Hz)')
ax2.set_ylabel('Faza (rad)')
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.legend(loc='lower right')

plt.tight_layout()
plt.show()

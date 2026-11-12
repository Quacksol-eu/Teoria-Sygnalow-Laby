import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parametry projektu
Fs = 5000.0
fp = 1000.0
fst = 1500.0
rp = 1.0
rs = 30.0

wp = fp / (Fs / 2)
ws = fst / (Fs / 2)

# Wyznaczanie rzędów i współczynników filtrów
N_b, Wn_b = signal.buttord(wp, ws, rp, rs)
b_butt, a_butt = signal.butter(N_b, Wn_b, btype='low')

N_c1, Wn_c1 = signal.cheb1ord(wp, ws, rp, rs)
b_ch1, a_ch1 = signal.cheby1(N_c1, rp, Wn_c1, btype='low')

N_c2, Wn_c2 = signal.cheb2ord(wp, ws, rp, rs)
b_ch2, a_ch2 = signal.cheby2(N_c2, rs, Wn_c2, btype='low')

N_e, Wn_e = signal.ellipord(wp, ws, rp, rs)
b_ell, a_ell = signal.ellip(N_e, rp, rs, Wn_e, btype='low')

filters = [
    ("Butterworth", b_butt, a_butt, N_b),
    ("Chebyshev I", b_ch1, a_ch1, N_c1),
    ("Chebyshev II", b_ch2, a_ch2, N_c2),
    ("Elliptic", b_ell, a_ell, N_e)
]

w, _ = signal.freqz(b_butt, a_butt, worN=512)
f = (w / np.pi) * (Fs / 2)

N_samples = 40
n = np.arange(0, N_samples)
x_imp = np.zeros(N_samples)
x_imp[0] = 1.0

# Tworzenie siatki wykresów 4x3 (łącznie 12 wykresów)
fig, axes = plt.subplots(4, 3, figsize=(16, 12))

for i, (name, b, a, order) in enumerate(filters):
    # Odpowiedź częstotliwościowa
    _, h = signal.freqz(b, a, worN=512)
    mag_db = 20 * np.log10(np.abs(h))
    phase = np.unwrap(np.angle(h))
    
    # Odpowiedź impulsowa
    y_imp = signal.lfilter(b, a, x_imp)
    
    # Kolumna 0: Charakterystyka amplitudowa
    axes[i, 0].plot(f, mag_db, 'b-', linewidth=1.5)
    axes[i, 0].set_title(f'{name} (N={order}) - Amplituda')
    axes[i, 0].set_ylabel('Amplituda [dB]')
    axes[i, 0].grid(True, linestyle=':', alpha=0.7)
    axes[i, 0].axvline(fp, color='gray', linestyle='--', alpha=0.7)
    
    # Kolumna 1: Charakterystyka fazowa
    axes[i, 1].plot(f, phase, 'r-', linewidth=1.5)
    axes[i, 1].set_title(f'{name} - Faza')
    axes[i, 1].set_ylabel('Faza [rad]')
    axes[i, 1].grid(True, linestyle=':', alpha=0.7)
    
    # Kolumna 2: Odpowiedź impulsowa
    axes[i, 2].stem(n, y_imp, linefmt='g-', markerfmt='go', basefmt='k-')
    axes[i, 2].set_title(f'{name} - Odp. impulsowa')
    axes[i, 2].set_ylabel('y[n]')
    axes[i, 2].grid(True, linestyle=':', alpha=0.7)

    # Etykiety osi X
    for col in range(3):
        axes[i, col].set_xlabel('Częstotliwość [Hz]' if col < 2 else 'Indeks próbki n')

plt.tight_layout()
plt.show()
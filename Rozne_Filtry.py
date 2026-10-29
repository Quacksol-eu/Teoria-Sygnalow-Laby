import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Specyfikacja projektu ---
f_pass = 1000.0  # Częstotliwość graniczna pasma przepustowego (Hz)
f_stop = 1500.0  # Częstotliwość graniczna pasma zaporowego (Hz)
omega_pass = 2 * np.pi * f_pass
omega_stop = 2 * np.pi * f_stop

Rp = 1.0   # Dopuszczalne falowanie w pasmie przepustowym (dB)
Rs = 30.0  # Minimalne tłumienie w pasmie zaporowym (dB)

# --- Wybór filtru do wyróżnienia (1: Butterworth, 2: Chebyshev I, 3: Chebyshev II, 4: Elliptic, 5: Bessel) ---
Selected_Filter = 2

# --- Wyznaczanie rzędów i projektowanie filtrów ---
N_butt, Wn_butt = signal.buttord(omega_pass, omega_stop, Rp, Rs, analog=True)
b_butt, a_butt = signal.butter(N_butt, Wn_butt, btype='low', analog=True)
z_butt, p_butt, k_butt = signal.tf2zpk(b_butt, a_butt)

N_cheb1, Wn_cheb1 = signal.cheb1ord(omega_pass, omega_stop, Rp, Rs, analog=True)
b_cheb1, a_cheb1 = signal.cheby1(N_cheb1, Rp, Wn_cheb1, btype='low', analog=True)
z_cheb1, p_cheb1, k_cheb1 = signal.tf2zpk(b_cheb1, a_cheb1)

N_cheb2, Wn_cheb2 = signal.cheb2ord(omega_pass, omega_stop, Rp, Rs, analog=True)
b_cheb2, a_cheb2 = signal.cheby2(N_cheb2, Rs, Wn_cheb2, btype='low', analog=True)
z_cheb2, p_cheb2, k_cheb2 = signal.tf2zpk(b_cheb2, a_cheb2)

N_ellip, Wn_ellip = signal.ellipord(omega_pass, omega_stop, Rp, Rs, analog=True)
b_ellip, a_ellip = signal.ellip(N_ellip, Rp, Rs, Wn_ellip, btype='low', analog=True)
z_ellip, p_ellip, k_ellip = signal.tf2zpk(b_ellip, a_ellip)

N_bessel = N_butt
b_bessel, a_bessel = signal.bessel(N_bessel, omega_pass, btype='low', analog=True, norm='delay')
z_bessel, p_bessel, k_bessel = signal.tf2zpk(b_bessel, a_bessel)

print(f"Wyznaczone rzędy filtrów:")
print(f" - Butterworth:    N = {N_butt}")
print(f" - Chebyshev I:    N = {N_cheb1}")
print(f" - Chebyshev II:   N = {N_cheb2}")
print(f" - Elliptic:       N = {N_ellip}")
print(f" - Bessel:         N = {N_bessel}")

# --- Przygotowanie danych ---
frequencies = np.linspace(0, 2.5 * f_pass, 2000)
omega = 2 * np.pi * frequencies

w_b, mag_b, phase_b = signal.bode((b_butt, a_butt), omega)
w_c1, mag_c1, phase_c1 = signal.bode((b_cheb1, a_cheb1), omega)
w_c2, mag_c2, phase_c2 = signal.bode((b_cheb2, a_cheb2), omega)
w_e, mag_e, phase_e = signal.bode((b_ellip, a_ellip), omega)
w_bes, mag_bes, phase_bes = signal.bode((b_bessel, a_bessel), omega)

t, y_butt = signal.impulse((b_butt, a_butt), T=np.linspace(0, 0.002, 10000))
_, y_cheb1 = signal.impulse((b_cheb1, a_cheb1), T=t)
_, y_cheb2 = signal.impulse((b_cheb2, a_cheb2), T=t)
_, y_ellip = signal.impulse((b_ellip, a_ellip), T=t)
_, y_bessel = signal.impulse((b_bessel, a_bessel), T=t)

# Lista strukturyzująca filtry dla łatwego i czystego rysowania
filters_data = [
    {"id": 1, "name": f"Butterworth (N={N_butt})", "short": "Butterworth", "mag": mag_b, "phase": phase_b, "y": y_butt, "poles": p_butt},
    {"id": 2, "name": f"Chebyshev I (N={N_cheb1})", "short": "Chebyshev I", "mag": mag_c1, "phase": phase_c1, "y": y_cheb1, "poles": p_cheb1},
    {"id": 3, "name": f"Chebyshev II (N={N_cheb2})", "short": "Chebyshev II", "mag": mag_c2, "phase": phase_c2, "y": y_cheb2, "poles": p_cheb2},
    {"id": 4, "name": f"Elliptic (N={N_ellip})", "short": "Elliptic", "mag": mag_e, "phase": phase_e, "y": y_ellip, "poles": p_ellip},
    {"id": 5, "name": f"Bessel (N={N_bessel})", "short": "Bessel", "mag": mag_bes, "phase": phase_bes, "y": y_bessel, "poles": p_bessel},
]

# ==========================================
# GŁÓWNE OKNO Z UKŁADEM 3x2 (5 WYKRESÓW)
# ==========================================
fig, axes = plt.subplots(3, 2, figsize=(14, 15))
ax1, ax2 = axes[0]
ax3, ax4 = axes[1]
ax5, ax6 = axes[2]

# Rysowanie charakterystyk z uwzględnieniem wybranego filtru
for f in filters_data:
    is_selected = (f["id"] == Selected_Filter)
    color = 'red' if is_selected else 'gray'
    alpha = 1.0 if is_selected else 0.35
    linewidth = 2.2 if is_selected else 1.0
    zorder = 10 if is_selected else 1

    # 1. Charakterystyka amplitudowa (pełna)
    ax1.plot(frequencies, f["mag"], color=color, alpha=alpha, linewidth=linewidth, zorder=zorder, label=f["name"])

    # 2. Przybliżenie początku charakterystyki amplitudowej (pasmo przepustowe)
    ax2.plot(frequencies, f["mag"], color=color, alpha=alpha, linewidth=linewidth, zorder=zorder, label=f["short"])

    # 3. Charakterystyka fazowa
    ax3.plot(frequencies, f["phase"], color=color, alpha=alpha, linewidth=linewidth, zorder=zorder, label=f["short"])

    # 4. Odpowiedź impulsowa
    ax4.plot(t * 1000, f["y"], color=color, alpha=alpha, linewidth=linewidth, zorder=zorder, label=f["short"])

    # 5. Rozmieszczenie biegunów na płaszczyźnie zespolonej
    ax5.plot(np.real(f["poles"]), np.imag(f["poles"]), 'x', color=color, alpha=alpha, markersize=8, zorder=zorder, label=f["short"])

# Dodatkowe linie i opisy dla wykresów amplitudowych
ax1.axvline(f_pass, color='gray', linestyle='--', alpha=0.7, label='F_pass')
ax1.axvline(f_stop, color='black', linestyle='--', alpha=0.7, label='F_stop')
ax1.axhline(-Rp, color='blue', linestyle=':', alpha=0.5)
ax1.axhline(-Rs, color='red', linestyle=':', alpha=0.5)
ax1.set_title('Charakterystyka amplitudowa')
ax1.set_xlabel('Częstotliwość f (Hz)')
ax1.set_ylabel('Amplituda (dB)')
ax1.set_xlim(0, 2.5 * f_pass)
ax1.set_ylim(-50, 5)
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend(loc='lower left', fontsize=8)

ax2.axvline(f_pass, color='gray', linestyle='--', alpha=0.7, label='F_pass')
ax2.axhline(-Rp, color='blue', linestyle=':', alpha=0.5, label=f'-Rp ({Rp} dB)')
ax2.set_title('Przybliżenie pasma przepustowego (Początek)')
ax2.set_xlabel('Częstotliwość f (Hz)')
ax2.set_ylabel('Amplituda (dB)')
ax2.set_xlim(0, f_pass)
ax2.set_ylim(-2.0, 0.5)
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.legend(loc='lower left', fontsize=8)

ax3.set_title('Charakterystyka fazowa')
ax3.set_xlabel('Częstotliwość f (Hz)')
ax3.set_ylabel('Faza (stopnie)')
ax3.set_xlim(0, 2.5 * f_pass)
ax3.grid(True, linestyle=':', alpha=0.7)
ax3.legend(loc='lower left', fontsize=8)

ax4.set_title('Odpowiedź impulsowa')
ax4.set_xlabel('Czas t (ms)')
ax4.set_ylabel('h(t)')
ax4.grid(True, linestyle=':', alpha=0.7)
ax4.legend(loc='upper right', fontsize=8)

ax5.spines['left'].set_position('zero')
ax5.spines['bottom'].set_position('zero')
ax5.spines['right'].set_color('none')
ax5.spines['top'].set_color('none')
ax5.set_title('Bieguny filtrów (Poles)')
ax5.set_xlabel('Real', loc='right')
ax5.set_ylabel('Imag', loc='top', rotation=0)
ax5.grid(True, linestyle=':', alpha=0.7)
ax5.legend(loc='upper left', fontsize=8)

# 6. Ukrycie ostatniego pustego pola w siatce
ax6.axis('off')

plt.tight_layout()
plt.show()


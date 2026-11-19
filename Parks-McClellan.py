import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 5000.0
fpass = 1000.0
fstop = 1500.0
Rp = 1.0
Rs = 30.0

nyq = Fs / 2.0
wp = fpass / nyq
ws = fstop / nyq
width = (fstop - fpass) / nyq

N_kaiser, beta = signal.kaiserord(Rs, width)
if N_kaiser % 2 == 0:
    N_kaiser += 1
h_kaiser = signal.firwin(N_kaiser, wp, window=('kaiser', beta), pass_zero='lowpass')


N_pm = 15 
bands = [0, wp, ws, 1.0]
desired = [1.0, 0.0]
delta_p = (10**(Rp / 20) - 1) / (10**(Rp / 20) + 1)
delta_s = 10**(-Rs / 20)
weights = [1.0 / delta_p, 1.0 / delta_s]
h_pm = signal.remez(N_pm, bands, desired, weight=weights, fs=2.0)

print(f"Kaiser M = {N_kaiser}")
print(f"Parks-McClellan M = {N_pm}")

# Wykres
plt.figure(figsize=(10, 6))

w_k, h_resp_k = signal.freqz(h_kaiser, 1.0, worN=2048)
f_k = (w_k / np.pi) * nyq
mag_k = 20 * np.log10(np.abs(h_resp_k) + 1e-12)

w_p, h_resp_p = signal.freqz(h_pm, 1.0, worN=2048)
f_p = (w_p / np.pi) * nyq
mag_p = 20 * np.log10(np.abs(h_resp_p) + 1e-12)

plt.plot(f_k, mag_k, label=f'Kaiser (M={N_kaiser})')
plt.plot(f_p, mag_p, label=f'Parks-McClellan (M={N_pm})', linestyle='--')

plt.axvline(fpass, color='gray', linestyle=':', label=f'Fpass = {fpass} Hz')
plt.axvline(fstop, color='gray', linestyle='-.', label=f'Fstop = {fstop} Hz')
plt.axhline(-Rp, color='red', linestyle=':', alpha=0.5)
plt.axhline(-Rs, color='blue', linestyle=':', alpha=0.5)

plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda [dB]')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.ylim([-60, 5])
plt.xlim([0, nyq])
plt.tight_layout()
plt.show()
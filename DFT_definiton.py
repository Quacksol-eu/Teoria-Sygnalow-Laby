import numpy as np
import matplotlib.pyplot as plt

N = 64
n = np.arange(N)
omega_0 = 2 * np.pi * 4 / N

signals = [
    ("x[n] = 1", np.ones(N, dtype=float)),
    ("x[n] = e^(j * omega_0 * n)", np.exp(1j * omega_0 * n)),
    ("x[n] = cos(omega_0 * n)", np.cos(omega_0 * n))
]

for name, x in signals:
    # 1. Obliczenie DFT
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        s = 0
        for idx in range(N):
            s += x[idx] * np.exp(-1j * (2 * np.pi / N) * k * idx)
        X[k] = s

    # 2. Obliczenie IDFT
    x_rec = np.zeros(N, dtype=complex)
    for idx in range(N):
        s = 0
        for k in range(N):
            s += X[k] * np.exp(1j * (2 * np.pi / N) * k * idx)
        x_rec[idx] = s / N

    X_fft_ref = np.fft.fft(x)
    x_ifft_ref = np.fft.ifft(X)

    err_dft = np.abs(X - X_fft_ref)
    err_idft = np.abs(x - x_ifft_ref)
    err_rec = np.abs(x - x_rec)

    fig, axes = plt.subplots(3, 1, figsize=(8, 10))

    # Wykres 1: DFT vs np.fft.fft
    axes[0].plot(n, np.abs(X), label='DFT własne', color='tab:blue', linewidth=1.5)
    axes[0].plot(n, np.abs(X_fft_ref), '--', label='np.fft.fft', color='tab:orange', linewidth=1.5)
    axes[0].set_title(f'DFT - {name}')
    axes[0].set_xlabel('Indeks k')
    axes[0].set_ylabel('Amplituda')
    axes[0].grid(True, linestyle=':', alpha=0.7)
    axes[0].legend(loc='upper right')
    axes[0].set_xlim([0, N - 1])

    # Wykres 2: IDFT vs np.fft.ifft
    axes[1].plot(n, np.real(x_rec), label='IDFT własne (R)', color='tab:green', linewidth=1.5)
    axes[1].plot(n, np.real(x_ifft_ref), '--', label='np.fft.ifft (R)', color='tab:red', linewidth=1.5)
    axes[1].set_title(f'IDFT - {name}')
    axes[1].set_xlabel('Próbka n')
    axes[1].set_ylabel('Wartość rzeczywista')
    axes[1].grid(True, linestyle=':', alpha=0.7)
    axes[1].legend(loc='upper right')
    axes[1].set_xlim([0, N - 1])

    # Wykres 3: Błędy
    axes[2].plot(n, err_dft, label='Różnica DFT vs fft', color='tab:purple', linewidth=1.5)
    axes[2].plot(n, err_idft, label='Różnica IDFT vs ifft', color='tab:brown', linewidth=1.5)
    axes[2].plot(n, err_rec, ':', label='Błąd rekonstrukcji x[n] - IDFT(DFT)', color='black', linewidth=1.5)
    axes[2].set_title(f'Błędy - {name}')
    axes[2].set_xlabel('Indeks n / k')
    axes[2].set_ylabel('Wartość błędu')
    axes[2].grid(True, linestyle=':', alpha=0.7)
    axes[2].legend(loc='upper right')
    axes[2].set_xlim([0, N - 1])

    plt.tight_layout()
    plt.show()
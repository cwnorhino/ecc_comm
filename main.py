import numpy as np
from modulation import bpsk_modulate
from modulation import bpsk_demodulate
from channel import awgn_channel
from ber import calculate_ber
from ecc import hamming74_encode, hamming74_decode


N = 10000
#bit stream
bits = np.random.randint(0,2,N)

'''print(bits[:20])
print(type(bits), bits.shape)
'''
#modulate the bits into signals
tx_symbols = bpsk_modulate(bits)


'''print(bits[:10])
print(tx_symbols[:10])
'''
rx_signal = awgn_channel(tx_symbols, snr_db=5)

rx_bits = bpsk_demodulate(rx_signal)
ber_no_ecc = calculate_ber(bits,rx_bits)

print(tx_symbols[:10])
print(rx_signal[:10])
print(rx_bits[:10])
print("BER without ECC:", ber_no_ecc)

# Encode
encoded_bits = hamming74_encode(bits)

# Modulate
tx_symbols_ecc = bpsk_modulate(encoded_bits)

# Channel
rx_signal_ecc = awgn_channel(tx_symbols_ecc, snr_db=5)

# Demodulate
rx_bits_ecc = bpsk_demodulate(rx_signal_ecc)

# Decode
decoded_bits = hamming74_decode(rx_bits_ecc)

# BER with ECC
ber_ecc = calculate_ber(bits[:len(decoded_bits)], decoded_bits)

print("BER with Hamming (7,4):", ber_ecc)

import matplotlib.pyplot as plt

# SNR range (in dB)
snr_db_range = np.arange(0, 11, 1)

ber_no_ecc_list = []
ber_ecc_list = []

for snr_db in snr_db_range:

    # ---------- NO ECC ----------
    tx_symbols = bpsk_modulate(bits)
    rx_signal = awgn_channel(tx_symbols, snr_db)
    rx_bits = bpsk_demodulate(rx_signal)
    ber_no_ecc = calculate_ber(bits, rx_bits)
    ber_no_ecc_list.append(ber_no_ecc)

    # ---------- WITH HAMMING (7,4) ----------
    encoded_bits = hamming74_encode(bits)
    tx_symbols_ecc = bpsk_modulate(encoded_bits)
    rx_signal_ecc = awgn_channel(tx_symbols_ecc, snr_db)
    rx_bits_ecc = bpsk_demodulate(rx_signal_ecc)
    decoded_bits = hamming74_decode(rx_bits_ecc)

    # Match lengths
    ber_ecc = calculate_ber(bits[:len(decoded_bits)], decoded_bits)
    ber_ecc_list.append(ber_ecc)

# ---------- PLOT ----------
plt.figure()
plt.semilogy(snr_db_range, ber_no_ecc_list, marker='o', label='BPSK (No ECC)')
plt.semilogy(snr_db_range, ber_ecc_list, marker='s', label='BPSK + Hamming (7,4)')

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR for BPSK with and without ECC")
plt.grid(True, which='both')
plt.legend()

plt.show()

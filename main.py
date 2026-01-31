import numpy as np
from modulation import bpsk_modulate
from modulation import bpsk_demodulate
from channel import awgn_channel
from ber import calculate_ber

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

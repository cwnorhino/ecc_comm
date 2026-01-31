import numpy as np
def bpsk_modulate(bits):
    return 1 - 2 * bits

def bpsk_demodulate(signal):
    return (signal < 0).astype(int)
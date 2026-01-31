import numpy as np
def awgn_channel(signals,snr_db):
    snr_linear = 10 ** (snr_db / 10)
    noise_power = 1 / snr_linear
    noise = np.sqrt(noise_power / 2) * np.random.randn(len(signals))

    return signals + noise



    
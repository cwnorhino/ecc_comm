import numpy as np

def hamming74_encode(bits):
    # Make length divisible by 4
    bits = bits[:len(bits)//4 * 4]

    # Reshape into blocks of 4
    bits = bits.reshape(-1, 4)

    d1 = bits[:, 0]
    d2 = bits[:, 1]
    d3 = bits[:, 2]
    d4 = bits[:, 3]

    # Parity bits (even parity)
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    # Codeword: [p1 p2 d1 p3 d2 d3 d4]
    codewords = np.stack((p1, p2, d1, p3, d2, d3, d4), axis=1)

    return codewords.reshape(-1)
def hamming74_decode(bits):
    bits = bits.reshape(-1, 7)

    b1, b2, b3, b4, b5, b6, b7 = bits.T

    # Syndrome bits
    s1 = b1 ^ b3 ^ b5 ^ b7
    s2 = b2 ^ b3 ^ b6 ^ b7
    s3 = b4 ^ b5 ^ b6 ^ b7

    syndrome = s1 + 2*s2 + 4*s3

    # Correct single-bit errors
    for i in range(len(syndrome)):
        if syndrome[i] != 0:
            bits[i, syndrome[i] - 1] ^= 1

    # Extract original data bits
    decoded = bits[:, [2, 4, 5, 6]]
    return decoded.reshape(-1)

"""
An implementation of the RSA encryption scheme, invented by Rivest, Shamir and Adleman.
"""

import sys
sys.path.insert(0, "../")

from utils import maths


def encrypt(m: int, e: int, n: int) -> int:
    """
    Encrypts a message m using the naive RSA algorithm.

    Source:
        https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Encryption

    Parameters:
        m (int): An arbitrarily chosen plaintext message
        e (int): Exponent e
        n (int): Part of the public key

    Returns:
        int: Encrypted plaintext message (ciphertext)
    """

    return m**e % n


def decrypt(c: int, d: int, n: int) -> int:
    """
    Decrypts a ciphertext c using the naive RSA algorithm.

    Source:
        https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption

    Parameters:
        c (int): Ciphertext to decrpt
        d (int): Modular inverse of exponent e
        n (int): Part of the public/secret key

    Returns:
        int: Decrypted ciphertext (plaintext)
    """

    return c**d % n


def generate_keys(
    p: int, q: int, e: int
) -> tuple[tuple[int, int], tuple[int, int, int]]:
    """
    Generate keys from two chosen primes and exponent e.

    Source:
        https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation

    Parameters:
        p (int): An arbitrarily chosen prime p
        q (int): An arbitrarily chosen prime q
        e (int): exponent such that gcd(e, (p-1) * (q-1)) = 1

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: (public key, secret key)
    """

    n = p * q
    phi = (p - 1) * (q - 1)

    (g, d, _) = maths.extended_euclidean_algorithm(e, phi)
    if g != 1:
        return None

    d %= phi
    if e * d % phi != 1:
        return None

    return ((n, e), (p, q, d))

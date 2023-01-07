"""
Implementation of the Caesar cipher.
"""

import sys
sys.path.insert(0, "../")

import shift


def encrypt(plaintext: str) -> str:
    """
    Encryption with the Caesar cipher.

    Parameters:
        plaintext (str): Plaintext to encrypt

    Returns:
        str: Ciphertext
    """

    return shift.encrypt(plaintext, 3)


def decrypt(ciphertext: str) -> str:
    """
    Decryption with the Caesar cipher.

    Parameters:
        ciphertext (str): Ciphertext to decrypt

    Returns:
        str: Plaintext
    """

    return shift.decrypt(ciphertext, 3)

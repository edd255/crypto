"""
An implementation of the Shift cipher.
"""

import sys
sys.path.insert(0, "../")

from utils import alphabet


def encrypt(plaintext: str, key: int) -> str:
    """
    Encryption with the Shift cipher.

    Parameters:
        plaintext (str): Plaintext to encrypt
        key (int): Number of shifts

    Returns:
        str: Ciphertext
    """

    ciphertext = ""
    for character in plaintext:
        if alphabet.is_letter(character):
            ciphertext += alphabet.shift_letter(character, key, True)
        else:
            ciphertext += character

    return ciphertext


def decrypt(ciphertext: str, key: int) -> str:
    """
    Decryption with the Shift cipher.

    Parameters:
        ciphertext (str): Ciphertext to decrypt
        key (int): Number of shifts

    Returns:
        str: Plaintext
    """

    plaintext = ""
    for character in plaintext:
        if alphabet.is_letter(character):
            plaintext += alphabet.shift_letter(character, key, True)
        else:
            plaintext += character

    return plaintext

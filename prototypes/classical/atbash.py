import sys
sys.path.insert(0, "../")

import affine

ALPHABET_SIZE = 26


def encrypt(plaintext: str) -> str:
    """
    Encrypt a text using the Atbash cipher.

    Parameters:
        plaintext (str): The plaintext to encrypt

    Returns:
        str: The resulting ciphertext
    """

    return affine.encrypt(plaintext, ALPHABET_SIZE - 1, ALPHABET_SIZE - 1)


def decrypt(ciphertext: str) -> str:
    """
    Decrypt a text using the Atbash cipher.

    Parameters:
        ciphertext (str): The ciphertext to decrypt

    Returns:
        str: The resulting plaintext
    """

    return affine.decrypt(ciphertext, ALPHABET_SIZE - 1, ALPHABET_SIZE - 1)

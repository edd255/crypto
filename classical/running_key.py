"""
Implementation of the running key cipher.
"""

from utils import alphabet


def encrypt(plaintext: str, key: str) -> str:
    """
    Encrypt a text using the running key cipher.

    Parameters:
        text (str): The plaintext to encrypt
        key (str): The key to use for the encryption

    Returns:
        str: The resulting ciphertext
    """

    if len(plaintext) != len(key):
        raise ValueError("key length does not match plaintext length")

    ciphertext = ""
    for character, key_character in zip(plaintext, key):
        if alphabet.is_letter(character):
            ciphertext += alphabet.shift_letter(
                character, alphabet.letter_to_position(key_character), True
            )
        else:
            ciphertext += character

    return ciphertext


def decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypt a text using the running key cipher.

    Parameters:
        text (str): The ciphertext to decrypt
        key (str): The key to use for the decryption

    Returns:
        str: The resulting plaintext
    """

    if len(ciphertext) != len(key):
        raise ValueError("key length does not match ciphertext length")

    plaintext = ""
    for character, key_character in zip(ciphertext, key):
        if alphabet.is_letter(character):
            plaintext += alphabet.shift_letter(
                character, alphabet.letter_to_position(key_character), False
            )
        else:
            plaintext += character

    return plaintext

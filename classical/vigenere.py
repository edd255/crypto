"""
An implementation of the Vigenère cipher.
"""


from utils import alphabet


def lengthen_key(text: str, key: str) -> str:
    """
    Adjusts the key length to the text length, if the text is longer than the
    key.

    Parameters:
        text (str): text to encrypt
        key (str): key that is used for the encryption

    Returns:
        str: a key that is as long as the text
    """

    if len(text) > len(key):
        fac = len(text) // len(key)
        res = len(text) % len(key)
        key = fac * key + key[:res]

    return key


def encrypt(plaintext: str, key: str) -> str:
    """
    Encrypt a text using the Vigenere cipher.

    Parameters:
        text (str): The plaintext to encrypt
        key (str): The key to use for the encryption

    Returns:
        str: The resulting ciphertext
    """

    ciphertext = ""
    key = lengthen_key(plaintext, key)
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
    Decrypt a text using the Vigenere cipher.

    Parameters:
        text (str): The ciphertext to decrypt
        key (str): The key to use for the decryption

    Returns:
        str: The resulting plaintext
    """

    plaintext = ""
    key = lengthen_key(ciphertext, key)
    for character, key_character in zip(ciphertext, key):
        if alphabet.is_letter(character):
            plaintext += alphabet.shift_letter(
                character, alphabet.letter_to_position(key_character), False
            )
        else:
            plaintext += character

    return plaintext

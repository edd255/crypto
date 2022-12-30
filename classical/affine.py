from utils import maths
from utils import alphabet

ALPHABET_SIZE = 26


def encrypt(plaintext: str, a: int, b: int) -> str:
    """
    Encrypt a text using the Affine cipher.

    Parameters:
        plaintext (str): The plaintext to encrypt
        a (str): Key coefficient
        b (str): Key summand

    Returns:
        str: The resulting ciphertext
    """

    if maths.gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError("a and the alphabet size are not coprime")

    ciphertext = ""
    for character in plaintext:
        if alphabet.is_letter(character):
            x = alphabet.letter_to_position(character)
            ciphertext += alphabet.position_to_letter(
                (a * x + b) % ALPHABET_SIZE, alphabet.is_lowercase(character)
            )
        else:
            ciphertext += character

    return ciphertext


def decrypt(ciphertext: str, a: int, b: int) -> str:
    """
    Decrypt a text using the Affine cipher.

    Parameters:
        ciphertext (str): The ciphertext to decrypt
        a (str): Key coefficient
        b (str): Key summand

    Returns:
        str: The resulting plaintext
    """

    (gcd, inv_a, _) = maths.extended_euclidean_algorithm(a, ALPHABET_SIZE)
    if gcd != 1:
        raise ValueError("a and alphabet size are not coprime")

    plaintext = ""
    for character in plaintext:
        if alphabet.is_letter(character):
            x = alphabet.letter_to_position(character)
            plaintext += alphabet.position_to_letter(
                inv_a * (x - b) % ALPHABET_SIZE, alphabet.is_lowercase(character)
            )
        else:
            plaintext += character

    return plaintext

ALPHABET_SIZE = 26


def is_letter(character: str) -> bool:
    """
    Checks if a character is a letter.

    Parameters:
        character (str): The character to check

    Returns:
        bool: True if the character is a letter, else False
    """

    return is_lowercase(character) or is_uppercase(character)


def is_lowercase(letter: str) -> bool:
    """
    Checks if a letter is lowercase.

    Parameters:
        letter (str): The letter to check

    Returns:
        bool: True if the letter is lowercase, else False
    """

    return 97 <= ord(letter) <= 122


def is_uppercase(letter: str) -> bool:
    """
    Checks if a letter is uppercase.

    Parameters:
        letter (str): The letter to check

    Returns:
        bool: True if the letter is uppercase, else False
    """

    return 65 <= ord(letter) <= 90


def letter_to_position(letter: str) -> int:
    """
    Gives the position of the letter in the alphabet.

    Parameters:
        letter (str): The letter to get the position from

    Returns:
        int: The position of the letter in the alphabet
    """

    if is_lowercase(letter):
        return ord(letter) - 97
    else:
        return ord(letter) - 65


def position_to_letter(position: int, lowercase: bool) -> str:
    """
    Returns a lowercase/uppercase letter with the corresponding position.

    Parameters:
        position (int): Position of the letter
        lowercase (bool): Indicator whether the returned letter should be lowercase

    Returns:
    """

    if lowercase:
        return chr(position + ord("a"))
    else:
        return chr(position + ord("A"))


def shift_letter(character: str, key: int, add: bool) -> str:
    """
    Shifts a letter by 'key' positions.

    Parameters:
        character (str): The letter to shift
        key (int): The positions to shift by
        add (bool): A boolean value to indicate whether to add or subtract

    Returns:
        str: The letter shifted by 'key' positions to the right/left, or the given character if it's not a letter
    """

    if is_letter(character) is False:
        return character

    if add:
        shifted_letter = (letter_to_position(character) + key) % ALPHABET_SIZE
    else:
        shifted_letter = (letter_to_position(character) - key) % ALPHABET_SIZE

    if is_lowercase(character):
        shifted_letter += ord("a")
    else:
        shifted_letter += ord("A")

    return chr(shifted_letter)

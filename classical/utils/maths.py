"""
Useful math functions.
"""


def gcd(a: int, b: int) -> int:
    """
    Computes the greatest common divisor of a and b.

    Source:
        https://en.wikipedia.org/wiki/Euclidean_algorithm

    Parameters:
        a (int): An arbitrarily chosen integer
        b (int): An arbitrarily chosen integer

    Returns:
        int: The greatest common divisor of a and b.
    """

    while b != 0:
        t = b
        b = a % b
        a = t

    return a


def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int, int]:
    """
    Computes the greatest common divisor of a and b as well as their Bézout
    coefficients.

    Source:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

    Parameters:
        a (int): An arbitrarily chosen integer
        b (int): An arbitrarily chosen integer

    Returns:
        tuple[int, int, int]: The greatest common divisor of a and b, the Bézout coefficient of a, the Bézout coefficient of b
    """

    (old_g, g) = (a, b)
    (old_x, x) = (1, 0)
    (old_y, y) = (0, 1)

    while g != 0:
        q = old_g // g
        (old_g, g) = (g, old_g - q * g)
        (old_x, x) = (x, old_x - q * x)
        (old_y, y) = (y, old_y - q * y)

    return (old_g, old_x, old_y)

from abc import ABC

from fractions import Fraction

LEAST_SIMPLE_INTEGER = -10 * 1000
GREATEST_SIMPLE_INTEGER = 10 * 1000

RATIONAL_DENOMINATOR = 1441440

class PossibleSimple(ABC):
    """
    A marker interface for numbers that might or might not be simple.

    Simple means having a compact description and is used, for instance,
    to determine whether to write the repr of the object itself in an exception or not.
    """

    def is_simple(self):
        raise NotImplemented("is_simple method is abstract")


def quantity_is_simple(x):
    """
    >>> quantity_is_simple(4)
    True
    >>> quantity_is_simple(1 + 10 * 1000)
    False
    """
    if isinstance(x, int):
        return LEAST_SIMPLE_INTEGER <= x <= GREATEST_SIMPLE_INTEGER
    elif isinstance(x, float):
        return False
    elif isinstance(x, Fraction):
        return quantity_is_simple(x.numerator) and quantity_is_simple(x.denominator)
    else:
        return x.is_simple()


def quantity_lowerbound(x):
    """
    >>> quantity_lowerbound(0)
    0
    """
    if isinstance(x, int):
        return x
    elif isinstance(x, float):
        return x
    elif isinstance(x, Fraction):
        return x
    else:
        return x.lowerbound()


def quantity_minimum(it):
    """
    >>> quantity_minimum([1, 2, 3])
    1
    """
    return min(quantity_lowerbound(x) for x in it)


def quantity_upperbound(x):
    """
    >>> quantity_lowerbound(0)
    0
    """
    if isinstance(x, int):
        return x
    elif isinstance(x, float):
        return x
    elif isinstance(x, Fraction):
        return x
    else:
        return x.upperbound()


def quantity_maximum(it):
    """
    >>> quantity_maximum([1, 2, 3])
    3
    """
    return max(quantity_upperbound(x) for x in it)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

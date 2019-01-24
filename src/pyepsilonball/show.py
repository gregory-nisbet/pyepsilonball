# Python library for rational interval arithmetic
#
# Provide a few dedicated interval types
# that form an arithmetic hierarchy on their own
#

from fractions import Fraction


def show_fraction(frac):
    """
    >>> show_fraction(Fraction(2, 1))
    '2'
    >>> show_fraction(Fraction(4, 7))
    'Fraction(4, 7)'
    >>> show_fraction(Fraction(-4, 5))
    'Fraction(-4, 5)'
    >>> show_fraction(Fraction(4, -5))
    'Fraction(-4, 5)'
    """
    if frac.denominator == 1:
        return repr(frac.numerator)
    else:
        return repr(frac)


def show_compact_fraction(frac):
    """
    >>> show_compact_fraction(Fraction(2, 1))
    '2'
    >>> show_compact_fraction(Fraction(-2, 1))
    '-2'
    >>> show_compact_fraction(Fraction(1, 2))
    '1/2'
    >>> show_compact_fraction(Fraction(-4, 5))
    '(-4)/5'
    >>> show_compact_fraction(Fraction(4, -5))
    '(-4)/5'
    """
    if frac.denominator == 1:
        if frac.numerator >= 0:
            return repr(frac.numerator)
        else:
            return "%s" % repr(frac.numerator)
    else:
        if frac.numerator >= 0:
            return "%s/%s" % (repr(frac.numerator), repr(frac.denominator))
        else:
            return "(%s)/%s" % (repr(frac.numerator), repr(frac.denominator))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

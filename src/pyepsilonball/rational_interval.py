# Python library for rational interval arithmetic
#
# Provide a few dedicated interval types
# that form an arithmetic hierarchy on their own
#

from fractions import Fraction


from baseclasses import *
from show import *


class RationalInterval(object):
    """
    An interval of rational numbers
    """

    def __init__(self, *args):
        if len(args) == 0:
            self.low = Fraction(0)
            self.high = Fraction(0)
        else:
            self.low = quantity_minimum(args)
            self.high = quantity_maximum(args)

    def __repr__(self):
        reprargs = (show_compact_fraction(self.low), show_compact_fraction(self.high))
        return "[%s, %s]" % reprargs

    def __contains__(self, item):
        return (self.low <= item) and (item <= self.high)

    def __add__(self, other):
        return RationalInterval(self.low + other.low, self.high + other.high)

    def __mul__(self, other):
        a, b = self.low, self.high
        c, d = other.low, other.high
        lyst = [a * c, a * d, b * c, b * d]
        return RationalInterval(min(lyst), max(lyst))

    def negate(self):
        return RationalInterval(-self.high, -self.low)

    def __sub__(self, other):
        return self + other.negate()

    def reciprocal(self):
        if 0 in self:
            if self.is_simple():
                raise ZeroDivisionError("%s contains zero." % self)
            else:
                raise ZeroDivisionError("interval contains zero.")
        else:
            return RationalInterval(1 / self.high, 1 / self.low)

    def __truediv__(self, other):
        return self * other.reciprocal()

    def is_simple(self):
        return quantity_is_simple(self.low) and quantity_is_simple(self.high)

    def lowerbound(self):
        return self.low

    def upperbound(self):
        return self.high


if __name__ == "__main__":
    import doctest

    class TestRationalInterval:
        """
        >>> RationalInterval(4, 5)
        [4, 5]

        >>> RationalInterval(Fraction(1, 2), Fraction(3, 4))
        [1/2, 3/4]

        >>> Fraction(3, 5) in RationalInterval(Fraction(1, 2), Fraction(3, 4))
        True

        >>> RationalInterval(1, 2) + RationalInterval(1, 3)
        [2, 5]

        >>> RationalInterval(1, 2) * RationalInterval(1, 3)
        [1, 6]

        >>> RationalInterval(1, 2) - RationalInterval(1, 2)
        [-1, 1]

        >>> RationalInterval(-4, 4) / RationalInterval(2, 2)
        [-2, 2]

        >>> RationalInterval(1, 1) / RationalInterval(-2, 2)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: [-2, 2] contains zero.

        A RationalInterval made out of RationalIntervals should collapse

        >>> RationalInterval(RationalInterval(1, 3), RationalInterval(2, 3))
        [1, 4]
        """

        pass

    doctest.testmod()

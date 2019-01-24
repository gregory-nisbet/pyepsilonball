from rational_interval import *


class RationalIntervalSeq(object):
    """
    """

    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError("no default RationalIntervalSeq")
        elif len(args) == 1:
            # TODO: probably use new instead
            if isinstance(args[0], RationalIntervalSeq):
                self.func = args[0].func
            else:
                self.func = args[0]
        else:
            raise ValueError("too many arguments")

    def get(self, idx):
        return self.func(idx)

    def __repr__(self):
        return "(%s, %s, %s, ...)" % (self.get(1), self.get(2), self.get(3))


if __name__ == "__main__":

    class TestRationalIntervalSeq:
        """
        >>> RationalIntervalSeq(lambda n : RationalInterval(n, n)).get(1)
        [1, 1]
        >>> RationalIntervalSeq(lambda n : RationalInterval(n, n))
        ([1, 1], [2, 2], [3, 3], ...)
        """

        pass

    import doctest

    doctest.testmod()

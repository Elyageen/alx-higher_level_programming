#!/usr/bin/python3
"""Defines an integer addition function.
# Th# The `add_integer` function takes two arguments `a` and `b`, with `b` having a default value of
# 98. It returns the integer addition of `a` and `b` after typecasting any float arguments to
e `add_integer` function takes two arguments `a` and `b`, with a default value of 98 for `b`.
# It returns the integer addition of `a` and `b`. If either `a` or `b` is a float, they are
# typecasted to integers before the addition is performed. If either `a` or `b` is not an integer  or a float, a `TypeError` is raised.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

#!/usr/bin/python3

def add_integer(a, b=98):
    """
    add two integers

    Args:
        a (int): integer 1
        b (int): integer 2

    Raises:
        TypeError: Exception if size is not an integer

    """
    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.7976931348623158e+308:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float and b == b and abs(b) <= 1.7976931348623158e+308:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b

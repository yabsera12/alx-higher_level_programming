#!/usr/bin/python3



def is_kind_of_class(obj, a_class):
    """
        function that returns True if the object is an instance of, or 
        if the object is an instance of 
        a class that inherited from, the specified class ; otherwise False.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False

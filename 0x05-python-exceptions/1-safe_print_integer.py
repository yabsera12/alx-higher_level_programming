#!/usr/bin/python3
def safe_print_integer(value):
    iserror = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        iserror = False
    return iserror

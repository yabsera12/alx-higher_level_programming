#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    isint = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as eror:
        isint = False
        sys.stderr.write("Exception: {}\n".format(eror))

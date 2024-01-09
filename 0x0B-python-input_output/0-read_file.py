#!/usr/bin/python3


def read_file(filename=""):
    """
    Reads text file and prints to STDOUT
    """

    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")

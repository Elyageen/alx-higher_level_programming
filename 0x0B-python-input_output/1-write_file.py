#!/usr/bin/python3
""" function that write a text file (UTF8) and prints it to stdout """


def write_file(filename="", text=""):
    """ function that write a text file (UTF8) and prints it to stdout """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

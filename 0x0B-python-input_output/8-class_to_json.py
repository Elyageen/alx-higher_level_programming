#!/usr/bin/python3
""" function that returns the dictionary description"""


def class_to_json(obj):
    """ function that returns the dictionary description"""
    return obj.__dict__.copy() if hasattr(obj, "__dict__") else {}

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    items_str = [str(x) for x in items]
    for i in range(len(items_str)):
        if str(items_str[i]) in frequencies.keys():
            frequencies[items_str[i]] = frequencies[items_str[i]] + 1
        else:
            frequencies[items_str[i]] = 1
    return frequencies

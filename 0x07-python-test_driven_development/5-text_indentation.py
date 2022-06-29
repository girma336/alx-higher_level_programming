#!/usr/bin/python3
"""Text indentations"""


def text_indentation(text):
    """Prints a text with 2 new lines
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

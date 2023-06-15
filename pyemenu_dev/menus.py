"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next functions:
    0. clear  : Clean the screen
    1. menu() : Easy customizable menu for CLI

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
# Global libraries
import os
from readchar import key, readkey
# Local Libraries
from .tools import *
from .texts import Text
from .titles import Title

class menu():
    '''
    This class allow to create an simple option list for selecting
    one option from a list of options
    '''
    def __init__(self, options: list,
                 title: str = '',

                 ):
        self.options = options
        self.title = title


# Print title for menu in CLI
def print_title(title, sep='-', position='center',  cursor='-->', options=[], col=1):
    if options!=[]:
        max_len_string = len(max(options, key=len))
    else:
        max_len_string = 0

    if position == 'center':
        number_chars = (len(cursor) + max_len_string + 1)*col
        print(f"{title:{sep}^{number_chars}}")
    if position == 'left':
        number_chars = (len(cursor) + max_len_string + 1)*col
        print(f"{title:{sep}<{number_chars}}")
    if position == 'right':
        number_chars = (len(cursor) + max_len_string + 1)*col
        print(f"{title:{sep}>{number_chars}}")


# Print options for menu in CLI
def print_options(options, col, position, cursor):
    max_len_option = len(max(options, key = len))
    for option in options:
        if options.index(option) % col == 0:
            print("")
        if position == options.index(option):
            print(f" {cursor} {option}"+f"{(max_len_option-len(option))*' '}", end="")
        else:
            print(f" {' '*(len(cursor)+1)}"+f"{option}"+f"{(max_len_option-len(option))*' '}", end="")

# Print interactive menu in CLI
def menu(title: str, options: list, col: int = 1, cursor: str = "=>"):
    """
    Easy customizable menu for CLI

    return the index option 
    or 
    return None if 'q' is press
    ______________________________

    Attributes:
    title   ->   str
        Title to be prompt at the top
    options ->   list
        Must be a list with the options
    col     ->   int
        Number of columns of how the options want to be arranged
        by default = 1
    cursor  ->   str
        Chars for representing the cursor
        by default = =>
    """
    options = validate_options(options)
    position = 0
    while True:
        clear()
        print_title(title, options, col, cursor)
        print_options(options, col, position, cursor)
        key = input_key()
        position = validate_position(cursor_position(key, position, col), options)
        if key in ["q", "Q"]:
            return None 
        if key == ENTER:
            return options[position]

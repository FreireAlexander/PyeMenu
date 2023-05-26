"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next functions:
    1. menu() : Easy customizable menu for CLI

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
#Libraries
import os
from readchar import key, readkey

## Global Variables
# Keyboard Values
ENTER = key.ENTER
UP = key.UP
DOWN = key.DOWN
LEFT = key.LEFT
RIGHT = key.RIGHT

# Os.clear functions
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# input key
def input_key():
    print(f"\n\n Press ENTER to select an option")
    print(f" Press (q) to exit")
    return readkey()

# Validate type of parameters for the list of choices
def validate_options(options):
    if type(options) != type([]):
        raise TypeError("Options must be a list")
    if len(options) == 0:
        raise ValueError("Options must contains more than zero values")
    
    return list(map(lambda x: str(x), options))

# Validate minimun and maximun value of position in list
def validate_position(position, options):
    if position < 0:
        return 0
    if position > len(options) - 1:
        return len(options) - 1
    
    return position

# Cursor position on menu as table
def cursor_position(key, position, col):
    if key == UP:
        position -=col
    if key == DOWN:
        position +=col
    if key == LEFT:
        position -=1
    if key == RIGHT:
        position +=1

    return position

# Print title for menu in CLI
def print_title(title, options, col, cursor):
    max_len_string = len(max(options, key=len))
    len_title_frame = ((len(cursor) + max_len_string + 1)*col - len(title))//2
    print(f"{len_title_frame*'_'} "+f"{title}"+f" {len_title_frame*'_'}")

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

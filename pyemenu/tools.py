"""
    This module provide specific tools for generate menus
    this module contain the next functions:
    0. clear  : Clean the screen

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
SPACE = key.SPACE

# Os.clear functions
def clear():
    """
    Clean windows screen
    """
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
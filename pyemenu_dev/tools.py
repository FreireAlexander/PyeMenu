"""
    This module provide specific tools for generate menus
    this module contain the next functions:
    0. clear_screen  : Clean the screen
    1. keyboard : read key pressed

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
#Libraries
import os
from readchar import key, readkey

## Global Variables
# Keyboard Values
ENTER   = key.ENTER
UP      = key.UP
DOWN    = key.DOWN
LEFT    = key.LEFT
RIGHT   = key.RIGHT
SPACE   = key.SPACE
input_info = """Press ENTER to select an option"""
input_exit = """Press (q) to exit"""

# Os.clear functions
def clear_screen():
    """
    Clean windows screen
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# input key
def getKeyboard(info:str=input_info, exit_message:str=input_exit):
    """
    This Function read the key press from user
    Also Allow to introduce an info messages and
    an exit message, by default:
    info = Press ENTER to select an option}
    exit_message = Press (q) to exit
    params
    info: str -> information of keyboard functions for the user 
    exit_message: str -> information of keyboard input to exit for the user
    """
    print(f"\n\n{info}")
    print(f"{exit_message}")
    return readkey()

def setCursor(keyboard, pointer: int, options: list, wrap: int):
    """
    This Function allow to place the cursor into a block,
    but it requires
    params
    keyboard: readkey() -> the input from the keyboard
    pointer:    int -> Pointer index where the cursor is placed
    options:  list -> the list of elements in the block
    wrap:     int -> the number of columns of how elements are wrapped
    """
    previous_pointer = pointer
    if keyboard == UP:    pointer -=wrap
    if keyboard == DOWN:  pointer +=wrap
    if keyboard == LEFT:  pointer -=1
    if keyboard == RIGHT: pointer +=1
    if pointer < 0: pointer = previous_pointer
    if previous_pointer > len(options) - 1: pointer = 0
    if pointer > len(options) - 1: pointer = previous_pointer
    
    return pointer
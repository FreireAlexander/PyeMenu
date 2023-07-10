"""
    This module provide specific tools for generate menus
    this module contain the next functions:
    0. clear_screen  : Clean the screen
    1. getKeyboard : read key pressed

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*

    PyeMenu version 1.0.1
"""
#Libraries
import os
from os import get_terminal_size
from readchar import key, readkey
from .components import Text, Title

## Global Variables
# Keyboard Values
ENTER   = key.ENTER
UP      = key.UP
DOWN    = key.DOWN
LEFT    = key.LEFT
RIGHT   = key.RIGHT
SPACE   = key.SPACE
input_info = """
    Press ENTER to select an option"""
input_exit = """
    Press (q) or (Q) to exit"""

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
    print(f"{info}", end="")
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

def resize_screen(wrap, block_width):
    """
    This method is for resizing the screen when widgets are print or show
    """
    cols, rows = get_terminal_size()
    while block_width*wrap>cols:
        wrap -=1       
    if wrap <0:
        wrap = 1
    return wrap

def print_title(widget, title_align, title_decorator, 
                block_width, wrap, title_padding_up, title_padding_bottom):
    """
    This method is for print the title in widgets
    """
    if widget.title.text != '':
        widget.title.print_title(title_align, title_decorator, 
                    (block_width)*wrap, 
                    title_padding_up, 
                    title_padding_bottom)

def print_logo(logo):
    """
    This method is for print the logo above widgets
    """
    if type(logo) in [type(Text("")), type(Title(""))]:
        print(f"{logo.styled}")
    elif str(logo):
        logo = Text(str(logo))
        print(f"{logo.styled}")
    else:
        pass

def fill_empty_blocks(self, empty_blocks, block_width):
    """
    This method is for fill empty spaces in widgets when it prints
    """
    if empty_blocks != 0:
        for i in range(empty_blocks):
            print(f"{self.bg_rgb}{((block_width))*' '}", end='')


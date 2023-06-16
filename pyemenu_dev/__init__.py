"""
    This Packages has a lot of tools for create Minimalist Text User Interface, 
    its allow foreground colors and background colors but depends of the terminal 
    used, by now It was tested succesfully in LINUX Terminals and Windows but just 
    when terminal.exe it is used
    Basic Elements as: 
        1. Text()
        2. Title()
    Basic Blocks as:
        1. Menu()
"""
from .tools import clear_screen, getKeyboard, setCursor
from .tools import ENTER, UP, DOWN, LEFT, RIGHT, SPACE
from .colors import Colors, html_rgb_fg, html_rgb_bg
from .texts import Text
from .titles import Title
from .menus import Menu
from .checkboxlists import Checkboxlist
from .forms import Form
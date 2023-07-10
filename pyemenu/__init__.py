"""
    A simple framework for develop simple and really easy Text User Interface, 
    You can Count with this elements:
    1. Components. These are used inside the widgets, these are:
        1. Text
        2. Title
        3. Checkbox
        4. Entry
        5. Button
    2. Widgets. These could be use to get information and data
        1. Menu -> For just one selection Menu
        2. Checkboxlist -> For a checkbox list with boolean choice
        3. Form -> A Simple widget to create Forms
    there are also a set of tools that can be use into your TUI as
        1. clear_screen() -> For cleaning the entire screen
        2. getKeyboard    -> For getting the input keyboard from user
        3. setCursor      -> For setting up the cursor position in a list
    Also, this package contain an special Class call Colors
        1. Colors -> A class with a lot of colors in hexadecimal format
    
    This package was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*

    PyeMenu version 1.0.0
"""
from .components import Text, Title, Entry, Button, Checkbox
from .widgets import Menu, Checkboxlist, Form
from .tools import clear_screen, getKeyboard
from .colors import Colors



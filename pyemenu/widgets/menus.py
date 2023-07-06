"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next Class:
    Menu() for create simple and easy useful Menu 

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
# Local Libraries
import math
from readchar import key
from ..components import Text
from ..components import Title
from ..colors import Colors, setColor
from ..tools import setCursor, getKeyboard, clear_screen, resize_screen
from ..tools import print_title, fill_empty_blocks
from readchar import key


nf = '\x1b[0m'
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'
input_info = """
    Press Enter to select and option or
    Press q to exit without select any option
"""

class Menu():
    '''
    This class allow to create an simple option list for selecting
    one option from a list of options.
    The parameters to initialize the class are:
        options: List -> List of labels for been selected 
        title: str or Text object -> The text title to be printed up the menu
        cursor: str or Text object -> The char/s that represent the cursor
        fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        bg: str -> A color in hexadecimal, much of colors could be found in Colors class
    Some of the properties of this class are:
        selected -> return the selected value from the list
    For Show this menu it should be use the print() method.
    '''
    def __init__(self, options: list, 
                title: str = '', cursor: str = '-->',
                fg: str = not_fg, bg: str = not_bg):
        self.options = [Text(str(option)) if type(option)!=type(Text('')) else option for option in options]
        self.max_len_option = max(self.options, key = lambda x: x.lenght).lenght
        title.width = self.max_len_option
        self.title = title
        self.cursor = cursor
        self.fg = fg
        self.fg_rgb = '\x1b[38;'+setColor(fg)
        self.bg = bg
        self.bg_rgb = '\x1b[48;'+setColor(bg)
        self.selected = Text('Vacio')
        self.cursor = Text.setText(self, cursor)
        self.title = Title.setTitle(self, title)

        self.options = []
        for option in options:
            if type(option) != type(Text('')):
                option = Text(str(option), fg=fg, bg=bg)
            if type(option) == type(Text('')) and option.bg == not_bg and option.fg != not_fg:
                option = Text(option.text, bg=bg, fg=option.fg)
            if type(option) == type(Text('')) and option.fg == not_fg and option.bg != not_bg:
                option = Text(option.text, fg=fg, bg=option.bg)
            if type(option) == type(Text('')) and option.fg == not_fg and option.bg == not_bg:
                option = Text(option.text, fg=fg, bg=bg)
            
            self.options.append(option)

    def print(self,
            wrap: int=1,
            highlight: bool = False,
            fg_hl = Colors.Azure,
            bg_hl = Colors.Navy, 
            title_decorator: str= ' ',
            title_align: str='center',
            padding_up: bool = False,
            padding_bottom: bool = False, 
            title_padding_up: bool = False,
            title_padding_bottom: bool = False
            ):
        """
        This Method allow a Menu to be show on screen
        Return a string with the selected value or None
        parameters:
            wrap: int -> how elements into options are wrapped
            highlight: bool = False,
            fg_hl -> foreground color for highlight current option
            bg_hl -> background color for highlight current option
            title_align: str -> 'center', 'right' or 'left'
            title_decorator: str -> just one char to print around Title text
            padding_up: bool = False -> add a new line above title
            padding_bottom: bool = False -> add a new line behind title
            title_padding_up: bool = False -> add a new line above title
            title_padding_bottom: bool = False -> add a new line behind title
        """
        pointer = 0
        selected = None
        keyboard = None
        while True:
            clear_screen()
            block_width = 4+self.cursor.lenght+self.max_len_option
            wrap = resize_screen(wrap, block_width)
            if padding_up:
                print(f"{self.bg_rgb}{((block_width)*wrap)*' '}")
            print_title(self, title_align, title_decorator, 
                        block_width, wrap, title_padding_up, 
                        title_padding_bottom)
            for option in self.options:
                if self.options.index(option) % wrap == 0:
                    print("")
                if pointer == self.options.index(option):
                    self.selected = option.text
                    if keyboard == key.ENTER:
                        self.selected = option.text
                    if highlight:
                        op_hl = Text(option.text, fg=fg_hl, bg=bg_hl)
                        print(
                            f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                            +f"{op_hl.bg_rgb} {op_hl.styled}{op_hl.bg_rgb} "\
                            +f"{(self.max_len_option-len(option.text))*' '}", 
                            end="")
                    else:
                        print(
                            f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "
                            +f"{option.bg_rgb} {option.styled}{option.bg_rgb} "\
                            +f"{(self.max_len_option-len(option.text))*' '}", 
                            end="")
                else:
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.lenght*' '}{self.cursor.bg_rgb} "\
                        +f"{option.bg_rgb} {option.styled}{option.bg_rgb} "\
                        +f"{(self.max_len_option-len(option.text))*' '}", 
                        end="")
            empty_blocks = int(math.ceil(len(self.options)/wrap)*wrap)-len(self.options)
            fill_empty_blocks(self, empty_blocks, block_width)
            if padding_bottom:
                print(f"\n{self.bg_rgb}{(block_width*wrap)*' '}", end='')
            print(f"{nf}")

            keyboard = getKeyboard()
            pointer = setCursor(keyboard, pointer, self.options, wrap)
            if keyboard in ["q", "Q"]:
                self.selected = None
                return self.selected
            if keyboard == key.ENTER:
                return self.selected
            

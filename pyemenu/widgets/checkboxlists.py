"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next Class:
    Checkboxlist() for create simple and easy useful Menu 

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
        
    PyeMenu version 1.0.0
"""
# Locals
from ..components import Text, Title, Checkbox
from ..colors import Colors, setColor
from ..tools import setCursor, getKeyboard, clear_screen, resize_screen
from ..tools import print_title, fill_empty_blocks, print_logo
# External
import math
from readchar import key


nf = '\x1b[0m'
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'
input_info = """
    Press Space to select or unselect an option
    Press Enter to exit and return the choice/s"""

class Checkboxlist():
    '''
    This class allow to create an simple option list for selecting
    one option from a list of options.
    The parameters to initialize the class are:
        options: List -> List of labels for been selected
        multiselect: bool -> Allow multiple choices by default it is True
        title: str or Text object -> The text title to be printed up the menu
        cursor: str or Text object -> The char/s that represent the cursor
        fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        bg: str -> A color in hexadecimal, much of colors could be found in Colors class
    Some of the properties of this class are:
        answer -> return the selected value from the list
    For Show this Checkboxlist it should be use the print() method. 
    '''
    def __init__(self, options: list,
                multiselect: bool = True, 
                title: str = '', cursor: str = '-->',
                fg: str = not_fg, bg: str = not_bg):
        self.multiselect = multiselect
        __options = [option if type(option)==type(Text('')) else Checkbox(str(option)) for option in options]
        self.max_len_option = len(max(__options, key = lambda x: x.lenght).text)
        title.width = self.max_len_option
        self.title = title
        self.cursor = cursor
        self.fg = fg
        self.fg_rgb = '\x1b[38;'+setColor(fg)
        self.bg = bg
        self.bg_rgb = '\x1b[48;'+setColor(bg)
        self.answer = []
        self.cursor = Text.setText(self, cursor)
        self.title = Title.setTitle(self, title)
        self.options = self.setOptions(options)
        
    def print(self,
            wrap: int=1,
            highlight: bool = True,
            fg_hl = Colors.white,
            bg_hl = Colors.Lime, 
            title_decorator: str= ' ',
            title_align: str='center',
            padding_up: bool = False,
            padding_bottom: bool = False, 
            title_padding_up: bool = False,
            title_padding_bottom: bool = False,
            logo: str = ''
            ):
        """
        This Method allow a Checkboxlist to be show on screen
        Return a string with the selected values or None
        parameters:
            wrap: int -> how elements into options are wrapped
            highlight: bool -> True by default
            fg_hl -> foreground color for highlight current option
            bg_hl -> background color for highlight current option
            title_align: str -> 'center', 'right' or 'left'
            title_decorator: str -> just one char to print around Title text
            padding_up: bool = False -> add a new line above title
            padding_bottom: bool = False -> add a new line behind title
            title_padding_up: bool = False -> add a new line above title
            title_padding_bottom: bool = False -> add a new line behind title
            logo: str -> This parameter allow to print a logo or an extra title 
                above the Form print
        """
        pointer = 0
        self.answer = []
        keyboard = None
        while True:
            clear_screen()
            block_width = 9+self.cursor.lenght+self.max_len_option
            wrap = resize_screen(wrap, block_width)
            print_logo(logo)
            if padding_up:
                print(f"{self.bg_rgb}{((block_width)*wrap)*' '}")
            print_title(self, title_align, title_decorator, 
                        block_width, wrap, title_padding_up, 
                        title_padding_bottom)
            if keyboard == key.SPACE:
                if self.multiselect:
                    if self.options[pointer].text not in self.answer:
                        self.options[pointer].onSelect() 
                        self.answer.append(self.options[self.options.index(self.options[pointer])].text)
                    elif self.options[pointer].text in self.answer:
                        self.options[pointer].onSelect()
                        self.answer.remove(self.options[self.options.index(self.options[pointer])].text)
                else:
                    self.options[pointer].onSelect()
                    for other in self.options:
                        if other != self.options[pointer]:
                            other.clear()
                            self.answer = self.options[self.options.index(self.options[pointer])].text
            for option in self.options:
                if self.options.index(option) % wrap == 0:
                    print("")
                if pointer == self.options.index(option):
                    if highlight:
                        it_hl = Checkbox(option.text,  box=option.box,
                                        fg=fg_hl, bg=bg_hl,
                                        bold=option.bold, italic=option.italic, 
                                        underline=option.underline, 
                                        blink=option.blink, reverse=option.reverse, 
                                        crossed=option.crossed)
                        print(
                            f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                            +f"{it_hl.print}{it_hl.bg_rgb}"\
                            +f"{(self.max_len_option-len(option.text))*' '}", 
                            end="")
                    else:
                        print(
                            f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                            +f"{option.print}{option.bg_rgb}"\
                            +f"{(self.max_len_option-len(option.text))*' '}", 
                            end="")    
                else:
                    print(
                        f"{self.cursor.bg_rgb} {' '*(len(self.cursor.text))}{self.cursor.bg_rgb} "\
                        +f"{option.print}{option.bg_rgb}"\
                        +f"{(self.max_len_option-len(option.text))*' '}", 
                        end="")
            empty_blocks = int(math.ceil(len(self.options)/wrap)*wrap)-len(self.options)
            fill_empty_blocks(self, empty_blocks, block_width)
            if padding_bottom:
                print(f"\n{self.bg_rgb}{(block_width*wrap)*' '}")
            print(f"{nf}")
            keyboard = getKeyboard(info=input_info)
            pointer = setCursor(keyboard, pointer, self.options, wrap)
            if keyboard in ["q", "Q"]:
                self.answer = None
                return self.answer
            if keyboard == key.ENTER:
                return self.answer

    def setOptions(self, options):
        list_options = []
        for option in options:
            if type(option) != type(Text('')):
                option = Checkbox(str(option), fg=self.fg, bg=self.bg)
            if type(option) == type(Text('')) and option.bg != not_bg and option.fg != not_fg:
                option = Checkbox(option.text, fg=option.fg, bg=option.bg,
                                bold=option.bold, italic=option.italic, underline=option.underline, 
                                blink=option.blink, reverse=option.reverse, crossed=option.crossed)
            if type(option) == type(Text('')) and option.bg == not_bg and option.fg != not_fg:
                option = Checkbox(option.text, bg=self.bg, fg=option.fg,
                                bold=option.bold, italic=option.italic, underline=option.underline, 
                                blink=option.blink, reverse=option.reverse, crossed=option.crossed)
            if type(option) == type(Text('')) and option.fg == not_fg and option.bg != not_bg:
                option = Checkbox(option.text, fg=self.fg, bg=option.bg,
                                bold=option.bold, italic=option.italic, underline=option.underline, 
                                blink=option.blink, reverse=option.reverse, crossed=option.crossed)
            if type(option) == type(Text('')) and option.fg == not_fg and option.bg == not_bg:
                option = Checkbox(option.text, fg=self.fg, bg=self.bg,
                                bold=option.bold, italic=option.italic, underline=option.underline, 
                                blink=option.blink, reverse=option.reverse, crossed=option.crossed)
            
            list_options.append(option)
        return list_options

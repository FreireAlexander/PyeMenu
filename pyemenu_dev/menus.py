"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next functions:
    1. menu() : Easy customizable menu for CLI

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
# Local Libraries
import math
from readchar import key
from .texts import Text
from .titles import Title
from .colors import Colors, setColor

nf = '\x1b[0m'
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Menu():
    '''
    This class allow to create an simple option list for selecting
    one option from a list of options
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
        if type(cursor) != type(Text('')):
            self.cursor = Text(str(cursor), fg=fg, bg=bg)
        if type(cursor) == type(Text('')) and cursor.bg == not_bg and cursor.fg != not_fg:
            self.cursor = Text(cursor.text, bg=bg, fg=cursor.fg)
        if type(cursor) == type(Text('')) and cursor.fg == not_fg and cursor.bg != not_bg:
            self.cursor = Text(cursor.text, fg=fg, bg=cursor.bg)
        if type(cursor) == type(Text('')) and cursor.fg == not_fg and cursor.bg == not_bg:
            self.cursor = Text(cursor.text, fg=fg, bg=bg)

        if type(title) != type(Title('')):
            self.title = Title(str(title), fg=fg, bg=bg)
        if type(title) == type(Title('')) and title.bg == not_bg and title.fg != not_fg:
            self.title = Title(title.text, bg=bg, fg=title.fg)
        if type(title) == type(Title('')) and title.fg == not_fg and title.bg != not_bg:
            self.title = Title(title.text, fg=fg, bg=title.bg)
        if type(title) == type(Title('')) and title.fg == not_fg and title.bg == not_bg:
            self.title = Title(title.text, fg=fg, bg=bg)

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
            pointer: int = 0,
            keyboard = '',
            wrap: int=1,
            highlight: bool = False,
            fg_hl = Colors.white,
            bg_gl = Colors.Lime, 
            title_decorator: str= '',
            title_align: str='center',
            padding_up: bool = False,
            padding_bottom: bool = False, 
            title_padding_up: bool = False,
            title_padding_bottom: bool = False
            ):
        """
        This Method allow a Menu to be show on screen, it is possible to 
        specifies:
        pointer: int -> location of cursor into the list of options
        keyboard: readkey() -> keyboard input 
        wrap: int -> how elements into options are wrapped
        highlight: bool = False,
        fg_hl -> foreground color for highlight current option
        bg_gl -> background color for highlight current option
        title_align: str -> 'center', 'right' or 'left'
        title_decorator: str -> just one char to print around Title text
        width: int -> width in number of chars
        new_line_up: bool = False -> add a new line above title
        new_line_bottom: bool = False -> add a new line behind title
        """
        block_width = 4+self.cursor.lenght+self.max_len_option
        if padding_up:
            print(f"\n{self.bg}{(block_width*wrap)*' '}")
        if self.title.text != '':
            self.title.print_title(title_align, title_decorator, 
                                    block_width*wrap, 
                                    title_padding_up, 
                                    title_padding_bottom)
        for option in self.options:
            
            if self.options.index(option) % wrap == 0:
                print("")
            if pointer == self.options.index(option):
                self.selected = option
                if keyboard == key.ENTER:
                    self.selected = option
                if highlight:
                    op_hl = Text(option.text, fg=fg_hl, bg=bg_gl)
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.formatted}{self.cursor.bg_rgb} "\
                        +f"{op_hl.bg_rgb} {op_hl.formatted}{op_hl.bg_rgb} "\
                        +f"{(self.max_len_option-len(option.text))*' '}", 
                        end="")
                else:
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.formatted}{self.cursor.bg_rgb} "
                        +f"{option.bg_rgb} {option.formatted}{option.bg_rgb} "\
                        +f"{(self.max_len_option-len(option.text))*' '}", 
                        end="")
                
            else:
                print(
                    f"{self.cursor.bg_rgb} {self.cursor.lenght*' '}{self.cursor.bg_rgb} "\
                    +f"{option.bg_rgb} {option.formatted}{option.bg_rgb} "\
                    +f"{(self.max_len_option-len(option.text))*' '}", 
                    end="")

        empty_blocks = int(math.ceil(len(self.options)/wrap)*wrap)-len(self.options)
        if empty_blocks != 0:
            for i in range(empty_blocks):
                print(f"{self.bg}{(block_width)*' '}", end='')
        if padding_bottom:
            print(f"\n{self.bg}{(block_width*wrap)*' '}")
        print(f"{nf}")

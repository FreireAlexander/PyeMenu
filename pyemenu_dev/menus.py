"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next functions:
    1. menu() : Easy customizable menu for CLI

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
# Local Libraries
from .texts import Text
from .titles import Title
from .colors import Colors, html_rgb_fg, html_rgb_bg

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
        self.options = [Text(str(option), fg=fg, bg=bg) if type(option)!=type(Text('')) else option for option in options]
        self.max_len_option = max(self.options, key = lambda x: x.lenght).lenght
        title.width = self.max_len_option
        self.title = title
        self.cursor = cursor
        if type(cursor) != type(Text('')):
            self.cursor = Text(str(cursor))
        if type(title) != type(Title('')):
            self.title = Title(str(title))

    def print(self,
            pointer: int = 0,
            keyboard = '',
            wrap: int=1,
            highlight: bool = False,
            fg_hl = Colors.white,
            bg_gl = Colors.Lime, 
            title_decorator: str= '',
            title_align: str='center', 
            new_line_up: bool = False,
            new_line_bottom: bool = False
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
        if self.title.text != '':
            self.title.print_title(title_align, title_decorator, 
                (2+self.cursor.lenght+self.max_len_option)*wrap, 
                new_line_up, 
                new_line_bottom)
        for option in self.options:
            if self.options.index(option) % wrap == 0:
                print("")
            if pointer == self.options.index(option):
                if highlight:
                    op_hl = Text(option.text, fg=fg_hl, bg=bg_gl)
                    print(f"{nf}{self.cursor.bg} {self.cursor.formatted}{nf}{op_hl.bg} "\
                        +f"{op_hl.formatted}{html_rgb_bg(bg_gl)}"\
                        +f"{(self.max_len_option-len(option.text))*' '}", end="")
                else:
                    print(f"{nf}{self.cursor.bg} {self.cursor.formatted}{nf}{option.bg} "\
                        +f"{option.formatted}{option.bg}"\
                        +f"{(self.max_len_option-len(option.text))*' '}", end="")
                self.selected = option
            else:
                print(f"{option.bg} {' '*(len(self.cursor.text)+1)}"\
                    +f"{option.formatted}{option.bg}"\
                    +f"{(self.max_len_option-len(option.text))*' '}", end="")

        print(f"{nf}")

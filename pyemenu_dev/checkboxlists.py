"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next functions:
    1. Checkboxlist() : Easy customizable Check Box List for CLI

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
# Local Libraries
import math
from readchar import key, readchar
from .texts import Text
from .titles import Title
from .colors import Colors, setColor

nf = '\x1b[0m'
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Checkboxlist():
    '''
    This class allow to create a CheckBoxList for choice 
    multiple option 
    '''
    def __init__(self, items: list, 
                title: str = '', cursor: str = '-->',
                fg: str = not_fg, bg: str = not_bg):
        __items = [Text(str(item)) if type(item)!=type(Text('')) else item for item in items]
        self.max_len_item = max(__items, key = lambda x: x.lenght).lenght
        title.width = self.max_len_item
        self.title = title
        self.cursor = cursor
        self.fg = fg
        self.fg_rgb = '\x1b[38;'+setColor(fg)
        self.bg = bg
        self.bg_rgb = '\x1b[48;'+setColor(bg)
        self.choices = []
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

        self.items = []
        for item in items:
            if type(item) != type(Text('')):
                item = Text(str(item), fg=fg, bg=bg)
                mark = Text(str(' '), fg=fg, bg=bg)
            if type(item) == type(Text('')) and item.bg == not_bg and item.fg != not_fg:
                item = Text(item.text, bg=bg, fg=item.fg)
                mark = Text(str(' '), fg=item.fg, bg=bg)
            if type(item) == type(Text('')) and item.fg == not_fg and item.bg != not_bg:
                item = Text(item.text, fg=fg, bg=item.bg)
                mark = Text(str(' '), fg=fg, bg=item.bg)
            if type(item) == type(Text('')) and item.fg == not_fg and item.bg == not_bg:
                item = Text(item.text, fg=fg, bg=bg)
                mark = Text(str(' '), fg=fg, bg=bg)
            
            self.items.append([item, mark])

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
        pointer: int -> location of cursor into the list of items
        keyboard: readkey() -> keyboard input 
        wrap: int -> how elements into items are wrapped
        highlight: bool = False,
        fg_hl -> foreground color for highlight current item
        bg_gl -> background color for highlight current item
        title_align: str -> 'center', 'right' or 'left'
        title_decorator: str -> just one char to print around Title text
        width: int -> width in number of chars
        new_line_up: bool = False -> add a new line above title
        new_line_bottom: bool = False -> add a new line behind title
        """
        block_width = 9+self.cursor.lenght+self.max_len_item
        if padding_up:
            print(f"\n{self.bg_rgb}{(block_width*wrap)*' '}")
        if self.title.text != '':
            self.title.print_title(title_align, title_decorator, 
                (block_width)*wrap, 
                title_padding_up, 
                title_padding_bottom)
        for item in self.items:
            if self.items.index(item) % wrap == 0:
                print("")
            if pointer == self.items.index(item):
                if keyboard == key.SPACE:
                    if item[0].text not in self.choices:
                        self.items[self.items.index(item)][1] = Text('*', fg=item[0].fg, bg=item[0].bg)
                        self.choices.append(self.items[self.items.index(item)][0].text)
                    elif item[0].text in self.choices:
                        self.items[self.items.index(item)][1] = Text(' ', fg=item[0].fg, bg=item[0].bg)
                        self.choices.remove(self.items[self.items.index(item)][0].text)

                if highlight:
                    it_hl = Text(item[0].text, fg=fg_hl, bg=bg_gl)
                    mk_hl = Text(item[1].text, fg=fg_hl, bg=bg_gl)
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.formatted}{self.cursor.bg_rgb} "\
                        +f"{it_hl.bg_rgb}{it_hl.fg_rgb} [{mk_hl.formatted}{it_hl.bg_rgb}{it_hl.fg_rgb}] "\
                        +f"{it_hl.bg_rgb} {it_hl.formatted}{it_hl.bg_rgb} "\
                        +f"{(self.max_len_item-len(item[0].text))*' '}", 
                        end="")
                else:
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.formatted}{self.cursor.bg_rgb} "\
                        +f"{item[0].bg_rgb} [{item[1].formatted}{item[0].bg_rgb}] "\
                        +f"{item[0].bg_rgb} {item[0].formatted}{item[0].bg_rgb} "\
                        +f"{(self.max_len_item-len(item[0].text))*' '}", end="")
                
                
            else:
                print(
                    f"{item[0].bg_rgb} {' '*(len(self.cursor.text))}{item[0].bg_rgb} "\
                    +f"{item[1].fg_rgb} [{item[1].formatted}{item[1].fg_rgb}{item[1].bg_rgb}] "\
                    +f"{item[0].bg_rgb} {item[0].formatted}{item[0].bg_rgb} "\
                    +f"{(self.max_len_item-len(item[0].text))*' '}", 
                    end="")

        empty_blocks = int(math.ceil(len(self.items)/wrap)*wrap)-len(self.items)
        if empty_blocks != 0:
            for i in range(empty_blocks):
                print(f"{self.bg_rgb}{block_width*' '}", end='')

        if padding_bottom:
            print(f"\n{self.bg_rgb}{(block_width*wrap)*' '}")
        print(f"")

        print(f"{nf}")
        
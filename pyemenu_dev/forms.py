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
from .tools import clear_screen
from .texts import Text
from .titles import Title
from .colors import Colors, setColor

nf = '\x1b[0m'
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Form():
    '''
    This class allow to create a CheckBoxList for choice 
    multiple option 
    '''
    def __init__(self, entries: list, 
                title: str = '', cursor: str = '-->',
                fg: str = not_fg, bg: str = not_bg):
        __entries = [Text(str(entry)) if type(entry)!=type(Text('')) else entry for entry in entries]
        self.max_len_item = max(__entries, key = lambda x: x.lenght).lenght+1
        title.width = self.max_len_item
        self.title = title
        self.cursor = cursor
        self.fg = fg
        self.fg_rgb = '\x1b[38;'+setColor(fg)
        self.bg = bg
        self.bg_rgb = '\x1b[48;'+setColor(bg)
        self.json = {}
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

        self.entries = []
        for entry in entries:
            if type(entry) != type(Text('')):
                entry = Text(str(entry), fg=fg, bg=bg)
                value = Text(str(' '), fg=fg, bg=bg)
            if type(entry) == type(Text('')) and entry.bg == not_bg and entry.fg != not_fg:
                entry = Text(entry.text, bg=bg, fg=entry.fg)
                value = Text(str(' '), fg=entry.fg, bg=bg)
            if type(entry) == type(Text('')) and entry.fg == not_fg and entry.bg != not_bg:
                entry = Text(entry.text, fg=fg, bg=entry.bg)
                value = Text(str(' '), fg=fg, bg=entry.bg)
            if type(entry) == type(Text('')) and entry.fg == not_fg and entry.bg == not_bg:
                entry = Text(entry.text, fg=fg, bg=bg)
                value = Text(str(' '), fg=fg, bg=bg)
            
            self.json[entry.text] = value.text
            self.entries.append([entry, value])
        
        __values = [Text(str(entry[1].text)) for entry in self.entries]
        self.max_len_values = max(__values, key = lambda x: x.lenght).lenght+1

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
        __values = [Text(str(entry[1].text)) for entry in self.entries]
        self.max_len_values = max(__values, key = lambda x: x.lenght).lenght
        block_width = 7+self.cursor.lenght+self.max_len_item+self.max_len_values
        if keyboard == key.SPACE:
                    clear_screen()
                    print("Type New Value")
                    print(f"Previous Value: {self.entries[pointer][1].formatted}")
                    new_value = input("Input: ")
                    self.entries[pointer][1] = Text(new_value, fg=self.entries[pointer][1].fg, bg=self.entries[pointer][1].bg)
                    self.json[self.entries[pointer][0].text] = new_value
                    clear_screen()
        if padding_up:
            print(f"\n{self.bg_rgb}{((block_width)*wrap)*' '}")
        if self.title.text != '':
            self.title.print_title(title_align, title_decorator, 
                (block_width)*wrap, 
                title_padding_up, 
                title_padding_bottom)
        for item in self.entries:
            if self.entries.index(item) % wrap == 0:
                print("")
            if pointer == self.entries.index(item):
                
                if highlight:
                    it_hl = Text(item[0].text, fg=fg_hl, bg=bg_gl)
                    mk_hl = Text(item[1].text, fg=fg_hl, bg=bg_gl)
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.formatted}{self.cursor.bg_rgb} "\
                        +f"{it_hl.bg_rgb} {it_hl.formatted}{it_hl.bg_rgb} "\
                        +f"{(self.max_len_item-len(item[0].text))*' '}"\
                        +f"{it_hl.fg_rgb}:"\
                        +f"{mk_hl.bg_rgb} {mk_hl.formatted}{mk_hl.bg_rgb} "\
                        +f"{(self.max_len_values-len(item[1].text))*' '}",
                        end="")
                else:
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.formatted}{self.cursor.bg_rgb} "\
                        +f"{item[0].bg_rgb} {item[0].formatted}{item[0].bg_rgb} "\
                        +f"{(self.max_len_item-len(item[0].text))*' '}"\
                        +f"{item[0].fg_rgb}:"\
                        +f"{item[1].bg_rgb} {item[1].formatted}{item[1].bg_rgb} "\
                        +f"{(self.max_len_values-len(item[1].text))*' '}", 
                        end="")
            else:
                print(
                    f"{item[0].bg_rgb} {' '*(len(self.cursor.text))}{item[0].bg_rgb} "\
                    +f"{item[0].bg_rgb} {item[0].formatted}{item[0].bg_rgb} "\
                    +f"{(self.max_len_item-len(item[0].text))*' '}"\
                    +f"{item[0].fg_rgb}:"\
                    +f"{item[1].bg_rgb} {item[1].formatted}{item[1].bg_rgb} "\
                    +f"{(self.max_len_values-len(item[1].text))*' '}", 
                    end="")

        empty_blocks = int(math.ceil(len(self.entries)/wrap)*wrap)-len(self.entries)
        if empty_blocks != 0:
            for i in range(empty_blocks):
                print(f"{self.bg_rgb}{((block_width))*' '}", end='')

        if padding_bottom:
            print(f"\n{self.bg_rgb}{((block_width)*wrap)*' '}")
        
        print(f"{nf}")

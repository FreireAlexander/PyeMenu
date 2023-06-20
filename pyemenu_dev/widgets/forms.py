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
from ..tools import clear_screen
from ..components import Text
from ..components import Title
from ..components import Entry
from ..components import Checkbox
from ..colors import Colors, setColor

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
                fg: str = not_fg, bg: str = not_bg,
                placeholder_fg: str = not_fg, placeholder_bg: str = not_bg):
        
        self.title = title
        self.cursor = cursor
        self.fg = fg
        self.fg_rgb = '\x1b[38;'+setColor(fg)
        self.bg = bg
        self.bg_rgb = '\x1b[48;'+setColor(bg)
        self.survey = {}
        self.placeholder_fg = placeholder_fg
        self.placeholder_bg = placeholder_bg
        if self.placeholder_bg == not_bg and self.placeholder_fg == not_fg:
            self.placeholder_fg = fg
            self.placeholder_bg = bg
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(self.fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(self.bg)
        if self.placeholder_bg != not_bg and self.placeholder_fg == not_fg:
            self.placeholder_fg = fg
            self.placeholder_bg = placeholder_bg
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(self.placeholder_bg)
        if self.placeholder_bg == not_bg and self.placeholder_fg != not_fg:
            self.placeholder_fg = placeholder_fg
            self.placeholder_bg = bg
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(self.placeholder_fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(bg)
        if self.placeholder_bg != not_bg and self.placeholder_fg != not_fg:
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(bg)
        __entries = Form.setEntries(self, entries)
        self.items2 = __entries
        self.max_len_item = max(__entries, key = lambda x: x.lenght).lenght+1
        title.width = self.max_len_item
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
        
        #__values = [Text(str(entry[1].text)) for entry in self.entries]
        #self.max_len_values = max(__values, key = lambda x: x.lenght).lenght+1

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
                    print(f"Previous Value: {self.entries[pointer][1].styled}")
                    new_value = input("Input: ")
                    self.entries[pointer][1] = Text(new_value, fg=self.entries[pointer][1].fg, bg=self.entries[pointer][1].bg)
                    self.survey[self.entries[pointer][0].text] = new_value
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
                        f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                        +f"{it_hl.bg_rgb} {it_hl.styled}{it_hl.bg_rgb} "\
                        +f"{(self.max_len_item-len(item[0].text))*' '}"\
                        +f"{it_hl.fg_rgb}:"\
                        +f"{mk_hl.bg_rgb} {mk_hl.styled}{mk_hl.bg_rgb} "\
                        +f"{(self.max_len_values-len(item[1].text))*' '}",
                        end="")
                else:
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                        +f"{item[0].bg_rgb} {item[0].styled}{item[0].bg_rgb} "\
                        +f"{(self.max_len_item-len(item[0].text))*' '}"\
                        +f"{item[0].fg_rgb}:"\
                        +f"{item[1].bg_rgb} {item[1].styled}{item[1].bg_rgb} "\
                        +f"{(self.max_len_values-len(item[1].text))*' '}", 
                        end="")
            else:
                print(
                    f"{item[0].bg_rgb} {' '*(len(self.cursor.text))}{item[0].bg_rgb} "\
                    +f"{item[0].bg_rgb} {item[0].styled}{item[0].bg_rgb} "\
                    +f"{(self.max_len_item-len(item[0].text))*' '}"\
                    +f"{item[0].fg_rgb}:"\
                    +f"{item[1].bg_rgb} {item[1].styled}{item[1].bg_rgb} "\
                    +f"{(self.max_len_values-len(item[1].text))*' '}", 
                    end="")

        empty_blocks = int(math.ceil(len(self.entries)/wrap)*wrap)-len(self.entries)
        if empty_blocks != 0:
            for i in range(empty_blocks):
                print(f"{self.bg_rgb}{((block_width))*' '}", end='')

        if padding_bottom:
            print(f"\n{self.bg_rgb}{((block_width)*wrap)*' '}")
        
        print(f"{nf}")

    def setEntries(self, entries):
        __entries = []
        for entry in entries:
            if type(entry) not in [type(Text('')), type(Entry('')), type(Checkbox(''))]:
                entry = Entry(str(entry))
            if type(entry) in [type(Text('')), type(Entry('')), type(Checkbox(''))]:
                if entry.bg == not_bg and entry.fg==not_fg:
                    print(f"{entry.text} verificacion 1")
                    entry.bg = self.bg
                    entry.fg = self.fg
                elif entry.bg != not_bg and entry.fg==not_fg:
                    print(f"{entry.text} verificacion 2")
                    entry.fg = self.fg
                    entry.bg = entry.bg
                elif entry.bg == not_bg and entry.fg!=not_fg:
                    print(f"{entry.text} verificacion 3")
                    entry.bg = self.bg
                    entry.fg = entry.fg
                else:
                    print(f"{entry.text} verificacion 4")
                    entry.bg = entry.bg
                    entry.fg = entry.fg
                
                if type(entry) == type(Text('')):
                    entry = Entry(entry.text, entry.id, ' ', 'all', entry.name, entry._class,
                                entry.fg, entry.bg, entry.fg, entry.bg, entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                elif type(entry) == type(Checkbox('')):
                    entry = Entry(entry.text, entry.id, ' ', 'checkbox', entry.name, entry._class,
                                entry.fg, entry.bg, entry.fg, entry.bg, entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                elif type(entry) == type(Entry('')):
                    if entry.placeholder_bg == not_bg and entry.placeholder_fg == not_fg:
                        print(f"{entry.text} verificacion 5")
                        entry = Entry(entry.text, entry.id, entry.value, entry.validation, entry.name, entry._class,
                                entry.fg, entry.bg, self.placeholder_fg, self.placeholder_bg, 
                                entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                    elif entry.placeholder_bg != not_bg and entry.placeholder_fg == not_fg:
                        print(f"{entry.text} verificacion 6")
                        entry = Entry(entry.text, entry.id, entry.value, entry.validation, entry.name, entry._class,
                                entry.fg, entry.bg, entry.placeholder_fg, self.placeholder_bg, 
                                entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                    elif entry.placeholder_bg == not_bg and entry.placeholder_fg != not_fg:
                        print(f"{entry.text} verificacion 7")
                        entry = Entry(entry.text, entry.id, entry.value, entry.validation, entry.name, entry._class,
                                entry.fg, entry.bg, entry.placeholder_fg, self.placeholder_bg, 
                                entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                    elif entry.placeholder_bg != not_bg and entry.placeholder_fg != not_fg:
                        print(f"{entry.text} verificacion 8")
                        entry = Entry(entry.text, entry.id, entry.value, entry.validation, entry.name, entry._class,
                                entry.fg, entry.bg, entry.placeholder_fg, entry.placeholder_bg, 
                                entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                    
                
            __entries.append(entry)

        return __entries
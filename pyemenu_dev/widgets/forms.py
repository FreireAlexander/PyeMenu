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
        self.placeholder_fg = placeholder_fg
        self.placeholder_bg = placeholder_bg
        self.placeholder_fg, self.placeholder_bg = Form.setPlaceholder(self)
        __entries = Form.setEntries(self, entries)
        self.entries = __entries
        self.max_len_item = max(self.entries, key = lambda x: x.lenght).lenght
        title.width = self.max_len_item
        self.max_len_values = max(self.entries, key = lambda x: x._len_value)._len_value
        self.survey = {entry.text:entry.value for entry in self.entries}
        self.cursor = Text.setText(self, cursor)
        self.title = Title.setTitle(self, title)
        

    def print(self,
            pointer: int = 0,
            keyboard = '',
            wrap: int=1,
            highlight: bool = False,
            fg_hl = Colors.white,
            bg_hl = Colors.Lime, 
            title_decorator: str= ' ',
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
        
        if keyboard == key.SPACE:
                    clear_screen()
                    self.entries[pointer].onSelect()
                    clear_screen()
        self.max_len_values = max(self.entries, key = lambda x: x._len_value)._len_value
        block_width = 7+self.cursor.lenght+self.max_len_item+self.max_len_values
        self.survey = {entry.text:entry.value for entry in self.entries}
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
                    it_hl = Entry(item.text, item.id, item.value, item.validation, item.name,
                                  item._class, fg_hl, bg_hl, fg_hl, bg_hl, item.bold, 
                                  item.italic, item.underline, item.blink, item.reverse, item.crossed)
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                        +f"{it_hl.styled_text}"\
                        +f"{it_hl.bg_rgb}{(self.max_len_item-item.lenght)*' '}"\
                        +f"{it_hl.fg_rgb}:"\
                        +f"{it_hl.styled_value}"\
                        +f"{it_hl.placeholder_bg_rgb}{(self.max_len_values-item._len_value)*' '}",
                        end="")
                else:
                    print(
                        f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                        +f"{item.styled_text}"\
                        +f"{item.bg_rgb}{(self.max_len_item-item.lenght)*' '}"\
                        +f"{item.fg_rgb}{item.bg_rgb}:"\
                        +f"{item.styled_value}{item.placeholder_fg_rgb}"\
                        +f"{item.placeholder_bg_rgb}{(self.max_len_values-item._len_value)*' '}", 
                        end="")
            else:
                print(
                    f"{self.cursor.bg_rgb} {' '*(len(self.cursor.text))}{self.cursor.bg_rgb} "\
                    +f"{item.styled_text}"\
                    +f"{item.bg_rgb}{(self.max_len_item-item.lenght)*' '}"\
                    +f"{item.fg_rgb}{item.bg_rgb}:"\
                    +f"{item.styled_value}{item.placeholder_fg_rgb}"\
                    +f"{item.placeholder_bg_rgb}{(self.max_len_values-item._len_value)*' '}", 
                    end="")

        empty_blocks = int(math.ceil(len(self.entries)/wrap)*wrap)-len(self.entries)
        if empty_blocks != 0:
            for i in range(empty_blocks):
                print(f"{self.bg_rgb}{((block_width))*' '}", end='')

        if padding_bottom:
            print(f"\n{self.bg_rgb}{((block_width)*wrap)*' '}")
        
        print(f"{nf}")
        print(f"{nf}")

    def setEntries(self, entries):
        __entries = []
        for entry in entries:   
            if type(entry) in [type(Text('')), type(Entry('estoy vacio')), type(Checkbox(''))]:
                if entry.bg == not_bg and entry.fg == not_fg:
                    entry.bg = self.bg
                    entry.fg = self.fg
                elif entry.bg != not_bg and entry.fg == not_fg:
                    entry.fg = self.fg
                elif entry.bg == not_bg and entry.fg != not_fg:
                    entry.bg = self.bg

                if type(entry) == type(Entry('viendo si es entry')):
                    if entry.placeholder_bg == not_bg and entry.placeholder_fg == not_fg:
                        entry.placeholder_bg = self.placeholder_bg
                        entry.placeholder_fg = self.placeholder_fg
                    elif entry.placeholder_bg != not_bg and entry.placeholder_fg == not_fg:
                        entry.placeholder_fg = self.placeholder_fg
                    elif entry.placeholder_bg == not_bg and entry.placeholder_fg != not_fg:
                        entry.placeholder_bg = self.placeholder_bg
                        
                    entry = Entry(entry.text, entry.id, entry.value, entry.validation, entry.name, entry._class,
                                entry.fg, entry.bg, entry.placeholder_fg, entry.placeholder_bg, 
                                entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                    
                if type(entry) == type(Text('')):
                    entry = Entry(entry.text, entry.id, ' ', 'all', 
                                        entry.name, entry._class,
                                        self.fg, self.bg, 
                                        self.placeholder_fg, self.placeholder_bg, 
                                        entry.bold, entry.italic, 
                                        entry.underline, entry.blink, 
                                        entry.reverse, entry.crossed)
                    
                if type(entry) == type(Checkbox('')):
                    entry = Entry(entry.text, id=entry.id, value=' ', validation='checkbox', 
                                  name=entry.name, _class=entry._class, fg=entry.fg, bg=entry.bg, 
                                  placeholder_fg=self.placeholder_fg, placeholder_bg=self.placeholder_bg, 
                                  bold=entry.bold, italic=entry.italic, underline=entry.underline, 
                                  blink=entry.blink, reverse=entry.reverse, crossed=entry.crossed)
                
            else:
                print(entry)
                print(f"{entry} porque era un texto")
                entry = Entry(str(entry), value=' ', validation='all',fg=self.fg, bg=self.bg, 
                              placeholder_fg=self.placeholder_fg, placeholder_bg=self.placeholder_bg)        
                
            __entries.append(entry)

        return __entries
    
    def setPlaceholder(self):
        if self.placeholder_bg == not_bg and self.placeholder_fg == not_fg:
            print("FORM PL no tiene ni fondo ni letra ")
            placeholder_fg_rgb = self.fg
            placeholder_bg_rgb = self.bg
        if self.placeholder_bg != not_bg and self.placeholder_fg == not_fg:
            print("FORM PL no letra ")
            placeholder_fg_rgb = self.fg
            placeholder_bg_rgb = self.placeholder_bg
        if self.placeholder_bg == not_bg and self.placeholder_fg != not_fg:
            print("FORM PL no tiene fondo ")
            placeholder_fg_rgb = self.placeholder_fg
            placeholder_bg_rgb = self.bg
        if self.placeholder_bg != not_bg and self.placeholder_fg != not_fg:
            
            placeholder_fg_rgb = self.placeholder_fg
            placeholder_bg_rgb = self.placeholder_bg
        
        return placeholder_fg_rgb, placeholder_bg_rgb
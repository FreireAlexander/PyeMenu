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
from .colors import Colors, html_rgb_fg, html_rgb_bg

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
        self.fg = html_rgb_fg(fg)
        self.bg = html_rgb_bg(bg)
        self.json = {}
        if type(cursor) != type(Text('')):
            self.cursor = Text(str(cursor), fg=fg, bg=bg)
        if type(cursor) == type(Text('')) and cursor._bg == not_bg and cursor._fg != not_fg:
            self.cursor = Text(cursor.text, bg=bg, fg=cursor._fg)
        if type(cursor) == type(Text('')) and cursor._fg == not_fg and cursor._bg != not_bg:
            self.cursor = Text(cursor.text, fg=fg, bg=cursor._bg)
        if type(cursor) == type(Text('')) and cursor._fg == not_fg and cursor._bg == not_bg:
            self.cursor = Text(cursor.text, fg=fg, bg=bg)

        if type(title) != type(Title('')):
            self.title = Title(str(title), fg=fg, bg=bg)
        if type(title) == type(Title('')) and title._bg == not_bg and title._fg != not_fg:
            self.title = Title(title.text, bg=bg, fg=title._fg)
        if type(title) == type(Title('')) and title._fg == not_fg and title._bg != not_bg:
            self.title = Title(title.text, fg=fg, bg=title._bg)
        if type(title) == type(Title('')) and title._fg == not_fg and title._bg == not_bg:
            self.title = Title(title.text, fg=fg, bg=bg)

        self.entries = []
        for entry in entries:
            if type(entry) != type(Text('')):
                entry = Text(str(entry), fg=fg, bg=bg)
                value = Text(str(' '), fg=fg, bg=bg)
            if type(entry) == type(Text('')) and entry._bg == not_bg and entry._fg != not_fg:
                entry = Text(entry.text, bg=bg, fg=entry._fg)
                value = Text(str(' '), fg=entry._fg, bg=bg)
            if type(entry) == type(Text('')) and entry._fg == not_fg and entry._bg != not_bg:
                entry = Text(entry.text, fg=fg, bg=entry._bg)
                value = Text(str(' '), fg=fg, bg=entry._bg)
            if type(entry) == type(Text('')) and entry._fg == not_fg and entry._bg == not_bg:
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
        
        if keyboard == key.SPACE:
                    clear_screen()
                    print("Type New Value")
                    print(f"Previous Value: {self.entries[pointer][1].formatted}")
                    new_value = input("Input: ")
                    self.entries[pointer][1] = Text(new_value, fg=self.entries[pointer][1]._fg, bg=self.entries[pointer][1]._bg)
                    self.json[self.entries[pointer][0].text] = new_value
                    clear_screen()
        if padding_up:
            print(f"\n{self.bg}{((6+self.cursor.lenght+self.max_len_item+self.max_len_values)*wrap)*' '}")
        if self.title.text != '':
            self.title.print_title(title_align, title_decorator, 
                (6+self.cursor.lenght+self.max_len_item+self.max_len_values)*wrap, 
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
                        f"{nf}{self.cursor.bg} {self.cursor.formatted}{nf}{it_hl.bg} "\
                        +f"{it_hl.formatted}{html_rgb_bg(bg_gl)} "\
                        +f"{html_rgb_fg(fg_hl)}: {mk_hl.formatted}{html_rgb_bg(bg_gl)}{html_rgb_fg(fg_hl)} "\
                        +f"{(self.max_len_values+self.max_len_item-len(item[0].text)-len(item[1].text))*' '}", 
                        end="")
                else:
                    print(
                        f"{nf}{self.cursor.bg} {self.cursor.formatted}{nf}{item.bg} "\
                        +f"{item[0].formatted}{item[0].bg} "\
                        +f": {item[1].formatted}{item[0].bg} "\
                        +f"{(self.max_len_values+self.max_len_item-len(item[0].text)-len(item[1].text))*' '}", end="")
            else:
                print(
                    f"{item[0].bg} {' '*(len(self.cursor.text)+1)}"\
                    +f"{item[0].formatted}{item[0].bg} "\
                    +f"{item[1].fg}: {item[1].formatted}{item[1].bg}{item[1].fg}{item[1].bg} "\
                    +f"{(self.max_len_values+self.max_len_item-len(item[0].text)-len(item[1].text))*' '}", 
                    end="")

        empty_blocks = int(math.ceil(len(self.entries)/wrap)*wrap)-len(self.entries)
        if empty_blocks != 0:
            for i in range(empty_blocks):
                print(f"{self.bg}{((6+self.cursor.lenght+self.max_len_item+self.max_len_values))*' '}", end='')

        if padding_bottom:
            print(f"\n{self.bg}{((6+self.cursor.lenght+self.max_len_item+self.max_len_values)*wrap)*' '}")
        print(f"{nf}")

        

"""
import pyemenu_dev as pyemenu 
from readchar import key, readkey, readchar
import functools
import time

def main():
    entries = ['lado 1', 'lado 2', 'lado 3', 'lado 4']
    entries = [[entry, ''] for entry in entries]
    print(entries)
    buttons = ['perimetro', 'area','salir']
    forms = entries.copy()
    forms.extend(buttons)
    print("Holis")
    print(f"Forms {forms}")
    
    grid_entries = 1
    grid_buttons = 2
    cursor = '-->'
    col = 0
    while True:
        pyemenu.clear()
        print(f"entries: {entries}")
        
        for item in range(len(forms)):
            if forms[item] in entries:
                if item % grid_entries == 0:
                    print("")
                if col==item:
                    print(f"{cursor} {forms[item][0]}: {forms[item][1]} ", end='')
                else:
                    print(f" {forms[item][0]}: {forms[item][1]} ", end='')
            if forms[item] in buttons:
                if item % grid_buttons == 0:
                    print("")
                if col==item:
                    print(f"\t\033[48;2;255;0;0m{forms[item]}\033[0m\t", end='')
                else:
                    print(f"\t{forms[item]}\t", end='')

        
        teclado = pyemenu.input_key()
        col = pyemenu.cursor_position(teclado, col, grid_entries)
        if col > len(forms) - 1:
            col = len(forms)-1
        if teclado in ['q', 'Q']:
            break
        if teclado == key.SPACE and forms[col] in entries:
            pyemenu.clear()
            print(f"Actualizar valor en la columna {col} de : {entries[col]}")
            entries[col][1] = input("Ingrese nuevo valor: ")
            forms[col][1] = entries[col][1]
        
        # Acciones de los botones
        if teclado == key.ENTER and forms[col] in buttons and forms[col] == 'perimetro':
            print(f"Seleccionaste {forms[col]}")
            try:
                print(f"elperimetro es: {sum([float(i[1]) for i in entries])}")
            except:
                print("La embarraste")
            pyemenu.input_key()
        
        if teclado == key.ENTER and forms[col] in buttons and forms[col] == 'multiplicar':
            print(f"Seleccionaste {forms[col]}")
            try:
                print(f"los cuadrados de la lista es: {list(map(lambda i: i**2,list(map(lambda i: int(i),entries))))}")
            except:
                print("La embarraste")
            pyemenu.input_key()
    

if __name__ == '__main__':
    main()

"""
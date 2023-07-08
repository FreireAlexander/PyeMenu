"""
    This module provide an easy way to build menu prompts for CLI
    this module contain the next Class:
    Checkboxlist() for create simple and easy useful Menu 

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
# Locals
from ..components import Text, Title, Checkbox, Entry, Button
from ..colors import Colors, setColor
from ..tools import getKeyboard, clear_screen, setCursor, print_title
from ..tools import resize_screen, print_logo, fill_empty_blocks
# Externals
import math
from readchar import key
from copy import deepcopy

nf = '\x1b[0m'
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'
input_info = """
    Press Space to input
    Press Delete to clear the input value 
    Press Enter to exit and return the answers"""

def clear_all(form):
    for entry in form:
        entry.clear()

def exit_form(self, form):
    self.exit = True
    self.answer = {entry.text:' ' for entry in self.entries}
    return self.exit, self.answer

def submit_answer(self):
    self.exit = True
    return self.exit

class Form():
    '''
    This class allow to create an simple option list for selecting
    one option from a list of options.
    The parameters to initialize the class are:
        entries: List -> List of entries for gather answers or info
            could be a list with strins or Entry or Text Type
        buttons: List -> Must be strings or Button object
        title: str or Text object -> The text title to be printed up the menu
        cursor: str or Text object -> The char/s that represent the cursor
        fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        bg: str -> A color in hexadecimal, much of colors could be found in Colors class
        placeholder_fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        placeholder_bg: str -> A color in hexadecimal, much of colors could be found in Colors class
    Some of the properties of this class are:
        answer -> return the selected answer from the entries as dict
    For Show this Form it should be use the print() method.
    '''
    def __init__(self, entries: list, buttons = ['clear', 'submit', 'exit'],
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
        self.entries = Form.setEntries(self, entries)
        self.buttons = Form.setButtons(self, buttons)
        self.elements = deepcopy(self.entries)
        self.elements.extend(self.buttons)
        self.max_len_entry = max(self.elements, key = lambda x: x.lenght).lenght
        self.max_len_button = max(self.buttons, key = lambda x: x.lenght).lenght
        title.width = self.max_len_entry
        self.max_len_values = max(self.entries, key = lambda x: x._len_value)._len_value
        self.answer = {entry.text:entry.value for entry in self.entries}
        self.cursor = Text.setText(self, cursor)
        self.title = Title.setTitle(self, title)
        self.exit = False
        if buttons == ['clear', 'submit', 'exit']:
            self.buttons[0].onClick = lambda: clear_all(self.entries)
            self.buttons[1].onClick = lambda: submit_answer(self)
            self.buttons[2].onClick = lambda: exit_form(self, self.entries)
        
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
            title_padding_bottom: bool = False, 
            button_focus_blink: bool = False,
            logo: str = ''
            ):
        """
        This Method allow a Form to be show on screen, it is possible to 
        specifies:
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
            logo: str -> This parameter allow to print a logo or an extra title 
                above the Form print
        """
        # Initialazing Variables
        pointer = 0
        keyboard = None
        while True:
            clear_screen()
            self.answer = {entry.text:entry.value for entry in self.entries}
            if keyboard == key.DELETE:
                if pointer in range(len(self.entries)):
                    clear_screen()
                    self.entries[pointer].clear()
                    clear_screen()
            if keyboard == key.SPACE:
                if pointer in range(len(self.entries)):
                    clear_screen()
                    self.entries[pointer].onSelect()
                    clear_screen()
            if keyboard == key.ENTER:
                if pointer in range(len(self.entries)):
                    clear_screen()
                    self.entries[pointer].onSelect()
                    clear_screen()
                if pointer in range(len(self.entries), len(self.elements)):
                    clear_screen()
                    self.elements[pointer].click()
                    clear_screen()
            if keyboard in ["q", "Q"]:
                self.answer = {entry.text:'' for entry in self.entries}
                break
            if self.exit == True:
                break
            
            
            self.max_len_values = max(self.entries, key = lambda x: x._len_value)._len_value
            block_width = 7+self.cursor.lenght+self.max_len_entry+self.max_len_values
            wrap = resize_screen(wrap, block_width)
            print_logo(logo)

            if padding_up:
                print(f"{self.bg_rgb}{((block_width)*wrap)*' '}")
            print_title(self, title_align, title_decorator, 
                        block_width, wrap, title_padding_up, 
                        title_padding_bottom)
            for entry in self.entries:
                if self.entries.index(entry) % wrap == 0:
                    print("")
                if pointer == self.entries.index(entry):
                    if highlight:
                        it_hl = Entry(entry.text, entry.value, entry.validation,
                                    fg_hl, bg_hl, fg_hl, bg_hl, entry.bold, 
                                    entry.italic, entry.underline, entry.blink, entry.reverse, entry.crossed)
                        if it_hl.validation=='password':
                            print(
                                f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                                +f"{it_hl.styled_text}"\
                                +f"{it_hl.bg_rgb}{(self.max_len_entry-entry.lenght)*' '}"\
                                +f"{it_hl.fg_rgb}:"\
                                +f" {it_hl._len_value*'*'} "\
                                +f"{it_hl.placeholder_bg_rgb}{(self.max_len_values-entry._len_value)*' '}",
                                end="")
                        else:
                            print(
                                f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                                +f"{it_hl.styled_text}"\
                                +f"{it_hl.bg_rgb}{(self.max_len_entry-entry.lenght)*' '}"\
                                +f"{it_hl.fg_rgb}:"\
                                +f"{it_hl.styled_value}"\
                                +f"{it_hl.placeholder_bg_rgb}{(self.max_len_values-entry._len_value)*' '}",
                                end="")
                    else:
                        print(
                            f"{self.cursor.bg_rgb} {self.cursor.styled}{self.cursor.bg_rgb} "\
                            +f"{entry.styled_text}"\
                            +f"{entry.bg_rgb}{(self.max_len_entry-entry.lenght)*' '}"\
                            +f"{entry.fg_rgb}{entry.bg_rgb}:"\
                            +f"{entry.styled_value}{entry.placeholder_fg_rgb}"\
                            +f"{entry.placeholder_bg_rgb}{(self.max_len_values-entry._len_value)*' '}", 
                            end="")
                else:
                    print(
                        f"{self.cursor.bg_rgb} {' '*(len(self.cursor.text))}{self.cursor.bg_rgb} "\
                        +f"{entry.styled_text}"\
                        +f"{entry.bg_rgb}{(self.max_len_entry-entry.lenght)*' '}"\
                        +f"{entry.fg_rgb}{entry.bg_rgb}:"\
                        +f"{entry.styled_value}{entry.placeholder_fg_rgb}"\
                        +f"{entry.placeholder_bg_rgb}{(self.max_len_values-entry._len_value)*' '}", 
                        end="")

            empty_blocks = int(math.ceil(len(self.entries)/wrap)*wrap)-len(self.entries)
            fill_empty_blocks(self, empty_blocks, block_width)
            if padding_bottom:
                print(f"\n{self.bg_rgb}{((block_width)*wrap)*' '}")
            
            print(f"{nf}")
            print(f"{block_width*wrap*'—'}", end='')
            for button in self.buttons:
                button_space = 3+self.max_len_values+self.max_len_entry-button.lenght
                if button_space%2==0:
                    left_spaces = button_space//2
                    right_spaces = left_spaces
                else:
                    left_spaces = button_space//2
                    right_spaces = button_space//2 + 1

                if self.buttons.index(button) % wrap == 0:
                    print("\n")
                
                if pointer == self.elements.index(button):
                    button_selected = Button(label=button.text, bg=bg_hl, fg=fg_hl, blink=button_focus_blink)
                    print(
                        f" {' '*(len(self.cursor.text))} "\
                        +f"{button_selected.bg_rgb}{(left_spaces)*' '}"\
                        +f"{button_selected.print}"\
                        +f"{button_selected.bg_rgb}{(right_spaces)*' '}\x1b[0m"\
                        ,end='')
                else:
                    print(
                        f" {' '*(len(self.cursor.text))} "\
                        +f"{button.bg_rgb}{(left_spaces)*' '}"\
                        +f"{button.print}"\
                        +f"{button.bg_rgb}{(right_spaces)*' '}\x1b[0m"\
                        ,end='')
            
            print(f"{nf}")
            keyboard = getKeyboard(input_info)
            pointer = setCursor(keyboard, pointer, self.elements, wrap)

    def setEntries(self, entries):
        __entries = []
        for entry in entries:   
            if type(entry) in [type(Text('')), type(Entry('')), type(Checkbox(''))]:
                if entry.bg == not_bg and entry.fg == not_fg:
                    entry.bg = self.bg
                    entry.fg = self.fg
                elif entry.bg != not_bg and entry.fg == not_fg:
                    entry.fg = self.fg
                elif entry.bg == not_bg and entry.fg != not_fg:
                    entry.bg = self.bg

                if type(entry) == type(Entry('')):
                    if entry.placeholder_bg == not_bg and entry.placeholder_fg == not_fg:
                        entry.placeholder_bg = self.placeholder_bg
                        entry.placeholder_fg = self.placeholder_fg
                    elif entry.placeholder_bg != not_bg and entry.placeholder_fg == not_fg:
                        entry.placeholder_fg = self.placeholder_fg
                    elif entry.placeholder_bg == not_bg and entry.placeholder_fg != not_fg:
                        entry.placeholder_bg = self.placeholder_bg
                        
                    entry = Entry(entry.text, entry.value, entry.validation,
                                entry.fg, entry.bg, entry.placeholder_fg, entry.placeholder_bg, 
                                entry.bold, entry.italic, 
                                entry.underline, entry.blink, entry.reverse, entry.crossed)
                    
                if type(entry) == type(Text('')):
                    entry = Entry(entry.text, '', 'all', 
                                        self.fg, self.bg, 
                                        self.placeholder_fg, self.placeholder_bg, 
                                        entry.bold, entry.italic, 
                                        entry.underline, entry.blink, 
                                        entry.reverse, entry.crossed)
                    
                if type(entry) == type(Checkbox('')):
                    entry = Entry(entry.text, value='', validation='checkbox', 
                                    fg=entry.fg, bg=entry.bg, 
                                    placeholder_fg=self.placeholder_fg, 
                                    placeholder_bg=self.placeholder_bg, 
                                    bold=entry.bold, italic=entry.italic, 
                                    underline=entry.underline, blink=entry.blink, 
                                    reverse=entry.reverse, crossed=entry.crossed)
            else:
                entry = Entry(str(entry), value='', validation='all',fg=self.fg, bg=self.bg, 
                                placeholder_fg=self.placeholder_fg, placeholder_bg=self.placeholder_bg)        
                
            __entries.append(entry)

        return __entries

    def setButtons(self, buttons):
        __buttons = []
        for button in buttons:   
            if type(button) != type(Button(' ')):
                button = Button(str(button))        
                
            __buttons.append(button)

        return __buttons
    
    def setPlaceholder(self):
        if self.placeholder_bg == not_bg and self.placeholder_fg == not_fg:
            placeholder_fg_rgb = self.fg
            placeholder_bg_rgb = self.bg
        if self.placeholder_bg != not_bg and self.placeholder_fg == not_fg:
            placeholder_fg_rgb = self.fg
            placeholder_bg_rgb = self.placeholder_bg
        if self.placeholder_bg == not_bg and self.placeholder_fg != not_fg:
            placeholder_fg_rgb = self.placeholder_fg
            placeholder_bg_rgb = self.bg
        if self.placeholder_bg != not_bg and self.placeholder_fg != not_fg:
            placeholder_fg_rgb = self.placeholder_fg
            placeholder_bg_rgb = self.placeholder_bg
        
        return placeholder_fg_rgb, placeholder_bg_rgb
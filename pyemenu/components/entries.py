import re
from .texts import Text
from ..colors import setColor

import getpass

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'
email_regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+' 

class Entry(Text):
    """
    Generate a Entry with its label and its value, this class extend from Text()
    this class allow to perform a validition from user's input, there are a predefined
    validitaion types, this must be pass as string, for example validation='all'
    these are:
        1. password -> allow to get an password value and show hidden in the form
        2. all      -> allow anything from user, this is the value for validation by default
        3. int      -> allow just integer
        4. alnum    -> allow just alphanumeric chars
        5. email    -> allow just a valid email format
        6. checkbox -> allow the entry to perform as a Checkbox
        
        Also it is possible to pass a validation function for validate the desire input from user
        these must return just False or True bool type
        
    some formats and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    A full list of terminals will be show on https://github.com/FreireAlexander/PyeMenu
    properties:
        text: str
        value: str=''
        validation: str='all'         
    ***** Text Style *****
        fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        bg: str -> A color in hexadecimal, much of colors could be found in Colors class
        placeholder_fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        placeholder_bg: str -> A color in hexadecimal, much of colors could be found in Colors class
        bold: bool 
        italic: bool 
        underline: bool 
        blink: bool 
        reverse: bool 
        crossed: bool
        
    PyeMenu version 1.0.0
    """
    def __init__(self, label: str, value: str='', validation='all',
                fg: str = not_fg, bg: str = not_bg,
                placeholder_fg: str = not_fg, placeholder_bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(label, fg, bg,
                            bold, italic, underline, 
                            blink, reverse, crossed)
        self.validation = validation
        self._text = ' '+label+' '
        self._lenght = len(self._text)
        self.placeholder_fg = placeholder_fg
        self.placeholder_bg = placeholder_bg
        Entry.setPlaceholder(self)     
        self.styled_text = Text.setStyle(self, self._text, self.fg, self.bg, bold, italic, underline, blink, reverse, crossed)
        self.value = value
        self._value = ' '+value+' '
        self.styled_value = Text.setStyle(self, self._value, self.placeholder_fg, self.placeholder_bg, bold, italic, underline, blink, reverse, crossed)
        self._len_value = len(self.value)
        self.print_label = f"{self.styled_text}{self.bg_rgb} "+"\x1b[0m"
        self.print_value = f"{self.styled_value}{self.placeholder_bg_rgb}"+"\x1b[0m"
        self.print = self.print_label + f"{self.bg_rgb}{self.fg_rgb}: " + self.print_value
        
    def setPlaceholder(self):
        """
        This method set the placeholder style
        """
        if self.placeholder_bg == not_bg and self.placeholder_fg == not_fg:
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(self.fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(self.bg)
        elif self.placeholder_bg != not_bg and self.placeholder_fg == not_fg:
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(self.fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(self.placeholder_bg)
        elif self.placeholder_bg == not_bg and self.placeholder_fg != not_fg:
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(self.placeholder_fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(self.bg)
        elif self.placeholder_bg != not_bg and self.placeholder_fg != not_fg:
            self.placeholder_fg_rgb = '\x1b[38;'+setColor(self.placeholder_fg)
            self.placeholder_bg_rgb = '\x1b[48;'+setColor(self.placeholder_bg)

        return self.placeholder_fg_rgb, self.placeholder_bg_rgb
    
    
    def onSelect(self):
        """
        This method perform the validation type for the Entry
        """
        if self.validation == 'password':
            try:
                value = getpass.getpass(prompt='Type Password: ')
            except Exception as error:
                print('ERROR', error)
            self.value = value
            self._value = " "+f"{len(value)*'*'}"+" "
            self._len_value = len(self.value)
            self.styled_value = Text.setStyle(self, self._value, self.placeholder_fg, self.placeholder_bg, self.bold, 
                                        self.italic, self.underline, self.blink, self.reverse, self.crossed)
            self.print_value = f"{self.styled_value}{self.placeholder_bg_rgb}"+"\x1b[0m"
            self.print = self.print_label + f"{self.bg_rgb}{self.fg_rgb}: " + self.print_value
        else:
            if self.validation == 'all':
                value = input("Type new value: ")
            elif self.validation == 'float':
                while True:
                    try:
                        value = str(float(input("Please enter a number: ")))
                    except ValueError:
                        print("Oops!  That was not a valid number.  Try again...")
                    else:
                        break
            elif self.validation == 'int':
                while True:
                    try:
                        value = str(int(input("Please enter a number: ")))
                    except ValueError:
                        print("Oops!  That was not a valid integer number.  Try again...")
                    else:
                        break
            elif self.validation == 'alnum':
                value = input("Type an alphanumeric value: ")
                while value.isalnum() == False:
                    print("Oop's somethings is wrong... try again")
                    value = input("Type an alphanumeric value: ")
            elif self.validation == 'email':
                value = input("Type email: ")
                while re.match(email_regex, value) == None:
                    print("OOps it's not email")
                    value = input("Type email again: ")
            elif self.validation == 'checkbox':
                if self.value == '':
                    value = '*'
                else:
                    value = ''
            else:
                value = input("Type new value: ")
                while self.validation(value) == False:
                    print("Oop's somethings is wrong... try again")
                    value = input("Type new value: ")

            self.value = value
            self._len_value = len(self.value)
            self._value = ' '+str(value)+' '
            self.styled_value = Text.setStyle(self, self._value, self.placeholder_fg, self.placeholder_bg, self.bold, 
                                        self.italic, self.underline, self.blink, self.reverse, self.crossed)
            self.print_value = f"{self.styled_value}{self.placeholder_bg_rgb}"+"\x1b[0m"
            self.print = self.print_label + f"{self.bg_rgb}{self.fg_rgb}: " + self.print_value
    
    def clear(self):
        """
        This method clear the value of the Entry
        """
        self.value = ''
        self._len_value = len(self.value)
        self._value = ' '+str(self.value)+' '
        self.styled_value = Text.setStyle(self, self._value, self.placeholder_fg, 
                                            self.placeholder_bg, self.bold, 
                                            self.italic, self.underline, self.blink, 
                                            self.reverse, self.crossed)
        self.print_value = f"{self.styled_value}{self.placeholder_bg_rgb}"+"\x1b[0m"
        self.print = self.print_label + f"{self.bg_rgb}{self.fg_rgb}: " + self.print_value
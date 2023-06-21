import re
from .texts import Text
from ..colors import setColor

import getpass
 


not_fg = '\x1b[39m'
not_bg = '\x1b[49m'
email_regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+' 

class Entry(Text):
    """
    Generate a Check Box with its label, this class extend from Text()
    some formats and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    properties:
        text: str         
    ***** Text Style *****
        fg: str # in html format, much color colud be found in Color() Class
        bg: str # in html format, much color colud be found in Color() Class
        bold: bool 
        italic: bool 
        underline: bool 
        blink: bool 
        reverse: bool 
        crossed: bool 
    """
    def __init__(self, label: str, id=None, value: str=' ', validation='all',
                name: str='',_class: str='', fg: str = not_fg, bg: str = not_bg,
                placeholder_fg: str = not_fg, placeholder_bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(label, id, name,_class, fg, bg,
                bold, italic, underline, blink, reverse, crossed)
        self.validation = validation
        self._text = ' '+label+' '
        self._lenght = len(self._text)
        
        self.placeholder_fg = placeholder_fg
        self.placeholder_bg = placeholder_bg
        self.placeholder_fg_rgb, self.placeholder_bg_rgb = Entry.setPlaceholder(self)     
        self.styled_text = Text.style(self, self._text, self.fg, self.bg, bold, italic, underline, blink, reverse, crossed)
        self.value = value
        self._value = ' '+value+' '
        self.styled_value = Text.style(self, self._value, self.placeholder_fg, self.placeholder_bg, bold, italic, underline, blink, reverse, crossed)
        self._len_value = len(self.value)
        self.print_label = f"{self.styled_text}{self.bg_rgb} "+"\x1b[0m"
        self.print_value = f"{self.styled_value}{self.placeholder_bg_rgb}"+"\x1b[0m"
        self.print = self.print_label + f"{self.bg_rgb}{self.fg_rgb}: " + self.print_value
        
    def setPlaceholder(self):
        if self.placeholder_bg == not_bg and self.placeholder_fg == not_fg:
            print("PL no tiene ni fondo ni letra ")
            placeholder_fg_rgb = '\x1b[38;'+setColor(self.fg)
            placeholder_bg_rgb = '\x1b[48;'+setColor(self.bg)
        if self.placeholder_bg != not_bg and self.placeholder_fg == not_fg:
            print("PL no letra ")
            placeholder_fg_rgb = '\x1b[38;'+setColor(self.fg)
            placeholder_bg_rgb = '\x1b[48;'+setColor(self.placeholder_bg)
        if self.placeholder_bg == not_bg and self.placeholder_fg != not_fg:
            print("PL no tiene fondo ")
            placeholder_fg_rgb = '\x1b[38;'+setColor(self.placeholder_fg)
            placeholder_bg_rgb = '\x1b[48;'+setColor(self.bg)
        if self.placeholder_bg != not_bg and self.placeholder_fg != not_fg:
            
            placeholder_fg_rgb = '\x1b[38;'+setColor(self.placeholder_fg)
            placeholder_bg_rgb = '\x1b[48;'+setColor(self.placeholder_bg)
        
        return placeholder_fg_rgb, placeholder_bg_rgb
    
    
    def onSelect(self):
        if self.validation == 'password':
            try:
                value = getpass.getpass(prompt='Type Password: ')
            except Exception as error:
                print('ERROR', error)
            self.value = value
            self._value = " "+f"{len(value)*'*'}"+" "
            self._len_value = len(self.value)
            self.styled_value = Text.style(self, self._value, self.placeholder_fg, self.placeholder_bg, self.bold, 
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
                if self.value == ' ':
                    value = 'x'
                else:
                    value = ' '
            else:
                value = input("Type new value: ")
                while self.validation(value) == False:
                    print("Oop's somethings is wrong... try again")
                    value = input("Type new value: ")

            self.value = value
            self._len_value = len(self.value)
            self._value = ' '+str(value)+' '
            self.styled_value = Text.style(self, self._value, self.placeholder_fg, self.placeholder_bg, self.bold, 
                                        self.italic, self.underline, self.blink, self.reverse, self.crossed)
            self.print_value = f"{self.styled_value}{self.placeholder_bg_rgb}"+"\x1b[0m"
            self.print = self.print_label + f"{self.bg_rgb}{self.fg_rgb}: " + self.print_value
            
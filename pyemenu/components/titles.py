from .texts import Text

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Title(Text):
    """
    This class allow you to format a Title, this class extend from Text()
    some colors styles and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    A full list of terminals will be show on https://github.com/FreireAlexander/PyeMenu
    properties:
        text: str         
    ***** Text Style *****
        fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        bg: str -> A color in hexadecimal, much of colors could be found in Colors class
        bold: bool 
        italic: bool 
        underline: bool 
        blink: bool 
        reverse: bool 
        crossed: bool 
        
        PyeMenu version 1.0.1
    """
    def __init__(self, text: str,
                fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(text, fg, bg,
                            bold, italic, underline, 
                            blink, reverse, crossed)
        self.title_text = ' '+text+' '
        self._lenght = len(self.title_text)
        self.styled = Text.setStyle(self, self.title_text, self.fg, self.bg, 
                                    self.bold, self.italic, self.underline, 
                                    self.blink, self.reverse, self.crossed)
        
    
    def print_title(self, align: str = 'center',
                decorator: str = ' ',
                width: int = 0,
                padding_up: bool = False,
                padding_bottom: bool = False):
        """
        This Methods print the Title, it is possible to 
        specifies:
        align: str -> 'center', 'right' or 'left'
        decorator: str -> just one char to print around Title text
        width: int -> width in number of chars
        new_line_up: bool = False -> add a new line above title
        new_line_bottom: bool = False -> add a new line behind title
        """
        decorator = Text.setText(self, oneChar(decorator))
        spaces = (width-self._lenght)  
        if type(decorator)==type(Text('')):
            if align == 'center':
                if spaces%2==0:
                    title_text = f"{spaces//2*decorator.styled}"+f"{self.styled}"+f"{spaces//2*decorator.styled}"
                else:
                    title_text = f"{(spaces//2+1)*decorator.styled}"+f"{self.styled}"+f"{spaces//2*decorator.styled}"
            if align == 'right':
                title_text = f"{spaces*decorator.styled}"+f"{self.styled}"
            if align == 'left':
                title_text = f"{self.styled}"+f"{spaces*decorator.styled}"
        
        title_text = title_text + '\x1b[0m'
        if padding_up and padding_bottom:
            print(f"{self.bg_rgb}{width*' '}")
            print(f"{title_text}")
            print(f"{self.bg_rgb}{width*' '}", end='')
        elif padding_up:
            print(f"{self.bg_rgb}{width*' '}")
            print(f"{title_text}", end='')
        elif padding_bottom:
            print(f"{title_text}")
            print(f"{self.bg_rgb}{width*' '}", end='')
        else: print(title_text, end='')

        print('\x1b[0m', end='')

    def setTitle(self, title):
        """
        This method transform a string object to a Title object
        """
        if type(title) != type(Title('')):
            title = Title(str(title), fg=self.fg, bg=self.bg)
        if type(title) == type(Title('')) and title.bg != not_bg and title.fg != not_fg:
            title = Title(title.text, bg=title.bg, fg=title.fg, 
                            bold=title.bold, italic=title.italic, underline=title.underline, 
                            blink=title.blink, reverse=title.reverse, crossed=title.crossed)
        if type(title) == type(Title('')) and title.bg == not_bg and title.fg != not_fg:
            title = Title(title.text, bg=self.bg, fg=title.fg, 
                            bold=title.bold, italic=title.italic, underline=title.underline, 
                            blink=title.blink, reverse=title.reverse, crossed=title.crossed)
        if type(title) == type(Title('')) and title.fg == not_fg and title.bg != not_bg:
            title = Title(title.text, fg=self.fg, bg=title.bg,
                            bold=title.bold, italic=title.italic, underline=title.underline, 
                            blink=title.blink, reverse=title.reverse, crossed=title.crossed)
        if type(title) == type(Title('')) and title.fg == not_fg and title.bg == not_bg:
            title = Title(title.text, fg=self.fg, bg=self.bg,
                            bold=title.bold, italic=title.italic, underline=title.underline, 
                            blink=title.blink, reverse=title.reverse, crossed=title.crossed)
        
        return title
    
def oneChar(string):
    """
    This funtion is for validate just one length string in print titles and others
    """
    if type(string) == type(Text('')):
        if string.lenght > 1:
            string = Text(' ', string.fg, string.bg, string.bold,
                            string.italic, string.underline, string.blink,
                            string.reverse, string.crossed)
            return string
        else:
            return string
    if str(string):
        if len(string)>1:
            return ' '
        else:
            return string


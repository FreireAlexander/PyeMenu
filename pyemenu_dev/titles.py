from .texts import Text

no_format = '\x1b[0m'

class Title(Text):
    """
    This class allow you to format a Title, this class extend from Text()
    some formats and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    properties:
        text: str 
    ***** optionals *****
        position = 'center' by default or 'right' or 'left'
        decorator = ' ' # Decorator must be an string or Text()
        width = 0 # by default, width of characters
        text_color: str # in html format, much color colud be found in Color() Class
        background_color: str # in html format, much color colud be found in Color() Class
    ***** Text Style *****
        bold: bool 
        italic: bool 
        underline: bool 
        blink: bool 
        reverse: bool 
        crossed: bool 
    """
    def __init__(self, 
                    text: str,
                    position: str = 'center',
                    decorator = '',
                    width: int = 0,
                    text_color: str = no_format,
                    background_color: str = no_format,
                    bold: bool = False,
                    italic: bool = False,
                    underline: bool = False,
                    blink: bool = False,
                    reverse: bool = False,
                    crossed: bool = False):
        
        super().__init__(text, text_color, background_color, 
                         bold, italic, underline, blink, 
                         reverse, crossed)
        self.position = position
        self.decorator = decorator
        spaces = (width-len(self.text))
        if type(decorator)==type('str'):
            if self.position == 'center':
                if spaces%2==0:
                    self.print = f"{spaces//2*decorator}"+f"{self.formatted}"+f"{spaces//2*decorator}"
                else:
                    self.print = f"{(spaces//2+1)*decorator}"+f"{self.formatted}"+f"{spaces//2*decorator}"
            if self.position == 'right':
                self.print = f"{spaces*decorator}"+f"{self.formatted}"
            if self.position == 'left':
                self.print = f"{self.formatted}"+f"{spaces*decorator}"   
        if type(decorator)==type(Text('')):
            if self.position == 'center':
                if spaces%2==0:
                    self.print = f"{spaces//2*decorator.formatted}"+f"{self.formatted}"+f"{spaces//2*decorator.formatted}"
                else:
                    self.print = f"{(spaces//2+1)*decorator.formatted}"+f"{self.formatted}"+f"{spaces//2*decorator.formatted}"
            if self.position == 'right':
                self.print = f"{spaces*decorator.formatted}"+f"{self.formatted}"
            if self.position == 'left':
                self.print = f"{self.formatted}"+f"{spaces*decorator.formatted}"

        
        

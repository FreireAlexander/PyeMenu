from .colors import html_rgb

no_format = '\x1b[0m'

class Text():
    """
    This class allow you to format text, some formats and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    properties:
        text: str 
        optionals
        text_color: str 
        background_color: 
        bold: bool 
        italic: bool 
        underline: bool 
        blink: bool 
        reverse: bool 
        crossed: bool 
    """
    text: str = None
    
    def __init__(self,text: str, 
                text_color: str = no_format, 
                background_color: str = no_format,
                bold: bool = False,
                italic: bool = False,
                underline: bool = False,
                blink: bool = False,
                reverse: bool = False,
                crossed: bool = False):
        self.text = text
        self.text_color = html_rgb(text_color)
        self.background_color = html_rgb(background_color)
        self.bold = bold
        self.italic = italic
        self.blink = blink
        self.underline = underline
        self.reverse = reverse
        self.crossed = crossed
        self.formatted = self.text
        if self.bold:
            self.formatted = f"\x1b[1m" + self.formatted
        if self.italic:
            self.formatted = f"\x1b[3m" + self.formatted
        if self.underline:
            self.formatted = f"\x1b[4m" + self.formatted
        if self.blink:
            self.formatted = f"\x1b[5m" + self.formatted
        if self.reverse:
            self.formatted = f"\x1b[7m" + self.formatted
        if self.crossed:
            self.formatted = f"\x1b[9m" + self.formatted
        if self.text_color != no_format and self.background_color != no_format:
            self.formatted = f"\x1b[38;{self.text_color}\x1b[48;{self.background_color}" + self.formatted
        if self.text_color == no_format and self.background_color != no_format:
            self.formatted = f"\x1b[48;{self.background_color}" + self.formatted
        if self.text_color != no_format and self.background_color == no_format:
            self.formatted = f"\x1b[38;{self.text_color}" + self.formatted
        
        self.formatted += '\x1b[0m'
    

        
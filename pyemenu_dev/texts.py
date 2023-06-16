from .colors import html_rgb_fg, html_rgb_bg

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Text():
    """
    This class allow you to format text, some formats and effects are not available
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
    text: str = None
    
    def __init__(self,text: str, 
                fg: str = not_fg, 
                bg: str = not_bg,
                bold: bool = False,
                italic: bool = False,
                underline: bool = False,
                blink: bool = False,
                reverse: bool = False,
                crossed: bool = False):
        self.text = text
        self.fg = html_rgb_fg(fg)
        self.bg = html_rgb_bg(bg)
        self._fg = fg
        self._bg = bg
        self.bold = bold
        self.italic = italic
        self.blink = blink
        self.underline = underline
        self.reverse = reverse
        self.crossed = crossed
        self.lenght = len(self.text)
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
        if self.fg != not_fg and self.bg != not_bg:
            self.formatted = f"{self.fg}{self.bg}" + self.formatted
        if self.fg == not_fg and self.bg == not_bg:
            self.formatted = f"\x1b[0m" + self.formatted
        if self.fg == not_fg and self.bg != not_bg:
            self.formatted = f"{self.bg}" + self.formatted
        if self.fg != not_fg and self.bg == not_bg:
            self.formatted = f"{self.fg}" + self.formatted
        
        self.formatted += '\x1b[0m'
    

        
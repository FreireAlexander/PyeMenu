from ..colors import setColor

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
    
    def __init__(self, text: str, id=None,
                name: str='',_class: str='', fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        self.text = text
        self.id = id
        if name == '':
            self.name = 'Text'
        else:
            self.name = str(name)
        if _class == '':
            self._class = 'Text'
        else:
            self._class = str(_class)
        self._class = _class
        self.fg = fg
        self.fg_rgb = '\x1b[38;'+setColor(fg)
        self.bg = bg
        self.bg_rgb = '\x1b[48;'+setColor(bg)
        self.bold = bold
        self.italic = italic
        self.blink = blink
        self.underline = underline
        self.reverse = reverse
        self.crossed = crossed
        self.lenght = len(self.text)
        self.styled = Text.style(self, self.text, self.fg, self.bg, 
                                self.bold, self.italic, self.underline, self.blink, self.reverse, self.crossed)

    def style(self, chars, fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
            result = chars
            if bold:
                result = f"\x1b[1m" + result
            if italic:
                result = f"\x1b[3m" + result
            if underline:
                result = f"\x1b[4m" + result
            if blink:
                result = f"\x1b[5m" + result
            if reverse:
                result = f"\x1b[7m" + result
            if crossed:
                result = f"\x1b[9m" + result
            if fg != not_fg and bg != not_bg:
                result = f"\x1b[38;{setColor(fg)}\x1b[48;{setColor(bg)}" + result
            if fg == not_fg and bg == not_bg:
                result = f"\x1b[0m" + result
            if fg == not_fg and bg != not_bg:
                result = f"\x1b[48;{setColor(bg)}" + result
            if fg != not_fg and bg == not_bg:
                result = f"\x1b[38;{setColor(fg)}" + result
        
            result += '\x1b[0m'
            return result
    

        
from ..colors import setColor, html_rgb_bg, html_rgb_fg

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Text():
    """
    This class allow you to format text, some formats and effects are not available
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
    """
    
    def __init__(self, text: str,
                fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, 
                underline: bool = False, blink: bool = False, 
                reverse: bool = False, crossed: bool = False):
        self.text = text
        self._text = ' '+text+' '
        self.fg = fg
        self.fg_rgb = html_rgb_fg(fg)
        self.bg = bg
        self.bg_rgb = html_rgb_bg(bg)
        self.bold = bold
        self.italic = italic
        self.blink = blink
        self.underline = underline
        self.reverse = reverse
        self.crossed = crossed
        self.lenght = len(self.text)
        self.styled = Text.setStyle(self, self.text, self.fg, self.bg, 
                                    self.bold, self.italic, self.underline, 
                                    self.blink, self.reverse, self.crossed)

    def setStyle(self, chars, fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        """
        This method set the Style with colors and effect to texts
        """
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
    
    def setText(self, cursor):
        """
        This method transform a string object to a Text object
        """
        if type(cursor) != type(Text('')):
            cursor = Text(str(cursor), fg=self.fg, bg=self.bg)
        if type(cursor) == type(Text('')) and cursor.fg != not_fg and cursor.bg != not_bg:
            cursor = Text(cursor.text, fg=cursor.fg, bg=cursor.bg, 
                            bold=cursor.bold, italic=cursor.italic, underline=cursor.underline, 
                            blink=cursor.blink, reverse=cursor.reverse, crossed=cursor.crossed)
        if type(cursor) == type(Text('')) and cursor.bg == not_bg and cursor.fg != not_fg:
            cursor = Text(cursor.text, bg=self.bg, fg=cursor.fg,
                            bold=cursor.bold, italic=cursor.italic, underline=cursor.underline, 
                            blink=cursor.blink, reverse=cursor.reverse, crossed=cursor.crossed)
        if type(cursor) == type(Text('')) and cursor.fg == not_fg and cursor.bg != not_bg:
            cursor = Text(cursor.text, fg=self.fg, bg=cursor.bg, 
                            bold=cursor.bold, italic=cursor.italic, underline=cursor.underline, 
                            blink=cursor.blink, reverse=cursor.reverse, crossed=cursor.crossed)
        if type(cursor) == type(Text('')) and cursor.fg == not_fg and cursor.bg == not_bg:
            cursor = Text(cursor.text, fg=self.fg, bg=self.bg,
                            bold=cursor.bold, italic=cursor.italic, underline=cursor.underline, 
                            blink=cursor.blink, reverse=cursor.reverse, crossed=cursor.crossed)
        
        return cursor
        
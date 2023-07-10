from .texts import Text
from ..colors import Colors, html_rgb_bg

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Button(Text):
    """
    Generate a Button with its label, this class extend from Text()
    some formats and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    A full list of terminals will be show on https://github.com/FreireAlexander/PyeMenu
    properties:
        label: str         
    ***** Text Style *****
        fg: str -> A color in hexadecimal, much of colors could be found in Colors class 
        bg: str -> A color in hexadecimal, much of colors could be found in Colors class
        bold: bool 
        italic: bool 
        underline: bool 
        blink: bool 
        reverse: bool 
        crossed: bool
        
    PyeMenu version 1.0.0
    """
    def __init__(self, label: str,
                fg: str = Colors.DimGray, bg: str = Colors.BlackOlive,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(label, fg, bg,
                            bold, italic, underline, 
                            blink, reverse, crossed)
        self._text = '['+label+']'
        self._lenght = len(self._text)
        self.noFocus = Text.setStyle(self, self._text, self.fg, self.bg, bold, italic, underline, blink, reverse, crossed)
        self.print = f"{self.noFocus}"
        self.onClick = None

    def click(self):
        """
        This method activate the click mode for the Button
        """
        if self.onClick:
            self.onClick()
    
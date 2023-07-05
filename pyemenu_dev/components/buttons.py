from .texts import Text
from ..colors import Colors, html_rgb_bg

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Button(Text):
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
    def __init__(self, label: str, id=None, 
                name: str='',_class: str='', fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(label, id, name,_class, fg, bg,
                bold, italic, underline, blink, reverse, crossed)
        self._text = ' '+label+' '
        self._lenght = len(self._text)
        self.noFocus = Text.setStyle(self, self._text, self.fg, self.bg, bold, italic, underline, blink, reverse, crossed)
        self.print = f"{self.noFocus}"
        self.focus = Text.setStyle(self, self._text, self.fg, Colors.GreenYellow, bold, italic, underline, blink, reverse, crossed)
        self.focus_bg_rgb = html_rgb_bg(Colors.GreenYellow)
        self.print_focus =  f"{self.focus}"
        self.onClick = None

    def click(self):
        if self.onClick:
            self.onClick()
    
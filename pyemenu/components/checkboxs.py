from .texts import Text

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Checkbox(Text):
    """
    Generate a Checkbox with its label, this class extend from Text()
    some formats and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    A full list of terminals will be show on https://github.com/FreireAlexander/PyeMenu
    properties:
        text: str
        box: str=' ' -> Indicate if the checkbox is selected or not by the default is an empty space      
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
    def __init__(self, label: str, box: str=' ', 
                fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(label, fg, bg,
                bold, italic, underline, blink, reverse, crossed)
        self._text = ' '+label+' '
        self._lenght = len(self._text)
        self.styled = Text.setStyle(self, self._text, self.fg, self.bg, bold, italic, underline, blink, reverse, crossed)
        self.box = box
        self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                    +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                    +"\x1b[0m"
    
    def onSelect(self):
        """
        This method mark or unmark the checkbox
        when it's marked the box parameter is equal to * 
        """
        if self.box == ' ':
            self.box = '*'
            self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                    +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                    +"\x1b[0m"
        else:
            self.box = ' '
            self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                    +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                    +"\x1b[0m"
    
    def clear(self):
        """
        this method unmark the checkbox 
        """
        self.box = ' '
        self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                +"\x1b[0m"
from .texts import Text

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Title(Text):
    """
    This class allow you to format a Title, this class extend from Text()
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
    def __init__(self, 
                    text: str,
                    fg: str = not_fg,
                    bg: str = not_bg,
                    bold: bool = False,
                    italic: bool = False,
                    underline: bool = False,
                    blink: bool = False,
                    reverse: bool = False,
                    crossed: bool = False):
        super().__init__(text, fg, bg, 
                        bold, italic, underline, blink, 
                        reverse, crossed)
        self.tilte_text = ' '+text+' '
        self.lenght = len(self.tilte_text)
        self.formatted = self.tilte_text
        self._fg = fg
        self._bg = bg
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
    
    def print_title(self, align: str = 'center',
                decorator: str = '',
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
        if type(decorator) != type(Text('')):
            decorator = Text(str(decorator), fg=self._fg, bg=self._bg)
        if type(decorator) == type(Text('')) and decorator._bg == not_bg and decorator._fg != not_fg:
            decorator = Text(decorator.text, bg=self._bg, fg=decorator._fg)
        if type(decorator) == type(Text('')) and decorator._fg == not_fg and decorator._bg != not_bg:
            decorator = Text(decorator.text, fg=self._fg, bg=decorator._bg)
        if type(decorator) == type(Text('')) and decorator._fg == not_fg and decorator._bg == not_bg:
            decorator = Text(decorator.text, fg=self._fg, bg=self._bg)
        spaces = (width-self.lenght)
        if type(decorator)==type('str'):
            if align == 'center':
                if spaces%2==0:
                    title_text = f"{spaces//2*decorator}"+f"{self.text}"+f"{spaces//2*decorator}"
                else:
                    title_text = f"{(spaces//2+1)*decorator}"+f"{self.formatted}"+f"{spaces//2*decorator}"
            if align == 'right':
                title_text = f"{spaces*decorator}"+f"{self.formatted}"
            if align == 'left':
                title_text = f"{self.formatted}"+f"{spaces*decorator}"   
        if type(decorator)==type(Text('')):
            if align == 'center':
                if spaces%2==0:
                    title_text = f"{spaces//2*decorator.formatted}"+f"{self.formatted}"+f"{spaces//2*decorator.formatted}"
                else:
                    title_text = f"{(spaces//2+1)*decorator.formatted}"+f"{self.formatted}"+f"{spaces//2*decorator.formatted}"
            if align == 'right':
                title_text = f"{spaces*decorator.formatted}"+f"{self.formatted}"
            if align == 'left':
                title_text = f"{self.formatted}"+f"{spaces*decorator.formatted}"
        
        if padding_up and padding_bottom:
            print(f"{self.bg}{width*' '}")
            print(f"{title_text}")
            print(f"{self.bg}{width*' '}", end='')
        elif padding_up:
            print(f"{self.bg}{width*' '}")
            print(f"{title_text}", end='')
        elif padding_bottom:
            print(f"{title_text}")
            print(f"{self.bg}{width*' '}", end='')
        else: print(title_text, end='')

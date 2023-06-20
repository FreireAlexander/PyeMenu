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
    def __init__(self, text: str, id=None,
                name: str='',_class: str='', fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(text, id, name,_class, fg, bg,
                bold, italic, underline, blink, reverse, crossed)
        self.title_text = ' '+text+' '
        self._lenght = len(self.title_text)
        self.styled = Text.style(self, self.title_text, self.fg, self.bg, 
                                 self.bold, self.italic, self.underline, self.blink, self.reverse, self.crossed)
        
    
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
        if type(decorator) != type(Text('')):
            decorator = Text(str(decorator), fg=self.fg, bg=self.bg)
        if type(decorator) == type(Text('')) and decorator.bg != not_bg and decorator.fg != not_fg:
            decorator = Text(decorator.text, bg=decorator.bg, fg=decorator.fg)
        if type(decorator) == type(Text('')) and decorator.bg == not_bg and decorator.fg != not_fg:
            decorator = Text(decorator.text, bg=self.bg, fg=decorator.fg)
        if type(decorator) == type(Text('')) and decorator.fg == not_fg and decorator.bg != not_bg:
            decorator = Text(decorator.text, fg=self.fg, bg=decorator.bg)
        if type(decorator) == type(Text('')) and decorator.fg == not_fg and decorator.bg == not_bg:
            decorator = Text(decorator.text, fg=self.fg, bg=self.bg)
        spaces = (width-self._lenght)
        if type(decorator)==type('str'):
            if align == 'center':
                if spaces%2==0:
                    title_text = f"{spaces//2*decorator}"+f"{self.text}"+f"{spaces//2*decorator}"
                else:
                    title_text = f"{(spaces//2+1)*decorator}"+f"{self.styled}"+f"{spaces//2*decorator}"
            if align == 'right':
                title_text = f"{spaces*decorator}"+f"{self.styled}"
            if align == 'left':
                title_text = f"{self.styled}"+f"{spaces*decorator}"   
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


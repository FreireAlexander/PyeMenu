from pyemenu import Colors
from pyemenu import Text, Title, Menu

def main():
    foreground = Colors.BlackOlive
    background = Colors.GhostWhite
    language1 = Text('Python')
    language2 = Text('JavaScript')
    language3 = Text('Java')
    language4 = Text('C++')
    language5 = Text('C#')
    language6 = Text('Swift')
    language7 = Text('Go')
    language8 = Text('Kotlin')
    options = [
                language1, language2, language3, language4,
                language5, language6, language7, language8
                ]
    title = Title('What is your favorite?', fg=Colors.DarkBlue, bold=True)
    cursor = Text('>>', fg=Colors.DarkBlue)
    menu = Menu(options, title=title, cursor=cursor, fg=foreground, bg=background)
    menu.print(
                wrap=3,
                highlight=True,
                title_align='center',
                title_decorator='*',
                title_padding_bottom=True, 
                padding_bottom=True,
                padding_up=True
                )
    print(f"\nThe selected value is: {menu.answer}")

if __name__ == '__main__':
    main()
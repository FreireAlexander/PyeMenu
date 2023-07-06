import pyemenu as pyemenu 
from pyemenu import Colors, Title, Text, Menu, Checkboxlist, Form, Entry, Checkbox, Button
from pyemenu import getKeyboard, setCursor, clear_screen
from readchar import key


def random_number(texto):
    import random

    print(random.randint(10, 2000))
    print(f"El texto es una cosa {texto}")


def main():
    foreground = Colors.BlueViolet
    background = Colors.AntiqueWhite
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
    title = Title('What is your favorite?', fg=Colors.DarkGreen)
    cursor = Text('>>', fg=Colors.DarkBlue)
    clear = Button("Clear")
    menu1 = Menu(options, title=title, cursor=cursor, fg=foreground, bg=background)
    value = menu1.print(
                wrap=3,
                highlight=True,
                title_align='center',
                title_decorator='*',
                title_padding_bottom=True, 
                padding_bottom=True,
                padding_up=True
                )
    
    if value == None:
        print("No has seleccionado nada")
        print(clear.print)
    else:
        print(f"el valor seleccionado fue: {value}")
        print(clear.print)
        clear.onClick = lambda: random_number(menu1.options[2].styled)
        clear.click()
        print(f"el valor seleccionado fue: {menu1.selected}")

if __name__ == '__main__':
    main()
import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Form
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.BlueViolet
    background = Colors.AntiqueWhite
    name = Text('Name')
    last_name = Text('Last Name')
    age = Text('Age')
    options = [name, last_name, age]
    title = Title('New User')
    cursor = Text('=>')
    menu1 = Form(options, title=title, cursor=cursor, fg=foreground, bg=background)
    # Initialazing Variables
    pointer = 0
    wrap = 2
    keyboard = ''
    selected = Text('')
    decorator = Text('+')
    while True:
        clear_screen()
        menu1.print(pointer=pointer, 
                    keyboard=keyboard, 
                    wrap=wrap,
                    highlight=True,
                    fg_hl=Colors.black, 
                    bg_gl=Colors.LimeGreen,
                    title_decorator=decorator,
                    title_align='center', 
                    padding_bottom=True,
                    padding_up=True
                    )
        selected = menu1.json
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.entries, wrap)
        if keyboard in ["q", "Q"]:
            break
    
    print(f"Form registered: {selected}")
    

if __name__ == '__main__':
    main()
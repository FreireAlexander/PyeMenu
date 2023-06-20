import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Form, Entry
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.green
    background = Colors.white
    name = 'Name_Largo'
    last_name = Text('Last Name background', bg=Colors.Navy)
    last_name2 = Text('Last Name2', fg=Colors.Navy)
    age = Entry('Age', bg=Colors.yellow, placeholder_bg=Colors.purple)
    options = [name, last_name, age, last_name2]
    title = Title('New User')
    cursor = Text('=>')
    menu1 = Form(options, title=title, cursor=cursor, fg=foreground, bg=background, placeholder_bg=Colors.red)
    # Initialazing Variables
    pointer = 0
    wrap = 2
    keyboard = ''
    selected = Text('')
    decorator = Text('+')
    while True:
        #clear_screen()
        """
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
        selected = menu1.survey
        """
        print(f"{age.print}Hola")
        for item in menu1.items2:
            print(item.print)

        print(f"Max len item: {menu1.max_len_item}")
        print(menu1.items2)
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.items2, wrap)
        if keyboard in ["q", "Q"]:
            break
    
    print(f"Form registered: {selected}")
    

if __name__ == '__main__':
    main()
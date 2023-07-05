import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Form, Entry, Checkbox, Button
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.green
    background = Colors.white
    name = 'Name'
    surname = Text('Surname', fg=Colors.red, bg=Colors.Navy)
    last_name = Text('Last', fg=Colors.Navy)
    age = Entry('Age', validation='int',
                 bg=Colors.yellow, placeholder_bg=Colors.pink)
    credit = Checkbox('Card')
    password = Entry('Password', validation='password',
                 bg=Colors.yellow, placeholder_fg=Colors.red)    
    options = [name, surname, last_name, age,password]
    title = Title('New User')
    cursor = Text('~>')
    clear_screen()
    print("Aqui empieza lo del while ")
    Enter = Button('El boton con el texto mas largo del mundo', bg=Colors.BurlyWood)
    menu1 = Form(options, title=title, cursor=cursor, fg=foreground, bg=background,
                 placeholder_fg=Colors.DarkBlue, placeholder_bg=Colors.DimGray,
                 )
    # Initialazing Variables
    pointer = 0
    wrap = 2
    keyboard = ''
    
    while True:
        clear_screen()
        menu1.print(pointer=pointer, 
                    keyboard=keyboard, 
                    wrap=wrap,
                    highlight=True,
                    fg_hl=Colors.black, 
                    bg_hl=Colors.LimeGreen,
                    title_align='center', 
                    padding_bottom=True,
                    padding_up=True
                    )
        print(Enter.print)
        survey = menu1.survey
        print(f"Max len item: {menu1.max_len_item}")
        print(f"Max len Value: {menu1.max_len_values}")
        
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.elements, wrap)
        if keyboard in ["q", "Q"]:
            break
        if keyboard in ["c", "C"]:
            print(menu1.entries[0].print)
            menu1.entries[0].clear()
            print(menu1.entries[0].print)
            input(f"Press Enter")
    
    print(f"User registered: {survey}")
    

if __name__ == '__main__':
    main()
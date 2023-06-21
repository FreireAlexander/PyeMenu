import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Form, Entry
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.green
    background = Colors.white
    name = 'Solo un texto tipo STR'
    last_name = Text('Fondo Azul letras rojas tipo Text', fg=Colors.red, bg=Colors.Navy)
    last_name2 = Text('Letras Azules tipo Text', fg=Colors.Navy)
    age = Entry('Fondo Amarillo y Placeholder fondo rosado tipo Entry', validation='password',
                 bg=Colors.yellow, placeholder_bg=Colors.pink)
    options = [name, last_name, age, last_name2]
    title = Title('Fondo blanco letras verdes place rojo')
    cursor = Text('=>')
    menu1 = Form(options, title=title, cursor=cursor, fg=foreground, bg=background, placeholder_bg=Colors.red)
    # Initialazing Variables
    pointer = 0
    wrap = 2
    keyboard = ''
    selected = Text('')
    while True:
        clear_screen()
        print(f"Max len Value: {menu1.max_len_values}")
        menu1.print(pointer=pointer, 
                    keyboard=keyboard, 
                    wrap=wrap,
                    highlight=False,
                    fg_hl=Colors.black, 
                    bg_hl=Colors.LimeGreen,
                    title_align='center', 
                    padding_bottom=True,
                    padding_up=True
                    )
        selected = menu1.survey
        
        print(f"{title.styled}")
        for item in menu1.entries:
            print(item.print)

        print(f"Max len item: {menu1.max_len_item}")
        print(f"Max len Value: {menu1.max_len_values}")
        
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.entries, wrap)
        if keyboard in ["q", "Q"]:
            break
    
    print(f"Form registered: {selected}")
    

if __name__ == '__main__':
    main()
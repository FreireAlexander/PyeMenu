import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Checkbox
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.Navy
    background = '#5D432C'
    Perro1 = 'French Poodle'
    Perro2 = 'Chihuaha'
    Perro3 = 'Dalmata'
    Perro4 = 'Golden Retriever'
    Perro5 = 'Labrador'
    Perro6 = 'Pastor Alemán'
    Perro7 = 'Akita'
    Perro8 = Text('Galgo', blink=True)
    Perro9 = Text("Perrito Cool", fg=Colors.BlueViolet, bg=Colors.RosyBrown)
    options = [Perro1, Perro2, Perro3, Perro4, Perro5, Perro6, Perro7, Perro8, Perro9, None]
    title = Title('Mejores Perritos', fg=Colors.BlueViolet, bg=Colors.RosyBrown)
    cursor = Text('>>', blink=True, fg=Colors.red)
    menu1 = Checkboxlist(options, multiselect=True ,title=title, cursor=cursor, fg=foreground, bg=background)
    # Initialazing Variables
    pointer = 0
    wrap = 2
    keyboard = ''
    selected = Text('')
    decorator = Text('+', blink=True, bg=Colors.red)
    print(type(Perro9)==type(' '))
    while True:
        clear_screen()
        print([item.text for item in menu1.items])
        menu1.print(pointer=pointer, 
                    keyboard=keyboard, 
                    wrap=wrap,
                    highlight=True,
                    fg_hl=Colors.black, 
                    bg_hl=Colors.LimeGreen,
                    title_decorator=decorator,
                    title_align='center', 
                    padding_bottom=True,
                    padding_up=True
                    )
        
        selected = menu1.choices
        print(f"\nHighlight Value: {selected}")
        print(f"\nHighlight Value: {menu1.max_len_item}")
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.items, wrap)
        if keyboard in ["q", "Q"]:
            break
        if keyboard == key.ENTER:
            break
    
    print(f"Selected Value: {selected}")
    
    

if __name__ == '__main__':
    main()
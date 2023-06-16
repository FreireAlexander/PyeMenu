import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.BlueViolet
    background = Colors.AntiqueWhite
    Perro1 = Text('French Poodle', fg=foreground, bg=background)
    Perro2 = Text('Chihuaha', fg=foreground, bg=background)
    Perro3 = Text('Dalmata', fg=foreground, bg=background)
    Perro4 = Text('Golden Retriever', fg=foreground, bg=background)
    Perro5 = Text('Labrador', fg=foreground, bg=background)
    Perro6 = Text('Pastor Alemán', fg=foreground, bg=background)
    Perro7 = Text('Akita', fg=foreground, bg=background)
    Perro8 = Text('Galgo', fg=foreground, bg=background)
    Perro9 = "Perrito Cool"
    options = [Perro1, Perro2, Perro3, Perro4, Perro5, Perro6, Perro7, Perro8, Perro9, None]
    title = Title('Mejores Perritos',fg=Colors.Navy, bg=background, bold=True,blink=True)
    cursor = Text(' >> ', fg=foreground, bg=background)
    menu1 = Menu(options, title=title, cursor=cursor, fg=Colors.red, bg=Colors.Beige)
    # Initialazing Variables
    pointer = 0
    wrap = 5
    keyboard = ''
    selected = Text('')
    decorator = Text(' ', fg=foreground, bg=background)
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
                    new_line_bottom=False,
                    new_line_up=False
                    )
        selected = menu1.selected
        print(f"\nHighlight Value: {selected.text}")
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.options, wrap)
        if keyboard in ["q", "Q"]:
            break
        if keyboard == key.ENTER:
            break
    
    print(f"Selected Value: {selected.text}")
    print(f"In position {menu1.options.index(selected)}")

if __name__ == '__main__':
    main()
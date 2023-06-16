import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.BlueViolet
    background = Colors.AntiqueWhite
    Perro1 = Text('French Poodle')
    Perro2 = Text('Chihuaha')
    Perro3 = Text('Dalmata')
    Perro4 = Text('Golden Retriever')
    Perro5 = Text('Labrador')
    Perro6 = Text('Pastor Alemán')
    Perro7 = Text('Akita')
    Perro8 = Text('Galgo')
    Perro9 = Text("Perrito Cool")
    options = [Perro1, Perro2, Perro3, Perro4, Perro5, Perro6, Perro7, Perro8, Perro9, None]
    title = Title('Mejores Perritos')
    cursor = Text(' >> ')
    menu1 = Checkboxlist(options, title=title, cursor=cursor, fg=Colors.red, bg=Colors.Beige)
    # Initialazing Variables
    pointer = 0
    wrap = 2
    keyboard = ''
    selected = Text('')
    decorator = Text('+')
    while True:
        clear_screen()
        print([item[0].text for item in menu1.items])
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
        selected = menu1.choices
        print(f"\nHighlight Value: {selected}")
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.items, wrap)
        if keyboard in ["q", "Q"]:
            break
        if keyboard == key.ENTER:
            break
    
    print(f"Selected Value: {selected}")
    

if __name__ == '__main__':
    main()
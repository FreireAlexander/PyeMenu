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
    menu1 = Checkboxlist(options, multiselect=False ,title=title, cursor=cursor, fg=foreground, bg=background)
    # Initialazing Variables
    value = menu1.print(  
                    wrap=2,
                    highlight=True,
                    fg_hl=Colors.black, 
                    bg_hl=Colors.LimeGreen,
                    title_align='center', 
                    padding_bottom=True,
                    padding_up=True
                    )
    
    print(f"Selected Value: {value}")
    print(f"Selected Value: {menu1.choices}")
    

if __name__ == '__main__':
    main()
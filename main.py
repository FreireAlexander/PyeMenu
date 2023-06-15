import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text

def main():
    titulo = Title(' Super titulo ', 'right',
                   decorator='#', 
                   width=40,
                   text_color=Colors.Navy, 
                   background_color=Colors.OrangeRed)
    print(titulo.print)
    print(titulo.lenght)

    char=Text(' ', text_color=Colors.DarkGoldenrod, 
              background_color=Colors.BlueViolet,
              blink=True)
    titulo1 = Title(' Super titulo con Text ', 'center', 
                    decorator=char,
                    width=40,
                    text_color=Colors.Navy, background_color=Colors.OrangeRed)

    print(titulo1.print)
    print(titulo1.lenght)

if __name__ == '__main__':
    main()
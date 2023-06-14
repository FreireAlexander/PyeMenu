import pyemenu_dev as pyemenu 
from readchar import key, readkey, readchar
import functools
import time
from pyemenu_dev import Colors

def main():
    texto1  = pyemenu.Text('Color y Fondo', '#FF0000', Colors.MidnightBlue)
    texto2  = pyemenu.Text('Solo Texto', text_color='#FF000000')
    texto3  = pyemenu.Text('Solo Fondo', background_color=Colors.LimeGreen)
    texto4  = pyemenu.Text('Blinking', blink=True)
    texto5  = pyemenu.Text('Blink and text color', text_color='#FF0000',blink=True)
    texto6  = pyemenu.Text('Bold and text color', text_color='#FF0000',bold=True)
    texto7  = pyemenu.Text('Italic and text color', text_color='#FF0000',italic=True)
    texto8  = pyemenu.Text('Underline and text color', text_color='#FF0000',underline=True)
    texto9  = pyemenu.Text('Reverse and text color', text_color='#FF0000',reverse=True)
    texto10 = pyemenu.Text('Crossed and text color', text_color='#FF0000',crossed=True)
    texto11 = pyemenu.Text('Italic and crossed and text color', text_color='#FF0000',italic=True, crossed=True)
    texto12 = pyemenu.Text('Blink and reverse and text color', text_color=Colors.DarkCyan,blink=True, reverse=True)
    print(texto1.formatted)
    print(texto2.formatted)
    print(texto3.formatted)
    print(texto4.formatted)
    print(texto5.formatted)
    print(texto6.formatted)
    print(texto7.formatted)
    print(texto8.formatted)
    print(texto9.formatted)
    print(texto10.formatted)
    print(texto11.formatted)
    print(texto12.formatted)
    listas = [texto10, texto4, texto12]
    for lista in listas:
        print(f"texto: {lista.text} con formato: {lista.formatted}")
    
    print("")

    for col in range(len(listas)):
        print(f"Posición {col} {listas[col].formatted}")
    
    for col in range(len(listas)):
        print(f"Solo texto => Posición {col} {listas[col].text}")

if __name__ == '__main__':
    main()
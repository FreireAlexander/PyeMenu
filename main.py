import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Form
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    texto = Text('Mi nombre', fg=Colors.Navy, bg=Colors.FloralWhite)
    texto1 = Title('Otra etiqueta', blink=True, italic=True)
    print(f"texto = {texto.text}")
    print(f"Texto 1 = {texto1.text}")
    print(f"Nombre de etiqueta = {texto.name}")
    print(f"La etiqueta 0 es la etiqueta numero {texto._class}")
    print(f"Nombre de texto 1 = {texto1.name}")
    print(f"La etiqueta 1 es la etiqueta numero {texto1._class}")
    print(f"Texto 0 con estilo {texto.formatted}")
    print(f"Texto 1 con estilo {texto1.formatted}")
    texto1.print_title(width=100)

if __name__ == '__main__':
    main()
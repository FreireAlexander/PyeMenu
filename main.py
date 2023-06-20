import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Form, Checkbox, Entry
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key
import getpass
import re


def main():
    valor = -100.300
    if type(valor) not in [type(1), type(12.5)]:
        print("Otro tipo de valor")
    else:
        print(f"es un numero entero o decima {valor}")

if __name__ == '__main__':
    main()
import pyemenu_dev as pyemenu 
from readchar import key, readkey, readchar
import functools
import time

def main():
    entries = ['lado 1', 'lado 2', 'lado 3', 'lado 4']
    entries = [[entry, ''] for entry in entries]
    print(entries)
    buttons = ['perimetro', 'area','salir']
    forms = entries.copy()
    forms.extend(buttons)
    print("Holis")
    print(f"Forms {forms}")
    
    grid_entries = 1
    grid_buttons = 2
    cursor = '-->'
    col = 0
    while True:
        pyemenu.clear()
        print(f"entries: {entries}")
        
        for item in range(len(forms)):
            if forms[item] in entries:
                if item % grid_entries == 0:
                    print("")
                if col==item:
                    print(f"{cursor} {forms[item][0]}: {forms[item][1]} ", end='')
                else:
                    print(f" {forms[item][0]}: {forms[item][1]} ", end='')
            if forms[item] in buttons:
                if item % grid_buttons == 0:
                    print("")
                if col==item:
                    print(f"\t\033[48;2;255;0;0m{forms[item]}\033[0m\t", end='')
                else:
                    print(f"\t{forms[item]}\t", end='')

        
        teclado = pyemenu.input_key()
        col = pyemenu.cursor_position(teclado, col, grid_entries)
        if col > len(forms) - 1:
            col = len(forms)-1
        if teclado in ['q', 'Q']:
            break
        if teclado == key.SPACE and forms[col] in entries:
            pyemenu.clear()
            print(f"Actualizar valor en la columna {col} de : {entries[col]}")
            entries[col][1] = input("Ingrese nuevo valor: ")
            forms[col][1] = entries[col][1]
        
        # Acciones de los botones
        if teclado == key.ENTER and forms[col] in buttons and forms[col] == 'perimetro':
            print(f"Seleccionaste {forms[col]}")
            try:
                print(f"elperimetro es: {sum([float(i[1]) for i in entries])}")
            except:
                print("La embarraste")
            pyemenu.input_key()
        
        if teclado == key.ENTER and forms[col] in buttons and forms[col] == 'multiplicar':
            print(f"Seleccionaste {forms[col]}")
            try:
                print(f"los cuadrados de la lista es: {list(map(lambda i: i**2,list(map(lambda i: int(i),entries))))}")
            except:
                print("La embarraste")
            pyemenu.input_key()
    





if __name__ == '__main__':
    main()
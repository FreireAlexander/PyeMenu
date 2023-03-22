#Libraries
import os
import readchar

# Os.clear functions

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Menu prompt functions
def menu():
    print("Imprimiendo menu")
    clear()
    print(f"Viendo orden de impresión de lineas \n Hola soy Zeustaquiones")
    return

# Function main for testing porpuses
def main():
    menu()

if __name__ == "__main__":
    main()
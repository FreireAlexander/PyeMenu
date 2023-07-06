import pyemenu
from pyemenu import Colors, Title, Text, Menu, Checkboxlist, Form, Entry, Checkbox, Button
from pyemenu import getKeyboard, setCursor, clear_screen
from readchar import key


logo = """
 _____   ___ ______ _____ _   _  ___________ _____ 
/  __ \ / _ \|  _  \  ___| \ | ||  ___| ___ \  _  |
| /  \// /_\ \ | | | |__ |  \| || |__ | |_/ / | | |
| |    |  _  | | | |  __|| . ` ||  __||    /| | | |
| \__/\| | | | |/ /| |___| |\  || |___| |\ \\ \_/ / 
 \____/\_| |_/___/ \____/\_| \_/\____/\_| \_|\___/ 
                                                   
                                                   
"""

Logo = Text(logo, fg=Colors.Azure, bg=Colors.Navy)

def hacealgo(edad):
    if edad.isnumeric() == False:
        edad = 0
    print(f"La edad es {edad} pero su cuadrado es {int(edad)*2}")
    input("Supuestamente hago algo")


def main():
    foreground = Colors.green
    background = Colors.white
    name = 'Name'
    surname = Text('Surname', fg=Colors.red, bg=Colors.Navy)
    last_name = Text('Last', fg=Colors.Navy)
    age = Entry('Age', validation='int',
                 bg=Colors.yellow, placeholder_bg=Colors.pink)
    credit = Checkbox('Card')
    password = Entry('Password', validation='password',
                 bg=Colors.yellow, placeholder_fg=Colors.red)    
    options = [name, surname, last_name, age,credit,password]
    title = Title('New User')
    cursor = Text('~>')
    
    print("Aqui empieza lo del while ")
    Enter = Button('No hace nada', bg=Colors.BurlyWood)
    
    menu1 = Form(options, title=title, cursor=cursor, fg=foreground, bg=background,
                 placeholder_fg=Colors.DarkBlue, placeholder_bg=Colors.DimGray,
                 buttons=[Enter])
    Enter.onClick = lambda: hacealgo(menu1.entries[3].value)
    
    
    
    menu1.print(
                    wrap=2,
                    highlight=True,
                    title_align='center', 
                    padding_bottom=True,
                    padding_up=True,
                    logo=Logo
                    )
        
    print(f"Max len item: {menu1.max_len_item}")
    print(f"Max len Value: {menu1.max_len_values}")
    print(f"Datos del form: {menu1.survey}")
    print(len(logo.splitlines()[1]))
    
    

if __name__ == '__main__':
    main()
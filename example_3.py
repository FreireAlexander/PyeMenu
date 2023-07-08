import pyemenu
from pyemenu import Colors, Title, Text, Menu, Checkboxlist, Form, Entry, Checkbox, Button
from pyemenu import getKeyboard, setCursor, clear_screen
from readchar import key


logo = r"""
  ____        _   _     ____     __     __   U _____ u   __   __ 
 / __"| u  U |"|u| | U |  _"\ u  \ \   /"/u  \| ___"|/   \ \ / / 
<\___ \/    \| |\| |  \| |_) |/   \ \ / //    |  _|"      \ V /  
 u___) |     | |_| |   |  _ <     /\ V /_,-.  | |___     U_|"|_u 
 |____/>>   <<\___/    |_| \_\   U  \_/-(_/   |_____|      |_|   
  )(  (__) (__) )(     //   \\_    //         <<   >>  .-,//|(_  
 (__)          (__)   (__)  (__)  (__)       (__) (__)  \_) (__) 
"""

Logo = Text(logo, fg=Colors.Azure, bg=Colors.Navy)

def main():
    foreground = Colors.BlackOlive
    background = Colors.LightCyan
    placeholder = Colors.LightBlue
    name = Text('Name')
    last_name = Text('Last')
    age = Entry('Age', validation='int')
    email = Entry('Email', validation='email') 
    password = Entry('Password', validation='password')    
    data = [name, last_name, age, email, password]
    title = Title('Creating a New User', italic=True, bold=True)
    cursor = Text('~>')    
    form = Form(data, title=title, cursor=cursor, fg=foreground, bg=background,
                placeholder_bg=placeholder,
                )
    form.print(
                wrap=2,
                highlight=True,
                title_align='center',
                logo=Logo
                )
    print(f"Your Answers are: {form.answer}")

if __name__ == '__main__':
    main()
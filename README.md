[![GitHub Repository](https://img.shields.io/badge/-GitHub-%230D0D0D?logo=github&labelColor=gray)](https://github.com/FreireAlexander/PyeMenu)
[![Latest PyPi version](https://img.shields.io/pypi/v/pyemenu.svg)](https://pypi.python.org/pypi/pyemenu)<br>
[![supported Python versions](https://img.shields.io/pypi/pyversions/pyemenu)](https://pypi.python.org/pypi/pyemenu)
[![Project licence](https://img.shields.io/pypi/l/pyemenu?color=blue)](LICENCE) <br>
[![Number of PyPi downloads](https://img.shields.io/pypi/dd/pyemenu.svg)](https://pypi.python.org/pypi/pyemenu)



# Python - PyeMenu Version 1.0.1
PyeMenu is a simple and really easy kit for developing Text User Interface apps in Python. It can be used to develop minimalist apps that run in terminal emulator.

### News
PyeMenu has a lot of new features, starting by it has color now, it is possible to set foreground and background color to text, titles and widgets, there is a special class call colors to get a lot of colors by name taken from this page [this](https://htmlcolorcodes.com/color-names/).<br>
PyeMenu Version 1.0.1 now includes two principal elements, there are widgets and components.

### Widgets and Components
PyeMenu has two main elements group, it has components and widgets.<br>
- Components: The components are elements used inside the widgets to give color to the text or to the background, depending on the widget that you use it is advisable to use a type of component or another, there are 5 types available, the Text, Title, Checkbox, Entry and Button, these are used depending on the widgets but for general uses you can use the Text class to give color to your texts and to the background.
- Widgets: Widgets are used to create a new window or menu where you can gather information, right now there are three possibilities, the Menu, the Checkboxlist and the Form.
    1. Menu : For select just one option from a list, return a text with the answer
    2. Checkboxlist : For select one or multiselect options from a list, return a list with the answers
    3. Form : For get information from user, it return a dictionary with answers
<br>
Moere information on the Wiki
<br>

## Installation

Simply installing it via `pip`:

```bash
pip install pyemenu
```

or installing manually as follow:

For manually installing this module you can download this repo as .zip file and unzip where You need it

After unziping **Don´t forget to install requierements.txt via pip install as follow**

```python
pip install -r requirements.txt
```

## Requierments

This package uses python module [readchar](https://github.com/magmax/python-readchar/tree/master) in their last version, currently in version 4.0.5.

*Copyright (c) 2014-2022 Miguel Ángel García* 

## Examples

It is better to understand the components and widgets by checking an example.<br>
the following example shows how to make a Menu in a simple way, the Menu class is used for single answer questions among a list of options. The options can be of the Text class or of the text type __str__, if the Text class is used it is possible to specify individually a text color, and a background color with the parameters fg and bg. The colors must be a text string with the hexadecimal format that is usually used in web development with html or using the Colors class you can search a color by its name, the references of the color and its name are in [this page](https://htmlcolorcodes.com/color-names/).

```python
from pyemenu import Colors
from pyemenu import Text, Title, Menu

def main():
    # Foreground and Background Colors using Colors Class
    foreground = Colors.BlackOlive
    background = Colors.GhostWhite
    # Options as a Text() type object 
    # It is possible to use just a str 
    language1 = Text('Python')
    language2 = Text('JavaScript')
    language3 = Text('Java')
    language4 = Text('C++')
    language5 = Text('C#')
    language6 = Text('Swift')
    language7 = Text('Go')
    language8 = Text('Kotlin')
    # Options must be pass as a list
    options = [
                language1, language2, language3, language4,
                language5, language6, language7, language8
                ]
    # The title could be pass a str or a Title
    title = Title('What is your favorite?', fg=Colors.DarkBlue, bold=True)
    # The same by the cursor you want to use
    cursor = Text('>>', fg=Colors.DarkBlue)
    # it is possible to create a Menu just passing the options to be choosen
    menu = Menu(options, title=title, cursor=cursor, fg=foreground, bg=background)
    # The method print is used to show the menu on terminal
    menu.print(
                wrap=3,
                highlight=True,
                title_align='center',
                title_decorator='*',
                title_padding_bottom=True, 
                padding_bottom=True,
                padding_up=True
                )
    # Widgets has a attribute call answer to get data input for the user
    print(f"\nThe selected value is: {menu.answer}")

if __name__ == '__main__':
    main()
```
<br>
if you use this example your output would be something like this:
<br>
<div style="text-align:center">
    <img src="https://github.com/FreireAlexander/PyeMenu/blob/master/images/Example_1.png" alt="Example">
</div>
<p></p>

The next code show an example for creating a checkboxlist menu for selecting multiples options from a list

```python
from pyemenu import Colors, Title, Text, Checkboxlist

def main():
    foreground = Colors.IndianRed
    background = Colors.LightGoldenrodYellow
    dog = Text('My Cool Dog', fg=Colors.DarkBlue, bg=Colors.Gold)
    options = [
        'French Poodle', 'Chihuaha', 'Dalmata',
        'Golden Retriever', 'Labrador', 'German Sheppard',
        'Akita', 'Galgo', dog
    ]
    title = Title('What is your favorite/s dog/s?', fg=Colors.SeaGreen, italic=True)
    cursor = Text('➤', blink=True, fg=Colors.Navy)
    question = Checkboxlist(options, multiselect=True ,
                            title=title, cursor=cursor, fg=foreground, bg=background)
    question.print(  
                    wrap=3, highlight=True,
                    fg_hl=Colors.black, bg_hl=Colors.SkyBlue,
                    title_padding_bottom=True, 
                    title_padding_up=True
                    )
    if question.answer == None:
        print(f"\nDo you really like dogs? ")
    elif len(question.answer)==1:
        print(f"\nMy Favorite Dog is {question.answer}")
    else:
        print(f"\nMy Favorites Dog are {question.answer}")
    

if __name__ == '__main__':
    main()
```

<div style="text-align:center">
    <img src="https://github.com/FreireAlexander/PyeMenu/blob/master/images/Example_2.png" alt="Example">
</div>

<p></p>

One of the new features of PyeMenu is the possibility to create a Form for get survey information or whatever you 
want from the users. So, this example show that it is possible to print a logo or your app above the menu.


```python
from pyemenu import Colors, Title, Text, Form, Entry, Button


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
```

This Form class allows a lot of type of inputs from users even a custom type specifing a custom validation function from the user, for more information visit the Wiki.<br>
<div style="text-align:center">
    <img src="https://github.com/FreireAlexander/PyeMenu/blob/master/images/Example_3a.png" alt="Example">
</div>

<p></p>

You can get something like this<br>
<div style="text-align:center">
    <img src="https://github.com/FreireAlexander/PyeMenu/blob/master/images/Example_3b.png" alt="Example">
</div>

<p></p>

## Wiki
you can view the wiki to understand more about the use of this package. It is really easy and simple for using it.
for more information get a look [here](https://github.com/FreireAlexander/PyeMenu/wiki)

## OS Support
Right now it only been tested on Windows Os and Linux Os, some terminals emulators are not allow to show all text effects as colors, blink, an so on.

## LICENSE

PyeMenu is using a MIT license

*Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
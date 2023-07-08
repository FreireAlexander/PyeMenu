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
        print(f"\nDo you really like dogs?")
    elif len(question.answer)==1:
        print(f"\nMy Favorite Dog is {question.answer}")
    else:
        print(f"\nMy Favorites Dog are {question.answer}")
    

if __name__ == '__main__':
    main()
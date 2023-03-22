import readchar
from os import system, name
import math
'''
UP = "\x1b\x5b\x41"
DOWN = "\x1b\x5b\x42"
LEFT = "\x1b\x5b\x44"
RIGHT = "\x1b\x5b\x43"
'''
# arrow image in ASCII
ARROW_CHAR = "-->"
DIV_CHAR = "|"

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def cursor_UP_DOWN(option):
    key_arrow = readchar.readkey()
    if key_arrow == "\x1b\x5b\x41":
        option -= 1
    elif key_arrow == "\x1b\x5b\x42":
        option += 1
    return option, key_arrow 

def list_menu(Title,args):

    isValid = True
    if len(args) < 1:
        isValid = False
        return "Options must be greater than 1"
    option = 0

    max_string = len(max(args, key = len))
    length_title_frames = ((len(ARROW_CHAR) + max_string + 2) - len(Title))//2
    while isValid:

        # Drawing menu
        print("_" * length_title_frames + " {} ".format(Title) + "_" * length_title_frames)
        for a in args:
            if args.index(a) == option:
                print("{}\t{}".format(ARROW_CHAR,a))
            else:
                print("\t{}".format(a))
            #Esc to exit menu or press Enter to select option   
        print("\nEsc to exit or press Enter to select option\n")
        # Catching cursor

        option,key_arrow = cursor_UP_DOWN(option)
        clear()      
        #Validating option
        if option <= -1:
            option = len(args)-1
        elif option > len(args)-1:
            option = 0
        #Enter to select option
        if key_arrow == "\x0d":
            isValid = False
            return option
        #Esc to exit menu and return None, None options selected
        if key_arrow == "\x1b":
            isValid = False
            return None


def cursor_UDLR(option,col):
    key_arrow = readchar.readkey()
    if key_arrow == "\x1b\x5b\x41": #UP
        option -= col
    elif key_arrow == "\x1b\x5b\x42": #DOWN
        option += col
    elif key_arrow == "\x1b\x5b\x43": #RIGHT
        option += 1
    elif key_arrow == "\x1b\x5b\x44": #LEFT
        option -= 1
    return option, key_arrow  


def table_menu_1(col, Title, args):
    isValid = True
    if len(args) < 1:
        isValid = False
        return "Options must be greater than 1"
    # Defining maximun string len
    max_string = len(max(args, key = len))
    length_title_frames = ((len(ARROW_CHAR) + max_string + 2)*col - len(Title))//2
    option = 0
    while isValid:
        # Drawing menu
        print("_" * length_title_frames + " {} ".format(Title) + "_" * length_title_frames) 
        for a in args:
            num = len(a)
            if args.index(a)%col == 0 and args.index(a) != 0:
                print("")

            if args.index(a) == option:
                print("{} {}".format(ARROW_CHAR,a)+" "*(max_string-num)+" ",end="")
            else:
                print(" "*len(ARROW_CHAR)+" {}".format(a)+" "*(max_string-len(a))+" ", end="")     
            #Esc to exit menu or press Enter to select option    
        print("\n\nEsc to exit or press Enter to select option\n")
        # Catching cursor
        option,key_arrow = cursor_UDLR(option,col)
        clear()
        # validation option [0:max]
        if option >= len(args):
            if key_arrow in ["\x1b\x5b\x43"]:
                option = 0
            elif key_arrow in ["\x1b\x5b\x42"]:
                option = option - col
        elif option <= -1:
            if key_arrow in ["\x1b\x5b\x44"]:
                option = len(args) - 1
            elif key_arrow in ["\x1b\x5b\x41"]:
                option = option + col
        #Enter to select option
        if key_arrow == "\x0d":
            isValid = False
            return option
        #Esc to exit menu and return None, None options selected
        if key_arrow == "\x1b":
            isValid = False
            return None

def input_key(key_arrow):
    if key_arrow == "\x1b\x5b\x41": #UP
        return "ARRIBA"
    elif key_arrow == "\x1b\x5b\x42": #DOWN
        return "ABAJO"
    elif key_arrow == "\x1b\x5b\x43": #RIGHT
        return "DER"
    elif key_arrow == "\x1b\x5b\x44": #LEFT
        return "IZQ"


def table_menu_2(col, Title,args):
    isValid = True
    if len(args) < 1:
        isValid = False
        return "Options must be greater than 1"
    #Calculating numbers of row
    row = math.ceil(len(args)/col)
    # Defining maximun string len
    max_string = len(max(args, key = len))
    length_title_frames = ((len(ARROW_CHAR) + max_string + 2)*col - len(Title))//2
    option = 0
    while isValid:
        # Drawing menu
        print("_" * length_title_frames + " {} ".format(Title) + "_" * length_title_frames)
        for a in args:
            # We need to know the len of string in a for calculating the numbers of spaces
            # to organize the table of options
            num = len(a)
            #Every time we are in first position in a row we need a new line
            if args.index(a)%col == 0 and args.index(a) != 0:
                print("")
            #Positioning arrow in selected
            if args.index(a) == option:
                print("{} {}".format(ARROW_CHAR,a)+" "*(max_string-num)+" ",end="")
            else:
                print(" "*len(ARROW_CHAR)+" {}".format(a)+" "*(max_string-len(a))+" ", end="")
            #Esc to exit menu or press Enter to select option   
        print("\n\nEsc to exit or press Enter to select option\n")
        # Catching cursor
        option,key_arrow = cursor_UDLR(option,col)
        clear()
        # Catching corner position for first and first in last row
        # for controlling events in this position
        corner = False
        zero_corner_up = False
        zero_corner_left = False

        if option == len(args) and key_arrow == "\x1b\x5b\x43":
            corner = True
        elif option == -col and key_arrow == "\x1b\x5b\x41":
            zero_corner_up = True
        elif option == -1 and key_arrow == "\x1b\x5b\x44":
            zero_corner_left = True
        '''Before validating options, I verify if option is in first row and 
            and input key was UP, then the numbers are negative. Well, later it is just
            stand from the first element of the last row and move as many option as the 
            option we are stand in first row
        '''
        if option in range (-col, 0):
            option = option + col
            if option != 0:
                if len(args)%col == 0:
                    option = option + row*col-col
                elif row*col-col + option > len(args) - 1:
                    option = row*col-col + option - col
                else:
                    option = row*col-col + option
            elif option > 0:
               option = option

        # validation option for being between [0:max]
        if option > len(args) - 1:
            option = option%col
        elif option <= -1:
            if key_arrow in ["\x1b\x5b\x44"]:
                option = 0

        #Validation by movements
        if key_arrow == "\x1b\x5b\x44": #Izquierda
            if (option+1)%col == 0:
                option = option + col
        elif key_arrow == "\x1b\x5b\x43": # Derecha
            if (option-1)%col == col - 1:
                option = option - col

        # Second validation to assure option is inside posible for choicing
        if option > len(args) - 1:
            if key_arrow in ["\x1b\x5b\x44"]:
                option = len(args) - 1                    
            else:    
                option = option%col
        elif option <= -1:
            if key_arrow in ["\x1b\x5b\x44"]:
                option = 0
            elif key_arrow in ["\x1b\x5b\x41"]:
                option = option + col

        # Validation of special cases first postion and and firs porsition at last row
        if corner:
            option = (row*col)-col  
        if zero_corner_up:
            option =  (row*col)-col
        if zero_corner_left:
            option = col - 1
        
        #Enter to select option
        if key_arrow == "\x0d":
            isValid = False
            return option
        #Esc to exit menu and return None, None options selected
        if key_arrow == "\x1b":
            isValid = False
            return None

def table_menu_3(col,div, Title,args):
    
    isValid = True
    if len(args) < 1:
        isValid = False
        return "Options must be greater than 1"
    #Calculating numbers of row
    row = math.ceil(len(args)/col)
    # Defining maximun string len
    max_string = len(max(args, key = len))
    length_title_frames = ((len(ARROW_CHAR) + max_string + 2)*col - len(Title))//2 + 1
    option = 0
    while isValid:
        # Drawing menu
        print("_" * length_title_frames + " {} ".format(Title) + "_" * length_title_frames)
        space_len = len(ARROW_CHAR) + max_string + 1 - 4
        for a in args:
            # We need to know the len of string in a for calculating the numbers of spaces
            # to organize the table of options
            num = len(a)

            div_char = " "
            if args.index(a)%col == div - 1 or args.index(a)%col == col-1:
                div_char = DIV_CHAR 

            #Every time we are in first position in a row we need a new line
            if args.index(a)%col == 0 and args.index(a) != 0:
                print("")
            #Positioning arrow in selected
            if args.index(a) == option:
                print("{} {}".format(ARROW_CHAR,a)+" "*(space_len-num)+"{}".format(div_char)+" ",end="")
            else:
                print(" "*len(ARROW_CHAR)+" {}".format(a)+" "*(space_len-num)+"{}".format(div_char)+" ", end="")
            #Esc to exit menu or press Enter to select option   
        print("\n\nEsc to exit or press Enter to select option\n")
        # Catching cursor
        option,key_arrow = cursor_UDLR(option,col)
        clear()
        # Catching corner position for first and first in last row
        # for controlling events in this position
        corner = False
        zero_corner_up = False
        zero_corner_left = False

        if option == len(args) and key_arrow == "\x1b\x5b\x43":
            corner = True
        elif option == -col and key_arrow == "\x1b\x5b\x41":
            zero_corner_up = True
        elif option == -1 and key_arrow == "\x1b\x5b\x44":
            zero_corner_left = True
        '''Before validating options, I verify if option is in first row and 
            and input key was UP, then the numbers are negative. Well, later it is just
            stand from the first element of the last row and move as many option as the 
            option we are stand in first row
        '''
        if option in range (-col, 0):
            option = option + col
            if option != 0:
                if len(args)%col == 0:
                    option = option + row*col-col
                elif row*col-col + option > len(args) - 1:
                    option = row*col-col + option - col
                else:
                    option = row*col-col + option
            elif option > 0:
               option = option

        # validation option for being between [0:max]
        if option > len(args) - 1:
            option = option%col
        elif option <= -1:
            if key_arrow in ["\x1b\x5b\x44"]:
                option = 0

        #Validation by movements
        if key_arrow == "\x1b\x5b\x44": #Izquierda
            if (option+1)%col == 0:
                option = option + col
        elif key_arrow == "\x1b\x5b\x43": # Derecha
            if (option-1)%col == col - 1:
                option = option - col

        # Second validation to assure option is inside posible for choicing
        if option > len(args) - 1:
            if key_arrow in ["\x1b\x5b\x44"]:
                option = len(args) - 1                    
            else:    
                option = option%col
        elif option <= -1:
            if key_arrow in ["\x1b\x5b\x44"]:
                option = 0
            elif key_arrow in ["\x1b\x5b\x41"]:
                option = option + col

        # Validation of special cases first postion and and firs porsition at last row
        if corner:
            option = (row*col)-col  
        if zero_corner_up:
            option =  (row*col)-col
        if zero_corner_left:
            option = col - 1
        
        #Enter to select option
        if key_arrow == "\x0d":
            isValid = False
            return option
        #Esc to exit menu and return None, None options selected
        if key_arrow == "\x1b":
            isValid = False
            return None
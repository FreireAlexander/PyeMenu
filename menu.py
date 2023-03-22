#Libraries
import os
import readchar
from readchar import key
import old_menus as table_menus


# Global Variables
ENTER = key.ENTER
UP = key.UP
DOWN = key.DOWN


# Os.clear functions
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Validate type of parameters
def validate_options(options):
    if type(options) != type([]):
        raise TypeError("Options must be a list")
    if len(options) == 0:
        raise ValueError("Options must contains most than zero values")

# Validate minimun and maximun value of position in list
def validate_position(position, options):
    if position < 0:
        return 0
    if position > len(options) - 1:
        return len(options) - 1
    
    return position

# Cursor position
def cursor_position(key, position):
    if key == UP:
        position -=1
    if key == DOWN:
        position +=1
    return position

# Print Title with Frames
def print_title(title, options, cursor):
    options_to_string = list(map(lambda x: str(x), options))
    max_len_string = len(max(options_to_string, key=len))
    len_title_frame = (len(cursor) + max_len_string - len(title))//2
    print(f"{len_title_frame*'_'} "+f"{title}"+f" {len_title_frame*'_'}"+"\n")

# Menu prompt functions
def menu_list(title, options, cursor = "🢧 "):
    validate_options(options)
    position = 0
    while True:
        clear()
        print_title(title, options, cursor)
        for option in options:
            if position == options.index(option):
                print(f"{cursor} {option}")
            else:
                print(f"{' '*(len(cursor)+1)}"+f"{option}")

        print(f"\n Press ENTER to select an option")
        print(f"\n Press (q) to exit")
        key = readchar.readkey()
        position = validate_position(cursor_position(key, position), options)

        if key in ["q", "Q"]:
            return -1
        if key == ENTER:
            return options[position]
        
# Function main for testing porpuses
def main():
    options = ["Open",
             "Create",
             "Delete",
             "Restore",
             "Comment"]
    #table_menus.table_menu_2(3, "Zeustaquio", lista)
    choice = menu_list("Title", options)
    print(f"Your choice was {choice}")
    
if __name__ == "__main__":
    main()
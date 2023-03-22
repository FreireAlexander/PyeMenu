#Libraries
import os
import readchar
from readchar import key
import old_menus as table_menus


# Global Variables
ENTER = key.ENTER
UP = key.UP
DOWN = key.DOWN
LEFT = key.LEFT
RIGHT = key.RIGHT

# Os.clear functions
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# input key
def input_key():
    print(f"\n\n Press ENTER to select an option")
    print(f" Press (q) to exit")
    return readchar.readkey()

# Validate type of parameters
def validate_options(options):
    if type(options) != type([]):
        raise TypeError("Options must be a list")
    if len(options) == 0:
        raise ValueError("Options must contains most than zero values")
    
    return list(map(lambda x: str(x), options))

# Validate minimun and maximun value of position in list
def validate_position(position, options):
    if position < 0:
        return 0
    if position > len(options) - 1:
        return len(options) - 1
    
    return position

# Cursor position on menu as table
def cursor_position(key, position, col):
    if key == UP:
        position -=col
    if key == DOWN:
        position +=col
    if key == LEFT:
        position -=1
    if key == RIGHT:
        position +=1

    return position

# Print title for table menu in CLI
def print_title(title, options, col, cursor):
    max_len_string = len(max(options, key=len))
    len_title_frame = ((len(cursor) + max_len_string + 1)*col - len(title))//2
    print(f"{len_title_frame*'_'} "+f"{title}"+f" {len_title_frame*'_'}")

# Print menu as table in CLI
def menu_list(title, options, col = 1, cursor = "🢧 "):
    options = validate_options(options)
    max_len_option = len(max(options, key = len))
    position = 0
    while True:
        clear()
        print_title(title, options, col, cursor)
        for option in options:
            if options.index(option) % col == 0:
                print("")
            if position == options.index(option):
                print(f" {cursor} {option}"+f"{(max_len_option-len(option))*' '}", end="")
            else:
                print(f" {' '*(len(cursor)+1)}"+f"{option}"+f"{(max_len_option-len(option))*' '}", end="")

        key = input_key()
        position = validate_position(cursor_position(key, position, col), options)

        if key in ["q", "Q"]:
            return -1
        if key == ENTER:
            return options[position]

    return
        
# Function main for testing porpuses
def main():
    options = ["Open",
             "Create",
             "Delete",
             "Restore",
             "Comment"]
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    choice = menu_list("Title", options)
    choice = menu_list("Title", options, col=3)
    print(f"Your choice was {choice}")
    
if __name__ == "__main__":
    main()
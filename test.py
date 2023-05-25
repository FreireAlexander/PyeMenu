# Libraries 
import menu
import time

# Function main for testing porpuses
# Function main for testing porpuses
def main():
    options = [
             "Poodle",
             "Chihuaha",
             "Golden",
             "Dalmata",
             "Galgo",
             "German Shepard",
             "Border Collie",
             "Corgie",
             "Mine"]
    choice = menu.print_menu("Title", options)
    print(f"Your choice was {choice}")
    time.sleep(2)
    choice = menu.print_menu("Title", options, col=3)
    print(f"Your choice was {choice}")
    time.sleep(2)
    choice = menu.print_menu("Best Dog", options, col=4, cursor=">===>>")
    print(f"Your choice was {choice}")

if __name__ == "__main__":
    main()


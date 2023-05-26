# Libraries 
import pyemenu
import time

# Function main for testing porpuses
# Function main for testing porpuses
def main():
    options = [
             "Insert a new user",
             "Delete an existing user",
             "Find an existing user",
             "Updatte information for an existing user"]
    choice = pyemenu.menu("My App", options, col=1)
    print(f"Your choice was {choice}")
    time.sleep(2)
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
    choice = pyemenu.menu("What is your favorite Dog", options, col = 3)
    print(f"Your choice was {choice}")
    time.sleep(2)
    options = [
             "North",
             "South",
             "East",
             "West"]
    choice = pyemenu.menu("Where do you want to go?", options, col=2, cursor="󰮯 ")
    print(f"Your choice was {choice}")

if __name__ == "__main__":
    main()
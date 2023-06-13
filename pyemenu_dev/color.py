"""
    This module contain the color value.

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""
'''
FG  BG  NAME
30 	40 	Black 	
31 	41 	Red 	
32 	42 	Green 	
33 	43 	Yellow 	
34 	44 	Blue 	
35 	45 	Magenta 	
36 	46 	Cyan 	
37 	47 	White 	
90 	100 	Bright Black (Gray) 	
91 	101 	Bright Red 	
92 	102 	Bright Green 	
93 	103 	Bright Yellow 	
94 	104 	Bright Blue 	
95 	105 	Bright Magenta 	
96 	106 	Bright Cyan 	
97 	107 	Bright White 	

print("Freire\n")
    print('Hola\x1b[1m Boldt Text\x1b[0m')
    print('Hola\x1b[2m Faint Text\x1b[0m')
    print('Hola\x1b[3m Italic Text\x1b[0m')
    print('Hola\x1b[4m UnderLine Text\x1b[0m')
    print('Hola\x1b[5m Blink Text\x1b[0m')
    print('Hola\x1b[7m Reverse Text\x1b[0m')
    print('Hola\x1b[9m Crossed Text\x1b[0m')
    print('Hola\x1b[21m Double Underline Text\x1b[0m')
    print('Hola\x1b[48;2;255;0;0m\x1b[38;2;0;0;255m BG RED FG BLUE\x1b[0m')
    BG = '199;21;133'
    FG = '0;100;0'
    print(f'Hola\x1b[48;2;{BG}m\x1b[38;2;{FG}m Custom BG in FG \x1b[0m')
    print(f'Hola\x1b[48;2;{BG}m\x1b[38;2;{FG}m\x1b[3m Custom BG in FG \x1b[0m')

'''

# SGR color constants
# rene-d 2018

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    # cancel SGR codes if we don't write to a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        # set Windows console in VT mode
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32


if __name__ == '__main__':
    for i in dir(Colors):
        if i[0:1] != "_" and i != "END":
            print("{:>16} {}".format(i, getattr(Colors, i) + i + Colors.END))
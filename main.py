import pyemenu

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


def main():
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


if __name__ == '__main__':
    main()
import pyemenu

def main():
    print("HOla freire")
    pyemenu.clear()
    print("No me borraste a mí")
    pyemenu.print_title("Holaaaa", sep='.', position='right')
    number_chars = 10
    title = "freire"
    title = " "+title+" "
    char = "-"
    print(f'{title:{char}^{number_chars}}')


if __name__ == '__main__':
    main()
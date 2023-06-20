

nf = '\x1b[0m'
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Screen():
    '''
    This class allow to create a CheckBoxList for choice 
    multiple option 
    '''
    def __init__(self, blocks: list, 
                title: str = '', cursor: str = '-->',
                fg: str = not_fg, bg: str = not_bg):
        self.blocks = blocks

"""
def move_position(key, array, row, col):
    if key == UP:
        col -= array
    if key == DOWN:
        col += array
    if key == LEFT:
        col -=1
    if key == RIGHT:
        col +=1
    if key == FORWARD:
        row +=1
    if key == BACKWARD:
        row -=1

    if col<0:
        col=0
    if row<0:
        row=0
    
    return row, col


def print_screen():
    matrix = [
        [1,2,3,4,5]
    ]
    
    cursor = '-->'
    fila = 0 
    columna = 0
    num_filas_screen = len(matrix)
    num_col_screen = len(max(matrix, key=lambda i: len(i)))
    len_blocks = list(map(lambda i: len(i),matrix))
    out_text = ''
    while True:
        pyemenu.clear()
        print(f"Numero de filas en la pantalla: {num_filas_screen}") # numero de filas
        print(f"Numero de columnas del bloque más grande: {num_col_screen}") # numero de columnas
        print(f"Longitudes de los block en el screen {len_blocks}")
        print(f"Posición en la matrix de la pantalla antes del For {fila}, {columna}\n")
        print(f"{out_text}")
        
        grid = 3
        for row in range(len(matrix)):
            print(f"\nfila {row} con longitud {len_blocks[row]}")
            if fila > num_filas_screen-1:
                    fila = num_filas_screen-1

            for col in range(len(matrix[row])):
                if fila == row:
                    if columna > len(matrix[row])-1:
                        columna = len(matrix[row])-1
                if col % grid == 0:
                    print("")
                if col==columna and fila == row:
                    print(f"{cursor}  [{row},{col}] {matrix[row][col]} ", end="")
                else:
                    print(f"[{row},{col}] {matrix[row][col]} ", end="")
            
            print("")

        
        teclado = readkey()
        out_text = f"Posición en la matrix de la pantalla DESPUES del For {fila}, {columna}"
        
        
        fila, columna = move_position(teclado, grid, fila, columna)
        print(f"teclado = {teclado}")
        
        if teclado in ["q", "Q"]:
            break 
        if teclado == FORWARD:
            print("hacia delante")
        if teclado == BACKWARD:
            print("hacia atrás")
    
    #pyemenu.menu('Cool', matrix)
"""

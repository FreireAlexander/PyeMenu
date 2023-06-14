def main():
    entries = ['\033[38;2;255;0;0mlado 1\033[0m', 'lado 2', 'lado 3', 'lado 4']
    entries = [[entry, ''] for entry in entries]
    print(entries)
    print("Holis")
    selected = []
    
    grid_entries = 2
    cursor = '-->'
    col = 0
    while True:
        pyemenu.clear()
        print(f"entries: {entries}")
        print(f"Selected: {selected}")
        
        for item in range(len(entries)):
            if item % grid_entries == 0:
                print("")
            if col==item:
                print(f"{cursor} [{entries[item][1]}] {entries[item][0]} ", end='')
            else:
                print(f" [{entries[item][1]}] {entries[item][0]} ", end='')
            

        
        teclado = pyemenu.input_key()
        col = pyemenu.cursor_position(teclado, col, grid_entries)
        if col > len(entries) - 1:
            col = len(entries)-1
        if teclado in ['q', 'Q']:
            break
        if teclado == key.SPACE:
            if entries[col][0] not in selected:
                entries[col][1] = '*'
                selected.append(entries[col][0])
            elif entries[col][0] in selected:
                entries[col][1] = ''
                selected.remove(entries[col][0])
            
    
    print(selected)
            

if __name__ == '__main__':
    main()
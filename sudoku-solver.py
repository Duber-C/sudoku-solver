# a very slow sudoku solver


def normalizar(n):
    if n <= 2:
        n = 0
    elif n <= 5:
        n = 3
    elif n <= 8:
        n = 6

    return(n)


def fila(x, y, sudoku):
    return(sudoku[y])


def columna(x, y, sudoku):
    s = []
    for i in range(9):
        s.append(sudoku[i][x])

    return(s)


def cuadro(x, y, sudoku):
    x = normalizar(x)
    y = normalizar(y)

    s = []
    for i in range(3):
        for j in range(3):
            s.append(sudoku[i + y][j + x])

    return(s)


def num_faltantes(lista):
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in lista:
        if i in num:
            num.remove(i)
    return(num)


def enumerar(sudoku):
    s = []
    for y, i in enumerate(sudoku):
        l = []
        for x, j in enumerate(i):
            if j == '-' or len(j) > 1:
                l.append(num_faltantes(
                    cuadro(x, y, sudoku) + columna(x, y, sudoku) + fila(x, y, sudoku)))
            else:
                l.append(j)
        s.append(l)
    return(s)


def simplificar(sudoku, sud):
    for y, i in enumerate(sud):
        for x, j in enumerate(i):
            if len(j) == 1:
                sudoku[y][x] = j[0]
    return(sudoku)


def tiene_duplicados(lista):
    for i in lista:
        if (i != '-') and not (isinstance(i, list)):
            if lista.count(i) > 1:
                return(True)
    return(False)


def esta_bien(sudoku):
    for x in ([0, 3, 6]):
        for y in ([0, 3, 6]):
            if tiene_duplicados(cuadro(x, y, sudoku)):
                return(False)

    for y in range(9):
        if tiene_duplicados(fila(0, y, sudoku)):
            return(False)
    for x in range(9):
        if tiene_duplicados(columna(x, 0, sudoku)):
            return(False)
    return(True)


def esta_completo(sudoku):
    for y in sudoku:
        if '-' in y:
            return(False)
    return(True)


def resolver(ind=0):
    x, y = ARBOL_POS[ind]
    dec = ARBOL_DEC[(x, y)]

    for d in dec:
        if esta_completo(SUDOKU) and esta_bien(SUDOKU):
            break

        SUDOKU[y][x] = d

        if esta_bien(SUDOKU):
            if not esta_completo(SUDOKU):
                resolver(ind + 1)

    if not esta_completo(SUDOKU):
        SUDOKU[y][x] = "-"
    return


def imp_matriz(m):
    if isinstance(m, list):
        s = "\n"
        for i in m:
            for j in i:
                s += str(j) + " "
            s += '\n'
        print(s)
    else:
        print(m)



if __name__ == "__main__":
    
    # VARIABLES GLOBALES
    SUDOKU = []
    ARBOL_POS = []
    ARBOL_DEC = {}

    for i in range(9):
        SUDOKU.append([j for j in input(': ')])

    for y, i in enumerate(SUDOKU):
        for x, j in enumerate(i):
            if j == "-":
                ARBOL_POS.append((x, y))
                ARBOL_DEC[(x, y)] = num_faltantes(
                    cuadro(x, y, SUDOKU) + columna(x, y, SUDOKU) + fila(x, y, SUDOKU))

    resolver()
    imp_matriz(SUDOKU)
    print(esta_bien(SUDOKU))

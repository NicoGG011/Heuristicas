##########################################################################
# Programación dinamica
##########################################################################


# ..............................................
# Ejemplo 1: Serie de Fibonacci
# ..............................................


# Iterativo
def Fibonacci(n):
    tabla[0] = 0
    tabla[1] = 1

    for i in range(2, n + 1):
        tabla[i] = tabla[i - 1] + tabla[i - 2]

    return tabla[n]


N = 64
tabla = []
for i in range(N + 1):
    tabla.append(-1)

print(Fibonacci(N))


# # Recursivo
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if tabla[n] != -1:
        return tabla[n]

    tabla[n] = Fibonacci(n - 1) + Fibonacci(n - 2)
    return tabla[n]


N = 64
tabla = []
for i in range(N + 1):
    tabla.append(-1)
print(Fibonacci(N))


# ..............................................
# Ejemplo 2: Ruta de costo mínimo en una matriz
# ..............................................


def MinCostos(costos, m, n):
    rows = len(costos)
    columns = len(costos[0])
    tabla = [[0 for i in range(columns)] for i in range(rows)]

    tabla[0][0] = costos[0][0]

    # Inicializar primera columna
    for i in range(1, m + 1):
        tabla[i][0] = tabla[i - 1][0] + costos[i][0]
        # print('\n', tabla)

    # Inicializar primera fila
    for j in range(1, n + 1):
        tabla[0][j] = tabla[0][j - 1] + costos[0][j]
        # print('\n', tabla)

    # Completar la tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tabla[i][j] = min(tabla[i - 1][j - 1], tabla[i - 1][j], tabla[i][j - 1]) + costos[i][j]
            # print('\n', tabla)

    return tabla[m][n]
    #    return tabla


costos = [[1, 2, 3],
          [4, 8, 2],
          [1, 5, 3]]

print(MinCostos(costos, 2, 2))


#######################################
# Actividad Backtracking
#######################################

def checkFactibilidad(board, N, row, col):
    # Chequear fila lado izquierdo
    for i in range(col):
        if board[row][i] == 1:
            return False

    # chequear diagonal superior del lado izquierdo
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # chquear diagonal inferior del lado izquierdo
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQ(board, N, col):
    # caso base
    if col >= N:
        return True

    else:
        for row in range(N):
            if checkFactibilidad(board, N, row, col):
                board[row][col] = 1

                # llamada recursiva para el resto de las reinas
                if solveNQ(board, N, col + 1) == True:
                    return True

                # si poner una reina en board[i][col] no funciona:
                board[row][col] = 0

        return False


def BacktrakingNQ():
    tablero = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

    N = len(tablero)
    col = 0
    if solveNQ(tablero, N, col) == False:
        print("No existe solucion")
        return False

    for i in range(len(tablero)):
        print(tablero[i])
    return True


BacktrakingNQ()


##################################################
# Actividad Programacion Dinamica
#################################################

def MinimumCost(cost, W):
    INF = 1000000
    n = len(cost)
    # Trabajar solo con los paquetes de naranjas disponibles
    val = list()
    wt = list()
    size = 0
    for i in range(n):
        if cost[i] != -1:
            val.append(cost[i])
            wt.append(i + 1)
            size += 1

    n = size
    tabla = [[0 for i in range(W + 1)] for j in range(n + 1)]

    # Caso base
    tabla[0][0] = 0
    for i in range(1, W + 1):
        tabla[0][i] = INF

        # Completar tabla
    for i in range(1, n + 1):
        for j in range(W + 1):
            # wt[i-1] > j implica que la capacidad de la mochila es inferior al peso del item
            if (wt[i - 1] > j):
                tabla[i][j] = tabla[i - 1][j]

                # determinamos el minimo costo (excluyendo e incluyendo item actual)
            else:
                tabla[i][j] = min(tabla[i - 1][j], tabla[i][j - wt[i - 1]] + val[i - 1])

    if tabla[n][W] == INF:
        return -1
    else:
        #        return tabla
        return tabla[n][W]


cost1 = [1, 2, 3, 4, 5]
W1 = 5

cost2 = [-1, -1, 4, 5, -1]
W2 = 5

resultado = MinimumCost(cost1, W1)
print(resultado)

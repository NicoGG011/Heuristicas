##########################################################################
# Backtraking
##########################################################################


# ................................
# Ejemplo 1: Permutaciones
# ................................

def permutacion(arr, l, r):
    if (l == r):
        print(arr)
    else:
        for i in range(l, r + 1):
            temp = arr[l]
            arr[l] = arr[i]
            arr[i] = temp
            print('Cambio: ', arr)
            permutacion(arr, l + 1, r)

            # Backtracking
            temp = arr[l]
            arr[l] = arr[i]
            arr[i] = temp
            print('Backtracking: ', arr)


instancia1 = [1, 2, 3]
l = 0
r = len(instancia1) - 1

permutacion(instancia1, l, r)


# ................................
# Ejemplo 2: Laberinto
# ................................

def solveLaberinto(laberinto, N, x, y, sol):
    # Verificar si estamos en el destino
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    # Verificar que laberinto[x][y] sea valido
    if x >= 0 and x < N and y >= 0 and y < N and laberinto[x][y] == 1:
        sol[x][y] = 1

        # Avanzar en la direccion de x
        if solveLaberinto(laberinto, N, x + 1, y, sol) == True:
            return True

        # Si en la direccion de x no llegamos a una solucion,
        # avanzar en la direccion de y
        if solveLaberinto(laberinto, N, x, y + 1, sol) == True:
            return True

        # Si avanzar en x o y no funciona, Volver atras (BACKTRACKING)
        sol[x][y] = 0
        return False
    else:
        return False


def Bactrakinglaberinto(laberinto):
    # Creamos arreglo para guardar solucion
    N = len(laberinto)
    sol = [[0 for j in range(N)] for i in range(N)]

    if solveLaberinto(laberinto, N, 0, 0, sol) == False:
        print("No existe solucion")
        return False

    else:
        print("La solucion es:")
        for i in range(len(laberinto)):
            print(sol[i])

        return True


instancia1 = [[1, 0, 0, 0],
              [1, 1, 0, 1],
              [0, 1, 0, 0],
              [1, 1, 1, 1]]

Bactrakinglaberinto(instancia1)




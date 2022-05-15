##########################################################################
# Algoritmos Recursivos
##########################################################################


# .........................................................
# Ejemplo 1: Suma de numeros - Solucion iterativa.
# .........................................................

def sumaIterativa(Numeros):
    suma = 0
    for i in Numeros:
        suma = suma + i
    return suma


Numeros = [5, 2, 7, 4]
resultado = sumaIterativa(Numeros)
print(resultado)


# .........................................................
# EJEMPLO 1: Suma de numeros - Solucion recursiva.
# .........................................................

def sumaRecursiva(Numeros):
    if len(Numeros) == 1:
        suma = Numeros[0]
        return suma
    else:
        suma = Numeros[0] + sumaRecursiva(Numeros[1:])
        return suma


Numeros = [5, 2, 7, 4]
resultado = sumaRecursiva(Numeros)
print(resultado)


# .........................................................
# Ejemplo 2: Factorial factorial de un numero
# .........................................................

def factorialRecursivo(n):
    if n == 1:
        return n
    else:
        return n * factorialRecursivo(n - 1)


numero = 7
resultado = factorialRecursivo(numero)
print(resultado)


# .........................................................
# Ejemplo 3: Serie de Fibonacci
# .........................................................


def FibonacciRecursivo(n):
    if n == 0 or n == 1:
        return n
    return FibonacciRecursivo(n - 1) + FibonacciRecursivo(n - 2)


n = 60
print(FibonacciRecursivo(n - 1))


##########################################################################
# Algoritmos Greedy
##########################################################################

# ................................
# Ejemplo 1
# ................................

def Algoritmo(A, T):
    NumeroTareas = 0
    TiempoUsado = 0

    A.sort()
    for i in range(len(A)):
        TiempoUsado += A[i]
        if TiempoUsado > T:
            break
        NumeroTareas += 1

    return NumeroTareas


A1 = [6, 4, 5, 3, 2]
A2 = [25, 56, 10, 13, 12]
A3 = [5, 3, 4, 2, 1]
T1 = 9
T2 = 25
T3 = 6
print("Maximo numero de tareas: ", Algoritmo(A3, T3))


# ................................
# Ejemplo 2
# ................................

def Algoritmo(A, k):
    l = 0
    p = 0
    capturas = 0
    Ladron = []
    Policia = []

    # Almacenar indices
    for i in range(len(A)):
        if A[i] == 'P':
            Policia.append(i)
        elif A[i] == 'L':
            Ladron.append(i)

            # Buscar los indices actuales mas bajos
    while l < len(Ladron) and p < len(Policia):
        if abs(Ladron[l] - Policia[p]) <= k:
            capturas += 1
            l += 1
            p += 1

        elif Ladron[l] < Policia[p]:
            l += 1
        else:
            p += 1

    return capturas


A1 = ['P', 'L', 'L', 'P', 'L']
A2 = ['P', 'L', 'P', 'L', 'L', 'P']
A3 = ['P', 'L', 'P', 'L', 'L', 'P']
k1 = 2
k2 = 2
k3 = 2
print("Maximo numero de ladrones capturados: ", Algoritmo(A1, k1))

################################################################
# ACTIVIDAD 2
################################################################


def multiplos5(n):
    if n == 1:
        resultado = 5
        print(resultado)
        return resultado
    else:
        resultado = multiplos5(n - 1) + 5
        print(resultado)
        return resultado


n = 10
multiplos5(n)


def invertirlista(lista):
    if not lista:
        return []
    else:
        return lista[-1:] + invertirlista(lista[:-1])


Lista = [1, 24, 3, 41, 5]
print(invertirlista(Lista))

# El problema del vendedor viajero o TSP (Travelling Salesman Problem), consiste en que dado un n´umero de
# ciudades n y las distancias entre cada par de ellas dij , encontrar la ruta m´as corta posible que visita cada
# ciudad exactamente una vez y al finalizar regresa a la ciudad de origen (partida). Implemente una funci´on
# en python que retorne la ruta m´as corta mediante un algortimo de bactracking.
# Su implementaci´on debe considerar:
# Nombre funci´on: EvaluarRutas()
# Input funci´on: diccionario llamado ciudades con la distancia entre las n ciudades.
# Output funci´on: Lista con el orden de las ciudades a visitar, y su distancia total.
# - n tomar´a valores enteros entre 3 y 15, inclusive.
# - dij tomar´a valores enteros entre 10 y 200, inclusive.
# - Considere que todas las ciudades estan conectadas.
import random

random.seed(2)


def permutacion(arr, l, r, dic: dict):
    if (l == r):
        c = 0
        val = []
        for i, o in enumerate(arr):
            if i + 1 < len(arr):
                d = arr[i + 1]
            else:
                d = arr[0]
            c = c + dic[o, d]
            val.append(c)
        print(arr, c)
    else:
        for i in range(l, r + 1):
            temp = arr[l]
            arr[l] = arr[i]
            arr[i] = temp
            # print('Cambio: ', arr)
            permutacion(arr, l + 1, r, dic)
            # Backtracking
            temp = arr[l]
            arr[l] = arr[i]
            arr[i] = temp
            # print('Backtracking: ', arr)


n = 3
dij = {(i, j): random.randrange(10, 200, 10) for i in range(1, n + 1) for j in range(1, n + 1) if i != j}
ciudades = [j for j in range(1, n + 1)]
l = 0
r = len(ciudades) - 1

results = permutacion(ciudades, l, r, dij)
